select_word = "smsm"
guess = ""
guess_count = 0
guess_limit = 3
no = False

while guess != select_word and not no:
    if guess_count < guess_limit:
        guess = input("enter guess ")
        guess_count += 1
    else:
        no = True

if no:
    print(" You Lose")
else:
    print("You Win")    