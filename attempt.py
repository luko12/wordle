attempt = 0
correct = "EARTH"
# response = ""
response = ["⬜"]*5
dict = {}

while attempt <=5:
    guess = input("Guess the word: ").upper()
    if guess == "1":
        break
    
    for i in range(5):
        if correct[i] in dict:
            dict[correct[i]] += 1
        else:
            dict[correct[i]] = 1

    for i in range(5):
        print(i)
        if guess[i] == correct[i]:
            response[i] = "🟩"
            # response = response[:i] + "🟩" + [i+1:]
            dict[guess[i]] -= 1
    
    for i in range(5):
        print(i)
        if guess[i] in dict:
            if(dict[guess[i]] > 0):
                # response += "🟨"
                dict[guess[i]] -= 1
        # else: response += "⬜"
    attempt += 1
    print(response)



