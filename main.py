import requests
import json

panel_domain = input("Enter the panel domain (e.g., https://panel.example.com): ")
api_key = input("Enter your API key: ")
remote_id = input("Enter the remote ID (e.g., 24): ")
url = f"{panel_domain}/api/application/servers/external/{remote_id}"
headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
}
response = requests.get(url, headers=headers)
if response.status_code == 200:
    print("Success! Here's the detailed information:")
    data = response.json()
    for key, value in data.items():
        print(f"{key.capitalize()}: {json.dumps(value, indent=4)}")
else:
    print(f"Failed to fetch data. Status code: {response.status_code}")
    print("Response content:", response.text)
