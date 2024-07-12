'''

results = ["heads","tails","tails","heads","tails","heads","heads","tails","tails","tails"]
head=0
tail=0
for result in results:
    if result=="heads":
        head+=1
    else:
        tail+=1
print("heads= ",head)
print("tails= ",tail)

i=0
for i in range(0,11):
    if i%2==0:
        continue
    else:
        print(i*i)
        i=i+1
expense_list = [2340, 2500, 2100, 3100, 2980]
month_list = ["January", "February", "March", "April", "May"]

enter=int(input("enter the value"))
i=-1
for i in range(len(month_list)):
    if enter==expense_list[i]:
        print( f'your {enter} amount spent on {month_list[i]} month ')
        break
# not finished  yet. try later again

'''


length=int(input("enter the racing length \n"))

i=1
for i in range(length):
   tired=input("are you tired?")
   if tired=="yes":
       print("you didn't finish the race")
   elif tired=="no":
       ask=input('"are you tired" on every km?')
   elif i==length:
       print("congratulations")

print("\nExercise 5\n")

for i in range(1,6):
    s = ''
    for j in range(i):
        s += '*'
    print(s)