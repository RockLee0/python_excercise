expense=[2200,2350,2600,2130,2190]


# 1. In Feb, how many dollars you spent extra compare to January?

spand=expense[1]-expense[0]
print(spand)

# 2. Find out your total expense in first quarter (first three months) of the year.

total=expense[0]+expense[1]+expense[2]

# 3. Find out if you spent exactly 2000 dollars in any month

for spend in expense:
    if(spend==2000):
        print("Yes, it is ",spend)
        break
    else:
        continue
print("there is no") 

# 4. June month just finished and your expense is 1980 dollar. Add this item to our monthly expense list

expense.append(1980)
print(expense)

'''
5. You returned an item that you bought in a month of April and
got a refund of 200$. Make a correction to your monthly expense list
based on this
'''
expense[3]=expense[3]-200
print(expense)


heros=['spider man','thor','hulk','iron man','captain america']
print(len(heros))
heros.append("black panther")
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