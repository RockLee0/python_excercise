'''
f=open("C://py//write.txt","a") #appned on existing file:a , read on exixting file:r ,create and write:w
f.write("\n i like it but")
f.close()

'''

f=open("C://py/read.txt",'w')
f.write("teacher: who is the black ship? \n shakil: he is \n teacher: 'Who is he?' \n shakil: 'no fucking idea'")
f.close()

f_r=open("C://py/read.txt",'r') #also write as: with f_r=open("C://py/read.txt",'r') as f (then, f_r.close() won't be necessary to write)
for line in f_r:
    tokens=line.split(' ')
    print("wordcount:",len(tokens),line)
f_r.close()

with open("C://py/read.txt",'r') as fn:
    tokens=[]
    for line in fn:
        tokens.append( line.split(':'))
        print(tokens)

