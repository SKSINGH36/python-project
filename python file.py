x = int(input("Enter your marks (out of 600): "))

if 0 <= x <= 600:
    print("My marks =", x)

    p = (x / 600) * 100
    print("My percentage = {:.2f}%".format(p))

    if p >= 90:
        g = "A+"
    elif p >= 80:
        g = "A"
    elif p >= 70:
        g = "B+"
    elif p >= 60:
        g = "B"
    elif p >= 50:
        g = "C+"
    elif p >= 40:
        g = "C"
    elif p >= 30:
        g = "D"
    else:
        g = "F"

    print("My Grade:", g)

    if g == "F":
        print("This student has failed.")
else:
    print("Invalid marks! Please enter marks between 0 and 600.")