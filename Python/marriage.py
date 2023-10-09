
import random 
print ("\n Hello. We are goini to make random couples 🤴👸 ")
Boys = ["Doruk" , "Omar" , "Bark" , "Sarp" , "Zolfaqar" , "Mart" , "Araz" , "Voral"]
Girls = ["Asie" , "Susan" , "Aybike" , "Leyla" ,"Malek" , "Gizam" , "Aylin" , "sevda"]
Couples = []

for i in range ( 8 ) :
    boy = random.randint (0 , len(Boys) - 1)
    girl = random.randint (0 , len(Girls) - 1)

    couple = f"({Boys[boy]} , {Girls[girl]})"
    Couples.append (couple)

    Boys.remove ( Boys[boy] )
    Girls.remove ( Girls[girl] )

print (" Random couples are :")
for i in Couples :
    print (i)