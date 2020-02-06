# client.py #
# A client library for authenticating with AWS and
# utilizing a parameter store

import sys
import json
import boto3
from ssm_parameter_store import EC2ParameterStore
from collections import OrderedDict



def create_store():
    """
    Creates a parameter store object from the default AWS credential on the
    (if there are any). This would mainly be used for EC2 instances with
    assigned IAM roles.

    Parameters:
        N/A

    Returns:
        Object: An AWS parameter store object.
    """
    client = boto3.Session()
    credentials = client.get_credentials()
    credentials = credentials.get_frozen_credentials()
    store = EC2ParameterStore(
        aws_access_key_id=credentials.access_key,
        aws_secret_access_key=credentials.secret_key,
        aws_session_token=client._session,  # optional
        region_name=client.region_name
    )
    return store


def create_store_from_profile(profile='default'):
    """
    Creates a parameter store object from the provided profile. If one is
    not provided it will try to use the default one.
    
    Arguments:
        profile {string} -- The name of the aws profile you wish to use. Looks
        at the config in ~/.aws/credentials

    Returns:
        Object -- An AWS parameter store object.
    """
    client = boto3.Session(profile_name=profile)
    credentials = client.get_credentials()
    store = EC2ParameterStore(
        aws_access_key_id=credentials.access_key,
        aws_secret_access_key=credentials.secret_key,
        #aws_session_token=client._session, # optional
        region_name=client.region_name
    )
    return store


def create_store_from_creds(access_key, secret_key, region, **kwargs):
    """
    Creates a parameter store object from the provided credentials.
    
    Arguments:
        access_key {string} -- The access key for your AWS account
        secret_key {string} -- The secret key for you AWS account
        region {string} -- The region you wish to connect to
    
    Keyword Arguments (Optional):
        session='session' {string} -- The session token you wish to use.
    
    Returns:
        Object -- An AWS parameter store object.
    """
    session = kwargs.get('session') if 'session' in kwargs else ''
    store = EC2ParameterStore(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        aws_session_token=session, #optional
        region_name=region
    )
    return store

def get_parameters_from_path(store, paths, **kwargs):
    """
    Gets parameters from the specified paths and combines them
    into one dictionary. Values that are the same WILL be overwritten.
    
    Arguments:
        store {EC2ParameterStore} -- The AWS Parameter Store you wish to use
        paths {array} -- The paths you wish to get variables from
    
    Returns:
        OrderedDict -- An OrderedDict of all of the value from the parameter store.
    """
    params = OrderedDict()
    for p in paths:
        temp_parameters = store.get_parameters_with_hierarchy(f"{p}", decrypt=True)
        params.update(temp_parameters)
    return params
