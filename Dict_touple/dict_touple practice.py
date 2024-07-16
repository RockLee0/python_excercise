dict={'China':143,'India':136,'USA':32,'Pakistan':21}

x=input('enter \n')

def print_all():
    for i in dict:
        print(i, '==>', dict[i])

if x=='print':
        print_all()

if x=='add':
    c=input('enter country name \n')
    if c in dict:
        print('it exist')
    else:
        moreInput=input('enter  population of the name  \n')
        dict[c]= moreInput
        print_all()

if x=='remove':
    country=input('enter the country to be removed \n ')
    if country in dict:
        dict.pop(country)
        print_all()
    else:
        print("country doesn't exist!")

if x=='query':
    c=input('enter country name \n')
    if c in dict:
        print(dict[c])



## further work: funtionalize all inputs, lower case the inputs and lower case the dict