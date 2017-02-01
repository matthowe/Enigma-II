#engima II
#https://www.youtube.com/watch?v=hiOjqskDlS0


def createWheel():
    """This creates the three cypher wheels"""
    
    five = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
    six = ['A','C','E','D','F','H','G','I','K','J','L','N','M','O','Q','P','R','T','S','U','W','V','X','Z','Y','B']
    seven = five[::-1] #revserses wheel five
    return (five,six,seven)

def wheelOrderSetup():
    wheels = ['5','6','7']
    print('first wheel:', wheels)              
    wheelOrderQuestion1 = input()
    wheels.remove(wheelOrderQuestion1)
    print('second wheel:', wheels)   
    wheelOrderQuestion2 = input()
    wheels.remove(wheelOrderQuestion2)
    wheelOrder = [wheelOrderQuestion1, wheelOrderQuestion2] + wheels
    print(wheelOrder)
    return(wheelOrder)



def setupWheels(wheelOrder,five,six,seven):
    wheels = []
    for i in range(len(wheelOrder)):
        #print (wheelOrder[i])
        if (wheelOrder[i]) == '5':
            wheels.append(five)
            #print('adding five')
        elif (wheelOrder[i]) == '6':
            wheels.append(six)
            #print('adding six')
        else:
            wheels.append(seven)
            #print('adding seven')

    return(wheels)


def keyWord(wheels):
    keyWord = input('What is the three letter keyword in capitals: ')
    wheelPointers = []
    for i in range(len(keyWord)):
        #print(keyWord[i])
        print(wheels[i].index(keyWord[i]))
        wheelPointers.append(wheels[i].index(keyWord[i]))
    
        
    return(wheelPointers)

#26

#wheel 3 adds 1 each turn to wheel 2
#wheel 2 takes 1 each turn from wheel 1

#3rd wheel is your input
#wheel 1 is first output
#wheel 2 is the second output


def turnWheels(wheelPointers):
    if (wheelPointers[0]) == 0:
        wheelPointers[0]= 25
    else:
        wheelPointers[0] = wheelPointers[0]-1
    #print('-1 to wheel 0', wheelPointers[0], wheels[0][wheelPointers[0]])
    
    if (wheelPointers[1]) == 25:
        wheelPointers[1]= 0
    else:
        wheelPointers[1] = wheelPointers[1]+1
    #print('-1 to wheel 1', wheelPointers[1], wheels[1][wheelPointers[1]])
    
    
    if (wheelPointers[2]) == 0:
        wheelPointers[2]= 25
    else:
        wheelPointers[2] = wheelPointers[2]-1
    #print('-1 to wheel 2', wheelPointers[2], wheels[2][wheelPointers[2]])


def encryption(wheels,wheelPointers):
    encryptWord = input('Type word you wish to encrypt in capitals')
    outputWheel = 1
    for i in range(len(encryptWord)):
        #print('looking for letter ',encryptWord[i])
        #a = encryptWord[i]
        #b = wheels[2][2]
        #inputWheelPosition = wheelPointers[2]
        #print(inputWheelPosition)
        #theWheelPosition = wheels[2][inputWheelPosition]     
        while encryptWord[i] != wheels[2][wheelPointers[2]]:
            # turn wheels from the setup keyWord positions so third wheel is on index
            print ('starting')
            newWheelPointers = turnWheels(wheelPointers)
            print (newWheelPointers)
            wheelPointers = newWheelPointers                                               
            
 
        #print('output wheel : ',outputWheel, 'wheel pointer', wheelPointers[outputWheel], 'letter', wheels[outputWheel][wheelPointers[outputWheel]])
      
        if outputWheel == 0:
            outputWheel = 1
            print(wheels[outputWheel][wheelPointers[outputWheel]],end='')
        else:
            outputWheel = 0
            print(wheels[outputWheel][wheelPointers[outputWheel]],end='')
            
            
#---------------------------------------------------------------------------------------------------------------------------------------------------------
def decryption(wheels,wheelPointers):
    decryptWord = input('Type word you wish to decrypt in capitals')
    inputWheel = 0
    for i in range(len(decryptWord)):
        #print('looking for letter ',decryptWord[i])
        #a = encryptWord[i]
        #b = wheels[2][2]
        #inputWheelPosition = wheelPointers[2]
        #print(inputWheelPosition)
        #theWheelPosition = wheels[2][inputWheelPosition]
        while decryptWord[i] != wheels[inputWheel][wheelPointers[inputWheel]]:
            # turn wheels from the setup keyWord positions so third wheel is on index

            newWheelPointers = turnWheels(wheelPointers)
            wheelPointers = newWheelPointers
    
   
        #print('output wheel : ',outputWheel, 'wheel pointer', wheelPointers[outputWheel], 'letter', wheels[outputWheel][wheelPointers[outputWheel]])
      
        print(wheels[2][wheelPointers[2]],end='')
        
        if inputWheel == 0:
            inputWheel = 1
       
        else:
            inputWheel = 0
           
def run():
    five, six, seven = createWheel()
    wheelOrder = wheelOrderSetup()
    wheels=setupWheels(wheelOrder,five,six,seven)
    wheelPointers=keyWord(wheels)
    choice = input('(e)ncrypt or (d)ecrypt?')
    if choice == 'e':
        encryption(wheels, wheelPointers)
    else:
        decryption(wheels, wheelPointers)
    print()
    
    

while True:
    print('---------')
    print('Run Again')
    run()






