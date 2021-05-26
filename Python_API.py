# using Python to create an API call using packages called requests
# Dependencies are pip

import requests
import json
#
# response_bbc = requests.get("https://www.bbc.co.uk/")
# print(response_bbc)
# print(response_bbc.status_code)
# print(response_bbc.headers)


post_api_response = requests.get("https://api.postcodes.io/postcodes/se120nb")
print(post_api_response.status_code)
if post_api_response.status_code == 200:
    print(f"Thanks for your request {post_api_response.status_code}")
else:
    print("Sorry the postcode is incorrect ")

