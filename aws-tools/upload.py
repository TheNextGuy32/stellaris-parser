import os
import sys
import boto3

from common import folders, versions

session = boto3.Session(
    aws_access_key_id = os.getenv("AWS_ACCESS_KEY"),
    aws_secret_access_key = os.getenv("AWS_SECRET_KEY"),
    region_name="us-east-1")

s3 = session.resource('s3')