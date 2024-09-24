import random


print("Please provide AI some data to learn...")

user_data = ""
temp = ""
print("The current data length is "+ str(len(user_data))+", "+str((100-len(user_data)))+" symbols left")

while len(user_data)<100:
    prompt = str(input("Print a random string containing 0 or 1:"))

    for x in prompt:
        if x == "0" or x == "1":
            user_data+=x


    print("The current data length is "+ str(len(user_data))+", "+str((100-len(user_data)))+" symbols left")
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

balance = 1000
print("You have $1000. Every time the system successfully predicts your next press, you lose $1.\nOtherwise, you earn $1. Print \"enough\" to leave the game. Let's go!")

user_input=""
preprocessed =""
while len(preprocessed) < 4:
    user_input=str(input("\nPrint a random string containing 0 or 1:"))
    if user_input=="enough":
        print("Game over!")
        break
    else:
        for sign in user_input:
            if sign =="0" or sign=="1":
                preprocessed+=sign
        if len(preprocessed)<4:
            preprocessed=""
        else:
            max_poss=len(preprocessed)-3
            pred_count=0
            prediction=""

            sliced2 = [preprocessed[symbol:symbol+4] for symbol in range(0, len(preprocessed))]
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
            balance+=(max_poss-2*pred_count)
            print("predictions:\n"+prediction)
            print("\nComputer guessed "+str(pred_count)+" out of "+str(max_poss)+" symbols right ("+str(pred_count/max_poss*100)+" %)")
            print("Your balance is now $"+str(balance))

            preprocessed=""
