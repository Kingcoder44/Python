import random
print("Welcome to Number Guesssing Game ")
print("I'm guessing of a number between 1 and 100")
s=input("Choose a difficulty : Type e for  'easy' and h for 'hard' ")
n =random.randint(1,100)
print(n)
if s=='e':
    i=10
    print(f"You have {i} lives ")
    while i>0 :
        no=int(input("Guess a number"))
        if no == n:
            print("You have guessed it right")
            exit(0)
        elif no>n :
            print("Wrong Answer: Too High ")
            i-=1
            print(f"Try Again: You have {i} lives remaining")
            
        else :
            print("Wrong Answer: Too Low ")
            i-=1
            print(f"Try Again: You have {i} lives remaining")
    print("OOPS: You Loose")

elif s=='h':
    i=5
    print(f"You have {i} lives ")
    while i>0 :
        no=int(input("Guess a number"))
        if no == n:
            print("You have guessed it right")
            exit(0)
        elif no>n :
            print("Wrong Answer: Too High ")
            i-=1
            print(f"Try Again: You have {i} lives remaining")
            
        else :
            print("Wrong Answer: Too Low ")
            i-=1
            print(f"Try Again: You have {i} lives remaining")
    print("OOPS: You Loose")
else:
    print("Invalid Choice")