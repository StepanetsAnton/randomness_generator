user_data = ""
temp = ""

while len(user_data)<100:
    prompt = str(input("Print a random string containing 0 or 1:"))

    for x in prompt:
        if x == "0" or x == "1":
            user_data+=x


    print("Current data length is ", len(user_data),",",(100-len(user_data)),"symbols left")

print()
print("Final data string:")
print(str(user_data))