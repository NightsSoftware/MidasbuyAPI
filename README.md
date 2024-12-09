<h1 align="center">
    ⚡️ MidasbuyAPI ⚡️
</h1>

<h4 align="center">
    🧩 API for Midasbuy Top-up Store (<a href="https://www.midasbuy.com">midasbuy.com</a>): PUBG codes activation, getting players info and more! 🧩
</h4>

<p align="center">
	<img src="https://i.ibb.co/CKy39V8/2024-12-09-132947302.png" alt="MidasbuyAPI"/>
</p>

<p align="center">
    <img src="https://i.ibb.co/w6YR6wS/2024-12-09-134630664.png" alt="MidasbuyAPI"/>
</p>

## 💫 **Documentation & Endpoints**

- **Online documentation is available here: https://midasbuyapi.nightstranger.space**

## 🗝️ **API key**

- To make requests to the API you will need only 1 thing - API key (X-Api-Key request header). It is used to control the number of requests. 
- **To get an API key, contact the developer: https://t.me/NightStrang6r**


## ☑️ **Examples**

### Activate PUBG code

```python
import requests

# API URL and headers
url = "https://midasbuyapi.nightstranger.space/api/v1/pubg/activate"
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "<your_api_key>"  # Replace with your API key
}

# Request payload
data = {
    "player_id": 555555555,  # Replace with the player's ID
    "uc_code": "rX7rASS72a25qdVcg0"  # Replace with the activation code
}

try:
    # Sending POST request
    response = requests.post(url, headers=headers, json=data)

    # Handling success responses
    if response.status_code == 200:
        result = response.json()
        if result["success"] and result["data"]["status"] == "success":
            print("\n🎉 Code activated successfully!")
            print(f"👤 Player: {result['data'].get('player_name', 'Unknown')} (ID: {result['data']['player_id']})")
            print(f"🔑 Code: {result['data']['code_activated']}")
            print(f"⏰ Activated at: {result['data']['activated_at']}")
        else:
            print("\n⚠️ Activation failed.")
            print(f"❌ Reason: {result['data']['message']}")
            print(f"🔑 Code: {result['data']['code_activated']}")
            if "activated_to" in result["data"]:
                print(f"🔁 Already activated for Player ID: {result['data']['activated_to']}")

    # Handling other responses
    elif response.status_code == 400:
        print("\n⚠️ Bad Request.")
        print(f"Message: {response.json().get('message', 'Invalid request data')}")
    elif response.status_code == 401:
        print("\n🔒 Unauthorized.")
        print(f"Message: {response.json().get('message', 'API key required')}")
    elif response.status_code == 500:
        print("\n💥 Server Error.")
        print(f"Message: {response.json().get('message', 'Internal server error')}")
    else:
        print("\n❓ Unexpected status code:", response.status_code)
        print("Response:", response.json())

# Handling request exceptions
except requests.RequestException as e:
    print("\n🚨 Request failed:", str(e))
```

### Get PUBG player info by ID

```python
import requests

# API URL and headers
url = "https://midasbuyapi.nightstranger.space/api/v1/pubg/getPlayer"
headers = {
    "Content-Type": "application/json",
    "X-Api-Key": "<your_api_key>"  # Replace with your API key
}

# Request payload
data = {
    "player_id": 555555555  # Replace with the player's ID
}

try:
    # Sending POST request
    response = requests.post(url, headers=headers, json=data)

    # Handling success responses
    if response.status_code == 200:
        result = response.json()
        if result["success"] and result["data"]["status"] == "success":
            print("\n🎉 Player information retrieved successfully!")
            print(f"👤 Player Name: {result['data'].get('player_name', 'Unknown')}")
            print(f"🆔 Player ID: {result['data']['player_id']}")
        else:
            print("\n⚠️ Player information not found.")
            print(f"❌ Reason: {result['data']['message']}")
            print(f"🆔 Player ID: {result['data']['player_id']}")

    # Handling other responses
    elif response.status_code == 400:
        print("\n⚠️ Bad Request.")
        print(f"Message: {response.json().get('message', 'Invalid request data')}")
    elif response.status_code == 401:
        print("\n🔒 Unauthorized.")
        print(f"Message: {response.json().get('message', 'API key required')}")
    elif response.status_code == 500:
        print("\n💥 Server Error.")
        print(f"Message: {response.json().get('message', 'Internal server error')}")
    else:
        print("\n❓ Unexpected status code:", response.status_code)
        print("Response:", response.json())

# Handling request exceptions
except requests.RequestException as e:
    print("\n🚨 Request failed:", str(e))
```

## 🎉 **Like it? Star it!**

Please rate this repository by giving it a star rating in the top right corner of the GitHub page (you must be logged in to your account). Thank you ❤️

![](https://i.ibb.co/x3hFFvf/2022-08-18-132617815.png)