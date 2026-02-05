def square_digits(x):
    s = str(x)
    result = 0
    for i in range(len(s)):
        result += int(s[i])**2
    return result

def arrives89(x):
    i = x
    found1or89 = False
    while (not found1or89):
        i = square_digits(i)
        if ((i==1) or (i==89)):
            found1or89 = True
    return (i==89)



# ------------- MAIN PART OF SCRIPT -----------------

count = 0
for i in range(1,10000000):
    if (arrives89(i)):
        count += 1

print(f"{count} starting numbers below ten million will arrive at 89.")

