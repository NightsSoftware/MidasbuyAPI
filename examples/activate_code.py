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