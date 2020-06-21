import boto3


ACCESS_KEY= ''
SECRET_KEY= ''
# SESSION_TOKEN=

client = boto3.client(
    's3',
    aws_access_key_id=ACCESS_KEY,
    aws_secret_access_key=SECRET_KEY,
    # aws_session_token=SESSION_TOKEN,
)


bucket = client.list_buckets()['Buckets'][0]['Name']

print(client.get_object(Bucket=bucket,
                        Key=''))
