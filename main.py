#guess the lucky number 
lucky_num = "7"
guess_num = ""
guess_limit = 10
guess_count = 0
out_of_guesses = False
while guess_num != lucky_num and not out_of_guesses:
  if guess_count < guess_limit:
    guess_num = input("Enter guess_num ")
    guess_count += 1
  else:
    out_of_guesses = True 
if out_of_guesses:
  print("Out of guesses, you lose!")
else:
  print("you win!")
