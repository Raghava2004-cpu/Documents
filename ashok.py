import random          #computer choose random number
def guess_number():
    numbers = range(1,10)
    x = random.choice(numbers)                   ###
    choice = input("Do you want to play with Computer(Yes/No) : ")
    choice = choice.lower()
    if choice == "no":
        print("Get Lost!")
    elif choice == "yes":
          n = int(input("Ok!then Enter a Number b/w 0-10: "))
          if n<0 or n>10:
              print(f"Number {n} not in the range")
              guess_number()
          elif n == x:
            print("You Won!")
            guess_number()
          else:
            print(f"You Lost! \nComputer choose {x}") 
            guess_number()
           
print("------------WELCOME TO PLAY------------")        
guess_number()                 
    