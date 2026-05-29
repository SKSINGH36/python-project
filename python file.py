x = int(input("Enter your mark: "))
print("My mark =", x)

p = x / 600 * 100
print("My percentage =", p)

if p >= 90:
    g = "A+"
    print("My Grade:", g)

elif p >= 80 and p < 90:
    g = "A"
    print("My Grade:", g)

elif p >= 70 and p < 80:
    g = "B+"
    print("My Grade:", g)

elif p >= 60 and p < 70:
    g = "B"
    print("My Grade:", g)

elif p >= 50 and p < 60:
    g = "C+"
    print("My Grade:", g)

elif p >= 40 and p < 50:
    g = "C"
    print("My Grade:", g)

elif p >= 30 and p < 40:
    g = "D"
    print("My Grade:", g)

elif p >= 0 and p < 30:
    g = "F"
    print("This student is fail. Grade:", g)

else:
    print("Invalid marks")