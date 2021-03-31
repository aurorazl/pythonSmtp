import requests
from requests.auth import HTTPBasicAuth

re = requests.get("http://127.0.0.1:5000/apis/Infer",auth=HTTPBasicAuth("rootRedfish","Machine@123"))
print(re.content)
