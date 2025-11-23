"""
Q4
Check if the user can log in based on correct username and password.

I/p

username = "admin"
password = "1234"

O/p
✅ Login Successful


For the Fail condition Other O/P = ❌ Invalid Credentials
"""

Correct_username = "admin"
Correct_password = "1234"

Username = str(input("Please enter your login username: "))
Password = str(input("Please enter your login password: "))

if Username == Correct_username and Password == Correct_password:
    print("✅ Login Successful")
else:
    print("❌ Invalid Credentials")