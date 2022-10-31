"""
Explanation:
- First, create dictionary containing counts of each character in the correct word
- For each attempt, check each character within user input for exact match;
    update response and decrement dict if so
- On second pass, check if dict key has value > 0; update response and decrement
    dict if so
- Stop prompting user input if attempts exceeds 6 or if all dict values <= 0

Pitfalls:
- By decrementing the dict in the case of a correct character at wrong position,
    we lose the ability to display yellow again. Try "STOOL" then "WASNT": the "T"
    in WASNT is no longer reflected as yellow
- Haven't implemented error handling for valid inputs
- Time complexity is high because we iterate through each guess twice
"""

attempt = 0
correct = "EARTH"
response = ["⬜"]*5
dict = {}

for i in range(5):
    if correct[i] in dict:
        dict[correct[i]] += 1
    else:
        dict[correct[i]] = 1

while attempt < 6:
    guess = input("Guess the word: ").upper()
    if guess == "1":
        break

    for i in range(5):
        if guess[i] == correct[i]:
            response[i] = "🟩"
            dict[guess[i]] -= 1
    
    for i in range(5):
        if guess[i] in dict:
            if(dict[guess[i]] > 0):
                response[i] = "🟨"
                dict[guess[i]] -= 1

    print("".join(response))
    if (all(value <= 0 for value in dict.values())):
        print("Correct!")
        break
    elif (attempt == 5):
        print("Out of attempts, correct word is:", correct)
    attempt += 1
    



