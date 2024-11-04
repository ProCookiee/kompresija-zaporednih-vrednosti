fulBin = ""
index = 8
nacin = ""

binBit = ""
binRazlika = ""
decRazlika = 0

binPonovitev = ""
decPonovitev = 0

binAbs = ""
decAbs = 0

prevNum = 0
numArray = []
f = open("output.txt", "r")
for line in f:
    fulBin += line
    
#print(fulBin)
prevNum = int(fulBin[0:8], 2)
numArray.append(prevNum)
#print(prevNum)

while(nacin != "11"):
    nacin = fulBin[index:index+2]
    #print(f"-------------------\n Nacin: {nacin}")
    if(nacin == "00"):
        binBit = fulBin[index+2:index+4]
        if(binBit == "00"):
            binRazlika = fulBin[index+4:index+6]
            if(binRazlika[0] == '0'):
                decRazlika = int(binRazlika, 2) - 2
            else:
                decRazlika = int(binRazlika, 2) - 1
            index += 6
        elif(binBit == "01"):
            binRazlika = fulBin[index+4:index+7]
            if(binRazlika[0] == '0'):
                decRazlika = int(binRazlika,2) - 6
            else:
                decRazlika = int(binRazlika, 2) - 1
            index += 7
        elif(binBit == "10"):
            binRazlika = fulBin[index+4:index+8]
            if(binRazlika[0] == '0'):
                decRazlika = int(binRazlika,2) - 14
            else:
                decRazlika = int(binRazlika, 2) - 1
            index += 8
        elif(binBit == "11"):
            binRazlika = fulBin[index+4:index+9]
            if(binRazlika[0] == '0'):
                decRazlika = int(binRazlika,2) - 30
            else:
                decRazlika = int(binRazlika, 2) - 1
            index += 9
        numArray.append(prevNum + decRazlika)
    elif(nacin == "01"):
        binPonovitev = fulBin[index+2:index+5]
        decPonovitev = int(binPonovitev, 2)
        for i in range (decPonovitev+1):
            numArray.append(prevNum)
        index+= 5
    elif(nacin == "10"):
        binAbs = fulBin[index+3: index+11]
        decAbs = int(binAbs, 2)
        #print(f"testni {fulBin[index+2]}")
        if(fulBin[index+2] == '1'):
            decAbs *= -1
        numArray.append(prevNum + decAbs)
        index+= 11
    prevNum = numArray[-1]        
    # print(f"BinBit: {binBit}")
    # print(f"BinRazlika: {binRazlika}")
    # print(f"DecRazlika: {decRazlika}")

    # print(f"BinPonovitev: {binPonovitev}")
    # print(f"DecPonovitev: {decPonovitev}")

    # print(f"BinAbs: {binAbs}")
    # print(f"DecAbs: {decAbs}")
    
    # print(f"Number: {prevNum}")

print(f"NumArray: {numArray}")