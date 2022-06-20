import os
print('Start')
print(os.environ.get("BUCKET_NAME", "Not Found"))
print(os.environ.get("KEY1", "Not Found"))
print('Finish')
def hello_http(request):
   """HTTP Cloud Function.
   Args:
       request (flask.Request): The request object.
       <https://flask.palletsprojects.com/en/1.1.x/api/#incoming-request-data>
   Returns:
       The response text, or any set of values that can be turned into a
       Response object using `make_response`
       <https://flask.palletsprojects.com/en/1.1.x/api/#flask.make_response>.
   """
   request_json = request.get_json(silent=True)
   request_args = request.args

   if request_json and 'name' in request_json:
       name = request_json['name']
   elif request_args and 'name' in request_args:
       name = request_args['name']
   else:
       name = 'Deepsphere!!!!'
       k1,k2,k3 = get_gcp_secret()
       print('Secret Values1 - ',k1)
       print('Secret Values2 - ',k2)
       print('Secret Values3 - ',k3)
   return 'Hello {}!'.format(name)



def get_gcp_secret():

    # Create the Secret Manager client.
    client = secretmanager.SecretManagerServiceClient()
    
    # Build the resource name of the secret version.
    aws_access_key_name =  os.environ.get('ACCESS_KEY','Specified environment variable GCP_SECRET_AWS_ACCESS_KEY is not set.')
    aws_secret_key_name =  os.environ.get('SECRET_KEY','Specified environment variable GCP_SECRET_AWS_SECRET_KEY is not set.')
    bucket_name =  os.environ.get('BUCKET_NAME','Specified environment variable BUCKET_NAME is not set.')
    
    # Access the secret version.
    aws_access_key_response = client.access_secret_version(request={"name": aws_access_key_name})
    aws_secret_key_response = client.access_secret_version(request={"name": aws_secret_key_name})
    bucket_name_response = client.access_secret_version(request={"name": bucket_name})
    # WARNING: Do not print the secret in a production environment - this
    # snippet is showing how to access the secret material.
    aws_access_key = aws_access_key_response.payload.data.decode("UTF-8")
    aws_secret_key = aws_secret_key_response.payload.data.decode("UTF-8")
    bucket_name_value = bucket_name_response.payload.data.decode("UTF-8")
    return aws_access_key,aws_secret_key
