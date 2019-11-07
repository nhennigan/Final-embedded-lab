import time

num= 5
def count_up(num):
  i=0
  while i < num:
    print(i)
    i+=1
    time.sleep(1)

def count_down(num):
  while num > 0:
    print(num)
    num-=1
    time.sleep(1)

choice=input("count up or down?: ")
number=int(input("To/from what number? "))

if choice == "up":
  count_up(number)

if choice == "down":
  count_down(number)
