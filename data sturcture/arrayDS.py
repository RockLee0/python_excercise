#In Feb, how many dollars you spent extra compare to January?
expenses =[['january',2200],['February',2350],['March',2600],['April', 2130],['May', 2900]]

if expenses[1][1]>expenses[0][1]:
    extra=expenses[1][1]-expenses[0][1]
    print('extra amount is: ',extra)
else:
    print('not bigger than january')

#Find out your total expense in first quarter (first three months) of the year.

total=0
count=0
for expense in expenses:
    total+=expense[1]
    count+=1
    if count>2:
        print('total expense in first quarter',total)
        break


#Find out if you spent exactly 2000 dollars in any month
count=0
for expense in expenses:
    count += 1
    if expense[1]==2000:
        print("yes, the month is",expense[0])
    elif  count==len(expenses):
        print('Nai')

#June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list
expenses.append(['june',1980])
print(expenses)

'''
You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''

for expense in expenses:
    if expense[0]=='April':
        expense[1] = expense[1]-200
        print(expenses)
        break

heros=['spider man','thor','hulk','iron man','captain america']

print(len(heros))
heros.append('black panther')
print(heros)
heros.pop()  #remove,del also can be used
heros.insert(3,"black panther")  #to add there is also extent()
print(heros)
heros.remove("thor")  #heros[1:3]=['doctor strange']
heros.remove("hulk")
heros.insert(1,"doctor strang")
print(heros)
heros.sort()
print(heros)



#Create a list of all odd numbers between 1 and a max number. Max number is something you need to take from a user using input() function

maxNumber=int(input('enter your max \n'))
i=1
values=[]
for i in range(i,maxNumber):
    if i%2 !=0:
        values.append(i)
    i+=1
    if i==maxNumber:
        print(values)



