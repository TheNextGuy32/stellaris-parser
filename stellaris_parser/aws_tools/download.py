from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
import boto3

from common import folders, versions

# Credit: https://stackoverflow.com/a/33350380/1021259
def download_dir(client, resource, dist, local='/tmp', bucket='your_bucket'):
    paginator = client.get_paginator('list_objects')
    for result in paginator.paginate(Bucket=bucket, Delimiter='/', Prefix=dist):
        if result.get('CommonPrefixes') is not None:
            for subdir in result.get('CommonPrefixes'):
                download_dir(client, resource, subdir.get('Prefix'), local, bucket)
        if result.get('Contents') is not None:
            for file in result.get('Contents'):
                if not os.path.exists(os.path.dirname(local + os.sep + file.get('Key'))):
                     os.makedirs(os.path.dirname(local + os.sep + file.get('Key')))
                resource.meta.client.download_file(bucket, file.get('Key'), local + os.sep + file.get('Key'))

def main(local_directory, bucket_name):

    def setup_s3(bucket_name):
        # Returns session, s3 and bucket
        session = boto3.Session(
            aws_access_key_id = os.getenv("AWS_ACCESS_KEY"),
            aws_secret_access_key = os.getenv("AWS_SECRET_KEY"),
            region_name="us-east-1")

        s3 = session.resource('s3')
        bucket = s3.Bucket(bucket_name)

        print("Setup S3 Bucket {}".format(bucket_name))

        return session, s3, bucket

    if bucket_name is not None:
        session, s3, bucket = setup_s3(bucket_name)
    else:
        session, s3, bucket = None, None, None

    client = session.client('s3')
    download_dir(client, s3, '/', local=local_directory, bucket=bucket_name)


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2])