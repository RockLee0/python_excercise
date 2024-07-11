#1.Area
length=92
width=48.8
print("area is ",length*width)

#2. changes amount
packetQuantity=int(input("How many packet you baought? \n ", ))
parPacketCost=int(input("par Packet Cost? \n ", ))
paid=int(input("How much you paid? \n ", ))
exchange=packetQuantity*parPacketCost-paid
print(exchange)

#3. cost of area
import math
side=5.5
area=pow(5.5,2)
costPerUnit=500
totalCost=area/costPerUnit
print(totalCost)


#4. bin of 17
print(bin(17))