# using Python to create an API call using packages called requests
# Dependencies are pip

import requests
import json

#
# response_bbc = requests.get("https://www.bbc.co.uk/")
# print(response_bbc)
# print(response_bbc.status_code)
# print(response_bbc.headers)


post_api_response = requests.get("https://api.postcodes.io/postcodes/" + "N160Eh")


# print(post_api_response.status_code)
# print(post_api_response.headers)
# post_api_response.json()
# print(json.dumps(post_api_response.json()["result"]["nhs_ha"]))
# testing the json dum function to allow the user to choice what section of infor they want
# for items in post_api_response.headers.values():
#    print(items)

# if post_api_response.status_code == 200:
#     print(f"Thanks for your request {post_api_response.status_code}")
# else:
#     print("Sorry the postcode is incorrect ")

###
# create a function to return the location/postcode if status code is 200
# get the user to input the postcode - validate the postcode before making the api call


# print(post_api_response.json()["result"])
# data = json.loads(json.dumps(post_api_response.json()["result"]))
# for item in data:
#     print(item)
# for items in str(post_api_response.json()["result"]):
#     print(items)


def PostCodeCheck():
    try:
        user_post = input("Enter your postcode ").upper()
        post_api_response = requests.get("https://api.postcodes.io/postcodes/" + user_post)
        print(post_api_response.status_code)
        if post_api_response.status_code == 200:
            print(f"Thanks for your request {post_api_response.status_code}")
            Json_keys = json.loads(json.dumps(post_api_response.json()[ "result" ]))  # prints the list of info
            for item in Json_keys:
                print(f"* {item}")
            User_Choice = input("Choice what extra info you would like ")
            print(json.dumps(post_api_response.json()[ "result" ][ User_Choice ]))
            # allows the user to choice from list of info
            # print(json.dumps(post_api_response.json()["result"]))
            # Will return the content of the page in a JSon format converting it from a dic
            return True
        else:
            print("Sorry the postcode is incorrect ")
            return False
    except KeyError:
        print("You entered an invalid choice try again")
        return True

PostCodeCheck()
