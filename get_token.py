import requests
from dotenv import load_dotenv, set_key
import os

def get_token():
    load_dotenv(override=True)

    # Base url currently points to PROD, can be changed
    base_url = "https://optimus.fulcrumhq.build"
    endpoint = "/api/TokenAuth/Authenticate"

    # # Base url currently points to QAS platform, can be changed
    # base_url = "https://optimus-qas.fulcrumhq.build"
    # endpoint_auth = "/api/TokenAuth/Authenticate"

    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36",
        "Authorization": f"Bearer {os.getenv('ACCESS_TOKEN')}"
    }

    payload = {
    "userNameOrEmailAddress": os.getenv('SVC_USERNAME'),
    # QAS
    # "password": "8KA9qMcRM97r",
    # "password": "m8rsRLb11K4T",
    # PROD
    'password': os.getenv('SVC_PASSWORD'),
    "rememberClient": False,
    "twoFactorRememberClientToken": None,
    "singleSignIn": False,
    "returnUrl": None,

    }

    response = requests.post(base_url+endpoint, headers=headers, json=payload)
    print(response.status_code)

    if response.status_code != 200:
        raise Exception(response.json()["error"]["message"])
    
    print("Token successful obtained")
    
    # Directly parse the JSON response
    response_json = response.json()
    access_token = response_json.get("result", {}).get("accessToken")
        
    if access_token:
        print(f"Access Token: {access_token}")
        # Store the access token in the .env file
        set_key(".env", "ACCESS_TOKEN", access_token)
    else:
        print("Access token not found in the response.")

# For testing purposes
if __name__ == "__main__":
    get_token()