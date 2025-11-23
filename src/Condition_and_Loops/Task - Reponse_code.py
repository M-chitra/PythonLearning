"""
1. Q - You receive an API response code from your test script.
Write an if-else block to check whether the response is successful (status code 200) or not.

I/P response = 404 , O/P ❌ Failed API Request
I/P response = 200 , O/P ✅ Passed API Request

"""

Response_code = int(input("Enter the Response Code: "))

if Response_code <100 or Response_code > 599:
    print("Please check the Response code is valid - The range only 100 to 599")
elif Response_code == 200:
    print("✅ Passed API Request - Successful", Response_code)
elif Response_code == 201:
    print("✅ Passed API Request - Created", Response_code)
elif Response_code == 204:
    print("✅ Passed API Request - Created but no content", Response_code)
elif Response_code == 404:
    print("❌ Failed API Request - Not found", Response_code)
elif Response_code == 400:
    print("❌ Failed API Request - Bad Request", Response_code)
elif Response_code == 401:
    print("❌ Failed API Request - Unauthorized", Response_code)
elif Response_code == 403:
    print("❌ Failed API Request - Forbidden", Response_code)
else:
    print("Unknow Response Code", Response_code)


