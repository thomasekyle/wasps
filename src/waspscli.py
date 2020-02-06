# wasp-cli.py #
# A python cli script for consuming and updating
# AWS Parameter Store in AWS.

import json
import configparser
import argparse
import waspsclient

parser = argparse.ArgumentParser(description='waspscli.py - A CLI tool for consuming and modifying the AWS parameter store.')
parser.add_argument(
            '--profile', '-p',
            metavar='myprofile', 
            type=str, 
            nargs='?',
            help='The AWS profile you wish to use. Located in ~/.aws/credentials')
parser.add_argument(
            '--access-key', '-a',
            metavar='your_aws_access_key',
            type=str,
            nargs='?',
            help='The AWS access key you wish to use to authenticate.')
parser.add_argument(
            '--secret-key', '-s',
            metavar='your_aws_secret_key',
            type=str,
            nargs='?',
            help='The AWS secret key you wish to use to authenticate.')   
parser.add_argument(
            '--session-', '-l',
            metavar='your_aws_session',
            type=str,
            nargs='?',
            help='The AWS session token you wish to use to authenticate.')
parser.add_argument(
            '--region', '-r',
            metavar='your_aws_region',
            type=str,
            nargs='?',
            help='The AWS region you wish to authenticate to.')
parser.add_argument(
            '--parameter-path', '-d',
            metavar='/path/to/params1, /path/to/params2',
            type=str,
            nargs='*',
            help='The parameters you wish to retrieve from the store.')
parser.add_argument(
            '--json', '-j',
            metavar='/path/to/config.json',
            type=str,
            nargs='?',
            help='The path to the JSON file you wish to output after retrieving the parameters.')
parser.add_argument(
            '--ini', '-i',
            metavar='/path/to/config.ini',
            type=str,
            nargs='?',
            help='The path to the INI file you wish to output after retrieving the parameters.')
parser.add_argument(
            '--properties', '-o',
            metavar='/path/to/application.properties',
            type=str,
            nargs='?',
            help='The path to the Java properties file you wish to output after retrieving the parameters.')
parser.add_argument(
            '--config', '-c',
            metavar='/path/to/config.json',
            type=str,
            nargs='?',
            help='The path to the JSON configuration you wish to generate parameters from.')
parser.add_argument(
            '--config-json', '-',
            metavar="""{'a': '1', 'b' : '2'}""",
            type=str,
            nargs='?',
            help='The JSON configuration string you wish to generate parameters from.')
parser.add_argument(
            '--supress', '-n',
            action='store_true',
            default=False,
            help='Supress output of the parameter to stdout. Use if you have sensitive outputs.')            

args = parser.parse_args()

#For testing
if (not args.profile and not args.access_key):
    wasps_store = waspsclient.create_store_from_profile('default')
parameters = waspsclient.get_parameters_from_path(wasps_store, ["/dev/python-app"])
print(parameters)

