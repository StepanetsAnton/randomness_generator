import random

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

triads = ["000", "001", "010", "011", "100", "101", "110", "111"]

sliced = [user_data[symbol:symbol+4] for symbol in range(0, len(user_data))]


triads_followed_by_0 = {"000":0}
for triad in triads:
    triads_followed_by_0.update({triad:0})
triads_followed_by_1 = {"000":0}
for triad in triads:
    triads_followed_by_1.update({triad:0})

for element in sliced:
    if len(element)==4:
        for triad in triads:
            if element.startswith(triad):
                if element[3] == "0":
                    temp = triads_followed_by_0[triad]
                    triads_followed_by_0.update({triad:(temp+1)})
                else:
                    temp=triads_followed_by_1[triad]
                    triads_followed_by_1.update({triad:(temp+1)})

print()

test_string = ""
while len(test_string) < 4:
    test_string=str(input("Please enter a test string containing 0 or 1:"))

max_poss=len(test_string)-3
pred_count=0
prediction=""

sliced2 = [test_string[symbol:symbol+4] for symbol in range(0, len(test_string))]
for element in sliced2:
    if len(element)==4:
        for triad in triads:
            if element.startswith(triad):
                if triads_followed_by_0[triad]>triads_followed_by_1[triad]:
                    prediction+="0"
                    if element[3]=="0":
                        pred_count+=1
                elif triads_followed_by_0[triad]<triads_followed_by_1[triad]:
                    prediction+="1"
                    if element[3]=="1":
                        pred_count+=1
                else:
                    rand = random.choice(["0","1"])
                    prediction+=rand
                    if element[3]==rand:
                        pred_count+=1

print("predictions:\n"+prediction)
print("Computer guessed "+str(pred_count)+" out of "+str(len(test_string))+" symbols right ("+str(pred_count/max_poss*100)+" %)")