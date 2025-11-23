# Grade Calculator

Score = int(input("Enter your Score:\n").strip())

if Score > 100 or Score < 0:
    print("❌ Your are super man!!!❌")
else:
    if 90 <= Score <= 100:
        print("You are grade is A")
    elif 80 <= Score < 90:
        print("You are grade is B")
    elif 70 <= Score < 80:
        print("You are grade is C")
    elif 60 <= Score < 70:
        print("You are grade is D")
    else:
        print("You are grade is F")
