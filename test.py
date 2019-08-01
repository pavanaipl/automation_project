import unittest

from testapp import sum
import json
import requests


def create_product(headers,passed_data,passed_data_count):
    product_data = {
        "ProductName": "sudhan",
        "rentAmount": "30",
        "rentFromDate": "2019-05-15T09:19:26.297Z",
        "rentToDate": "2019-05-15T09:19:26.297Z",
        "rentToInMilliseconds": "157845",
        "belongsTo": "5cd3dd04bf1fd36c68fcf6b7",
        "rentFromInMilliseconds": "158589",
        "rentType": "withConfirmation",
        "minimumRentDays": "1",
        "maximumRentDays": 20,
        "details": "MTB cycle",
        "hiringType": "oneTime"
    }
    product_url = "http://demo.knoit.co/v6/hiring/hiringProduct"
    product_response = requests.post(product_url, product_data, headers=headers)
    product_json = json.loads(product_response.content.decode('utf-8'))
    product_json["product_url"] = product_url
    data = {"url":product_url}
    passed_data_count +=1
    passed_data.append(data)
    print (passed_data_count,"inside function")
    print (passed_data,"passed_data")
    return (product_json,passed_data_count,passed_data)

class TestSum(unittest.TestCase):
    def test_list_int(self):
        """
        Test that it can sum a list of integers
        """
        passed_data = []
        failed_data = []
        not_found_data = []
        server_error_data = []
        passed_data_count = 0
        not_found_data_count = 0
        server_error_data_count = 0
        failed_data_count = 0
        data = {
            "password":"cWPQlLFinKU0oA4nAZsKMhYHnsY2",
            "phoneNumber":"9876544560",
            "osVersion":"28",
            "mobileType":"android",
            "fcmToken":"cjDo-J10OMA:APA91bFMvV8IpaGkM_48v5s9b6S1y3ytOYA4wa9dIKnQNX0MoZlDLypnjVLgm99gVu5RewVCj7hBwykovSXxxFUv8fxY7FaxEjoAqLm62-ZERi0373X5IR97Z-P4r-RQXkSKgLKRzkZb",
            "email":"9876544560@knoit.com"
        }
        api_url = "http://demo.knoit.co/v6/users/numberAuthentication"
        response = requests.post(api_url, data)
        new_response = json.loads(response.content.decode('utf-8'))
        if new_response["statusCode"] == 404:
            data = {"url": api_url}
            not_found_data.append(data)
            not_found_data_count+=1
        if new_response["statusCode"] == 400:
            data = {"url": api_url}
            failed_data.append(data)
            failed_data_count += 1
        if new_response["statusCode"] == 200 :
            data = {"url":api_url}
            passed_data_count+=1
            passed_data.append(data)
            otp_data={
                "email":"saranya@appinessworld.com",
                "OTP":1010
            }
            otp_url = "http://demo.knoit.co/v6/users/verify"
            verification_response = requests.post(otp_url, otp_data)
            verification_json = json.loads(verification_response.content.decode('utf-8'))
            if verification_json["statusCode"]== 200 :
                jwt_token = verification_json["data"]["token"]["jwt"]
                headers = {"Authorization" : jwt_token}
                product_json = create_product(headers,passed_data,passed_data_count)
                print(product_json,"product_json")
                product_url = product_json["product_url"]
                details_url = product_url +"/"+ product_json["data"]["id"]
                get_product_details = requests.get(details_url, headers = headers)
                product_detals = json.loads(get_product_details.content.decode('utf-8'))
                print (product_detals)
        print (passed_data,"passed_data")
        print (passed_data_count,"passed data count")
        print (not_found_data, "not_found_data")
        print (not_found_data_count, "not found data count")

if __name__ == '__main__':
    unittest.main()

