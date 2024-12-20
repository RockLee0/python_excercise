#purpose: if there are any error, immediately finding the error type is necessary.

try:
    raise OverflowError('operation size is too large')
except OverflowError as e:
    print(e)

# customize

class Beshi:
    pass

def withdraw(amount,balance):
    if amount>balance:
        raise Beshi('you dont have enough balance')
    return True

try:
    withdraw(100,50)
except Beshi as e:
    print(e)


