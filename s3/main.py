import boto3
import botocore
import time
import os


BUCKET_NAME = 'tms-system-docs'

resource = boto3.resource('s3',
	aws_access_key_id=os.getenv("AWS_ACCESS_KEY_ID"),
	aws_secret_access_key=os.getenv("AWS_SECRET_ACCESS_KEY"),
)
client = resource.meta.client


def get_resource():
	return resource

def get_client():
	return client


def obj_to_dict(key, client=client):
	presigned_url = client.generate_presigned_url(
		'get_object',
		Params={
			'Bucket': BUCKET_NAME,
			'Key': key
		},
		ExpiresIn=3600
	)
	return {
		"title": os.path.split(key)[-1],
		"src": presigned_url,
	}

def file_exists(bucket, file_key):
	try:
		bucket.Object(file_key).get()
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
	s3 = get_resource()
	s3 = resource
	bucket = s3.Bucket(BUCKET_NAME)

	file_name = get_file_name_with_timestamp(file_name)
	file_key = f'load/{load_number}/{file_name}'

	obj = bucket.put_object(Key=file_key, Body=file)
	return obj_to_dict(file_key)


def all_documents(load_number):
	client = get_client()
	objs = client.list_objects_v2(Bucket=BUCKET_NAME, Prefix=f"load/{load_number}")["Contents"]
	files = [obj_to_dict(obj["Key"]) for obj in objs]
	return files
