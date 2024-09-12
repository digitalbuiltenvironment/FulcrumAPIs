import json
import requests

# API endpoint
url = 'https://optimus.fulcrumhq.build/api/TokenAuth/Scope/Elevate'

# # Your API token (if required)
# need to copy everytime you log in and call ObtainAccessToken
api_token = 'eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJodHRwOi8vc2NoZW1hcy54bWxzb2FwLm9yZy93cy8yMDA1LzA1L2lkZW50aXR5L2NsYWltcy9uYW1laWRlbnRpZmllciI6IjMyNDMiLCJBc3BOZXQuSWRlbnRpdHkuU2VjdXJpdHlTdGFtcCI6IkJEMzRXMkgyQTRDTldRRURZVDRCT0hSQ1BOSE1QTE1BIiwiaHR0cDovL3d3dy5hc3BuZXRib2lsZXJwbGF0ZS5jb20vaWRlbnRpdHkvY2xhaW1zL3RlbmFudElkIjoiMTAwNyIsInN1YiI6IjMyNDMiLCJqdGkiOiI4ZDcxYTBjOS0wM2RmLTRlN2QtOTA3OC03NTE1NTZhY2FhZGEiLCJpYXQiOjE3MjE5NTk5MjQsInRva2VuX3ZhbGlkaXR5X2tleSI6ImI2MmI3ZGQ3LWY5ZmMtNGUxNS04NTU4LTQ4MjMxZTJlN2RmYyIsInVzZXJfaWRlbnRpZmllciI6IjMyNDNAMTAwNyIsInRva2VuX3R5cGUiOiIwIiwibmJmIjoxNzIxOTU5OTI0LCJleHAiOjE3MjE5NjM1MjQsImlzcyI6Ikx0RmllbGQiLCJhdWQiOiJMdEZpZWxkIn0.fGZsEzTJlFvmHeSwJCAdF6EGhtlCf9Sk-6EfgGYtqdQ'

# # Headers (if needed)
# headers = {'Authorization': f'Bearer {api_token}'}

def set_user_agent(choice):
    useragents = [
        "PostmanRuntime/7.36.3",
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
    ]
    return useragents[choice]

headers = {
    "User-Agent": set_user_agent(choice=1),
    "Authorization": f'Bearer {api_token}'
    }


payload = {
    "userNameOrEmailAddress": "SVC_FORMS",
    # QAS
    # "password": "8KA9qMcRM97r",
    # "password": "m8rsRLb11K4T",
    # PROD
    'password': "hLd4OdH29UIF",
    "rememberClient": False,
    "twoFactorRememberClientToken": None,
    "singleSignIn": False,
    "returnUrl": None,
}

# Make the request
response = requests.request("POST", url, headers=headers, json=payload)

# Print the response
print(response.json())