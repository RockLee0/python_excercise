#1. address, city ,country
street=input('enter street ')
city=input('enter city')
country=input('enter country')

address1= street+'\n'+city+'\n'+country
address2=f"{street} \n{city} \n{country}"

print(address1)
print(address2)

#2. slicing

fact="Earth revolves around the sun"
print(fact[slice(5,14)])
print(fact[-3:])
print(fact[5:14])

#3. fruits and vegitables
fruits=int(input())
vegi=int(input())

print(f"i eat {fruits} fruits and {vegi} vegitables")

#4. replace a certain part of a string

s = 'maine 200 banana khaye'
s=s.replace('200','10')
s=s.replace('banana','samosa')
print(s)
s=s.replace('200','10').replace('samosa','idli')
print(s)

