import requests
import json

url = "https://[kpi-url]/api/v2/assets/[asset_uid]/exports.json"  # Replace [kpi-url] with your server details, & [asset_uid] with your assets_uid

headers = {
    "Authorization": "Token [your_token_goes_here]",  # Replace [your_token_goes_here] with your API key
    "Content-Type": "application/json"
}

# Construct the payload // You can also configure the payload to reflect the settings in KPI:

payload = {
    "fields_from_all_versions": True,
    "fields": [],
    "group_sep": "/",
    "hierarchy_in_labels": False,
    "lang": "English (en)",     
    "name": "name",              # you can give a name to your export
    "multiple_select": "summary",
    "type": "xls",
    "xls_types_as_text": False,
    "include_media_url": True,
    "query": {
        "$and": [
            {
                "_submission_time": { # _submission_time can also be replase with any fields in the submissions
                    "$gte": "2024-11-01T00:00:00",  # Replace with start date and time
                    "$lt": "2024-12-01T00:00:00"    # Replace with end date and time
                }
            }
        ]
    }
}


# Perform the POST request
try:
    response = requests.post(url, headers=headers, json=payload)

    # Check the response status code
    if response.status_code == 201:
        # Parse the response
        data = response.json()
        print("Export successful!")
        print(json.dumps(data, indent=2))
    elif response.status_code == 400:
        print("Bad Request: The server couldn't process the request. Check the payload and headers.")
        print("Details:", response.text)
    elif response.status_code == 401:
        print("Unauthorized: Check the access token.")
    elif response.status_code == 403:
        print("Forbidden: The token might lack permissions for this asset.")
    elif response.status_code == 404:
        print("Not Found: The asset_uid might be incorrect or does not exist.")
    elif response.status_code == 500:
        print("Internal Server Error: Something went wrong on the server side.")
    else:
        print(f"Unexpected Error: {response.status_code}")
        print("Response Details:", response.text)

except requests.exceptions.RequestException as e:
    print("Request failed due to an exception:", str(e))
