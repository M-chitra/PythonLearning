"""
Q3

You want to check whether a web page loads within 3 seconds (performance test condition).

load_time = 4.2
⚠️ Page load too slow: 4.2 seconds

"""

Loading_time = float(input("Please enter your loading time: "))

if Loading_time <=3:
    print("Page loading looks good:", Loading_time ,"Seconds")
else:
    print("Page loading to slow:" + str(Loading_time) + " Seconds")