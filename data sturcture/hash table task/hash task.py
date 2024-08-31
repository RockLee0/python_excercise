arr=[]
with open('C:\\Users\\LENOVO\\PycharmProjects\\python_excercise\\data sturcture\\data\\nyc_weather.csv','r') as f:
    for line in f:
        tokens = line.strip().split(',')
        try:
         arr.append(int(tokens[1]))
        except:
            print('invalid data')
sum=0
i=0
for i in range(len(arr)):
    if i>6:
        break
    else:
        sum+=arr[i]
    i=i+1
print(sum/7)

i=1
big=arr[0]
for i in range(1,len(arr)):
    if arr[i]>big:
        big=arr[i]
print(big)

dict={}
with open('C:\\Users\\LENOVO\\PycharmProjects\\python_excercise\\data sturcture\\data\\nyc_weather.csv','r') as f_n:
    for line in f_n:
        tokens = line.strip().split(',')
        try:
         dict[tokens[0]]=int(tokens[1])
        except:
            print('invalid data')
print(dict)
print(dict['Jan 9'])
print(dict['Jan 10'])


arr=[]
with open('C:\\Users\\LENOVO\\PycharmProjects\\python_excercise\\data sturcture\\data\\poem.txt','r') as f_r:
    for line in f_r:
        tokens=line.strip().split(' ')
        for token in tokens:
            arr.append(token)


print(arr)
def hash(key):
    h=0
    l=len(arr)
    for char in key:
       h+=ord(char)
    return h%l



# not finished  yet

dict={}
for item in arr:
    print(item,':',hash(item))
    idx=hash(item)
    print(idx)