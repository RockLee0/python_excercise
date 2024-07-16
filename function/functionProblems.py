'''
def area(base,height):
    return (1/2)*base*height


def area2(base,height,shape="trangle"):
    if shape=="triangle":
        area=(1/2)*base*height
    elif shape=="rectangle":
        area=height*base
    return area

'''
'''
def print_pattern(n=5):
    for i in range(n):
        s = ''
        for j in range(i+1):
            s = s + '*'
        print(s)


print_pattern(5)

'''


for i in range(5):
    s = ''
    for j in range(i+1):
        s= s+ '*'
    print(s)



