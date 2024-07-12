india = ["mumbai", "banglore", "chennai", "delhi"]
pakistan = ["lahore","karachi","islamabad"]
bangladesh = ["dhaka", "khulna", "rangpur"]

'''
Write a program that asks user to enter a city name and it should tell which country the city belongs to
'''
city=input("Enter the city name \n")

if city  in india:
        print('india')
elif city in pakistan:
        print('pakistan')
elif city in bangladesh:
        print('bangladesh')
'''
Write a program that asks user to enter two cities and it tells you if they both are in same country or not.
For example if I enter mumbai and chennai, it will print "Both cities are in India" but if I enter mumbai and
dhaka it should print "They don't belong to same country"
'''
city1=input("Enter the city name 1 \n")
city2=input("Enter the city name 2 \n")

if city1 and city2 in india:
    print('Both cities are in india')
if city1 and city2 in pakistan:
    print('Both cities are in pakistar')
if city1 and city2 in bangladesh:
    print('Both cities are in bangladesh')
else:
    print("They don't belong to same country")

'''
Write a python program that can tell you if your sugar is normal or not. Normal fasting level sugar range is 80
to 100.

Ask user to enter his fasting sugar level
If it is below 80 to 100 range then print that sugar is low
If it is above 100 then print that it is high otherwise print that it is normal
'''

level=int(input("what is your suger level? "))
if 80 <= level <= 100:
    print("NORMAL")
else: print("ABNORMAL")

levelFast=int(input("what is your fasting suger level? "))
if levelFast<80:
    print("suger is low")
elif levelFast>100 : print("suger is high")
else: print("it is normal")