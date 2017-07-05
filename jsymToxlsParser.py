
def getPf(lineList):
    pf=lineList[1]
    pf= pf[6:8]
    return pf

def getPs(lineList):
    ps=lineList[2]
    ps=ps[6:8]
    return ps

def getSa(lineList):
    sa=lineList[3]
    if sa[0:2]=="sa":
        sa =sa[4:8]
        return sa
    else:
        return ""
    

def getPgLabel(lineList):
    i =0
    label =lineList[3]
    if label[0:2]=="sa":
        label = lineList[4]
        label = label[7:len(label)]
        while i != (len(lineList)-5):
            i+=1
            label=label+" "+lineList[4+i]
        label = label[:-2]
        
        return label
    else:
        label = label[7:len(label)]
        while i != (len(lineList)-4):
            i+=1
            label=label+" "+lineList[3+i]
        label = label[:-2]
        return label

def getByte(lineList):
    byte=lineList[1]
    byte =byte[-2:-1]
    return byte

def getBit(lineList):
    bit = lineList[2]
    bit =bit[-2:-1]
    return bit

def getLength(lineList):

    if lineList[3][9].isdigit():
        length= lineList[3]
        length=length[8:10]
        return length
    else:
        return lineList[3][8]

def getSelectfieldLabel(lineList):
    fieldLabel= lineList[4]
    i=0
    fieldLabel = fieldLabel[7:len(fieldLabel)]
    while i != (len(lineList)-5):
        i+=1
        fieldLabel=fieldLabel+" "+lineList[4+i]
    fieldLabel = fieldLabel[:-2]
    return fieldLabel

def getTextfieldLabel(lineList):
    textfieldLabel=lineList[5]
    textfieldLabel = textfieldLabel[7:-2]
    return textfieldLabel
    

def getBase(lineList):
    base =lineList[1]
    base= base[6:-1]
    return base

def getTextFieldType(lineList):
    textFieldType=lineList[4]
    textFieldType=textFieldType[6:-1]
    return textFieldType
    
    
        



inTag = False

fileHandle=open('file004.txt','r')
print("PGN    SA    PGN Name  Data length      Parameter name         Start positoin   Bit length      base")
for line in fileHandle:
    lineList= line.split()
    if lineList[0] == "<pg":
        inTag=True
        pf =getPf(lineList)
        ps=getPs(lineList)
        sa=getSa(lineList)
        dataLength="8"
        pgLabel=getPgLabel(lineList)
        
    elif lineList[0] =="<selectfield":
        byte=getByte(lineList)
        bit=getBit(lineList)
        length=getLength(lineList)
        fieldLabel=getSelectfieldLabel(lineList)
        
        if inTag:
            
            print("0x"+pf+ps+" "+sa+"  "+pgLabel+"     "+"8"+"       "+fieldLabel, end='')
            print(byte.rjust(70-len("0x"+pf+ps+" "+sa+"  "+pgLabel+"     "+"8"+"       "+fieldLabel))+"."+bit+"          "+length+"  ", end='         ')

            
            
    elif  lineList[0] =="<textfield":
        byte=getByte(lineList)
        bit=getBit(lineList)
        length=getLength(lineList)
        textFieldType=getTextFieldType(lineList)
        textfieldLabel=getTextfieldLabel(lineList)
        
        print("0x"+pf+ps+" "+sa+"  "+pgLabel+"       "+"8"+"       "+textfieldLabel, end='')
        print(byte.rjust(70-len("0x"+pf+ps+" "+sa+"  "+pgLabel+"       "+"8"+"       "+textfieldLabel))+"."+bit+"          "+length+"           "+textFieldType)

    elif lineList[0]=="<select" and inTag:
        if inTag:
            base=getBase(lineList)
            print(base)
            

    elif lineList[0]=="</pg>":
        inTag=False
        print()
        print()
        print()

    
        
    
    
        
    
    
    
    ##print(i.strip("\n"))
    
fileHandle.close()
    


    
