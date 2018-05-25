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
        if len(sys.argv) == 3:
            local_directory, bucket_name = sys.argv[1:3]
        elif len(sys.argv) == 2:
            local_directory = sys.argv[1]
        return local_directory, bucket_name

    def create_folder_if_dne(key, root):
        directory = os.path.dirname(key)
        # No need to do recursive calls because of makedirs
        full_name = os.path.normpath(os.path.join(root, directory))
        if not os.path.exists(full_name):
            os.makedirs(full_name)



    local_directory, bucket_name = get_args()
    if bucket_name is not None:
        session, s3, bucket = setup_s3(bucket_name)
    else:
        session, s3, bucket = None, None, None

    bucket_root = os.path.join(destination, os.path.basename(local_directory))


    for key in my_bucket.objects.all():
        create_folder_if_dne(key, local_directory)
        my_bucket.download_file(key.key, os.path.normpath(os.path.join(local_directory, key.key)))
        print("{} downloaded to {}".format("s3://{}/{}".format(bucket_name, upload_to)), os.normpath(os.path.join(local_directory, key.key)))


main()