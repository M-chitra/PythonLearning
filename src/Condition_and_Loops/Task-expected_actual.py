"""
Q2

In automation, you often compare expected and actual outputs.
Write code to check if a test case passed or failed.

expected_title = "Dashboard"
actual_title = "Dashboard "

✅ Test Passed – Title matches


True - why >  Strip and convert them into the lowercase = both of them are equal.


"""
Expected_tittle = str(input("Please enter your expected tittle: "))
Actual_tittle = str(input("Please enter your actual tittle: "))

if Expected_tittle.lower().strip() == Actual_tittle.lower().strip():
    print("Test Passed - Tittle Matched")
else:
    print("Test Failed - Tittle Not Matched")