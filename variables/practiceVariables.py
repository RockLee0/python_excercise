#1. variable
'''break = 5
print(break)
#SyntaxError: invalid syntax. reason: there are inbuilt keyword which you can't use as a variable.
'''

#2. find out the age
birth=int(input("enter the birth year \n",))
current=int(input("enter this year \n",))
print("Your age is: ", current-birth)


#3. full name (concate)

firstName=input("What is your first name? \n",)
middleName=input("What is your second name? \n",)
lastName=input("What is your last name? \n",)

fullName=firstName+' '+middleName+' '+lastName;
print("Your full name is ",fullName)


#4. check variable
'''
_nation=1 (no prob)
1record=2 (can't start with number)
record1=3 (ok)
record_one=4 (ok)
record-one=5 (symbol)
record^one=6 (can't be a symbol)
continue=7 (keyword problem)
'''
