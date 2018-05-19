from __future__ import absolute_import, print_function, unicode_literals

import os
import sys
import boto3

from common import folders, versions

def main():

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

    def get_args():
        local_directory = None
        bucket_name = None
        destination = None
        if len(sys.argv) == 4:
            local_directory, bucket_name, destination = sys.argv[1:4]
        elif len(sys.argv) == 2:
            local_directory = sys.argv[1]
        return local_directory, bucket_name, destination

    def remove_unwanted(dirs):
        dirs[:] = [d for d in dirs if d in folders]

    local_directory, bucket_name, destination = get_args()
    if bucket_name is not None:
        session, s3, bucket = setup_s3(bucket_name)
    else:
        session, s3, bucket = None, None, None

    bucket_root = os.path.join(destination, os.path.basename(local_directory))

    for root, dirs, files in os.walk(local_directory):
        if os.path.basename(root) in versions:
            remove_unwanted(dirs)

        for f in files:
            path = os.path.join(root, f)
            upload_to = os.path.normpath(os.path.join(os.path.join(bucket_root, root), f))
            bucket.upload_file(path, upload_to)
            print("{} uploaded to {}".format(path, "s3://{}/{}".format(bucket_name, upload_to)))


main()