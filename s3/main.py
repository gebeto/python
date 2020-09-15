import boto3
import botocore
import time
import os


def file_exists(bucket, file_path):
	try:
		bucket.Object(file_path).get()
		return True
	except botocore.exceptions.ClientError as e:
		if e.response['Error']['Code'] == 'NoSuchKey':
			print('NoSuchKey')
	return False


def get_file_name_with_timestamp(file_name):
	timestamp = str(int(time.time() * 1000))
	file_name_split = list(os.path.splitext(file_name))
	file_name_split[0] = file_name_split[0] + '-' + str(timestamp)
	return "".join(file_name_split)


def upload_file(load_number, file_name, file):
	s3 = boto3.resource('s3',
		aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
		aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
	)
	bucket = s3.Bucket('tms-system-docs')

	file_name = get_file_name_with_timestamp(file_name)
	file_path = f'load/{load_number}/{file_name}'

	return bucket.put_object(Key=file_path, Body=file)


upload_file('1', 'test.txt', open("test.txt", "rb"))