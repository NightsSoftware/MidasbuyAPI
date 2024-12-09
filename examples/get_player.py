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