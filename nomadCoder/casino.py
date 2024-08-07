#노마드코더 방법
import random

pc=random.randint(1,50)
playing=True

while playing:
  user=int(input("Choose a number: "))
  if user==pc:
    print(f"Correct!! You won! Number is {pc}")
    playing=False
  elif user>pc:
    print("Too high! ")
  elif user<pc:
    print("Too low! " )
  





#이건 내가 푼 것
"""import random 

user_c=int(input("Choose number."))
pc_c=random.randint(1,50)

while user_c != pc_c:
  if user_c > pc_c:
    print("Lower! Computer chose",pc_c)
  elif user_c < pc_c:
    print("Higher! Computer chose",pc_c)
  user_c=int(input("Choose number."))
  print(f"You won!,{pc_c}")"""