import random
import struct

def generate_numbers(N, M):
    numbers = []
    current_number = random.randint(0, 255)
    numbers.append(current_number)

    for _ in range(N - 1):
        delta = random.randint(-M, M)
        next_number = max(0, min(255, current_number + delta))
        numbers.append(next_number)
        current_number = next_number

    return numbers

# Testi
N = 500
M = 30
test_data = generate_numbers(N, M)
#test_data = [55, 53, 53, 53, 53, 53, 10, 10, 11, 11, 11, 11]
print(f"Generirani podatki: {test_data}")

# Shranjevanje podatkov
with open('test_data.bin', 'wb') as file:
    for number in test_data:
        file.write(struct.pack('B', number))  # 'B' je format za unsigned char (0..255)

# Branje podatkov
with open('test_data.bin', 'rb') as file:
    data = file.read()
    unpacked_data = [struct.unpack('B', bytes([byte]))[0] for byte in data]
    print(int(bin(unpacked_data[0])[2:]))
    ##print(f"Prebrani podatki: {unpacked_data}")


prev_number = 0
ponovitev = 0
first = True
razlika = 0
binNum = ""
fulBin = bin(unpacked_data[0])[2:].zfill(8)
fulBin += " "
for x in unpacked_data:
    print(f"num: {x}")
    binNum = ""
    if x != prev_number and first == False:
        if(ponovitev > 0):
            fulBin += " |01 "
            fulBin += bin(ponovitev-1)[2:].zfill(3)
            print(f"Ponovitev {ponovitev}")
            print(f"01 {bin(ponovitev-1)[2:].zfill(3)}")
            fulBin += " "
        ponovitev = 0
        razlika = x - prev_number
        print(f"Razlika: {razlika}")
        binNum = "|00 "
        if(abs(razlika) < 3):
            print(f"Kodiranje razlike")
            binNum += "00 "
            if(razlika > 0):
                binNum += bin(razlika+1)[2:].zfill(2)
            else:
                binNum += bin(razlika+2)[2:].zfill(2)
        elif(abs(razlika) < 7):
            print(f"Kodiranje razlike")
            binNum += "01 "
            if(razlika > 0):
                binNum += bin(razlika+1)[2:].zfill(3)
            else:
                binNum += bin(razlika + 6)[2:].zfill(3)
        elif(abs(razlika) < 15):
            print(f"Kodiranje razlike")
            binNum += "10 "
            if(razlika > 0):
                binNum += bin(razlika + 1)[2:].zfill(4)
            else:
                binNum += bin(razlika + 14)[2:].zfill(4)
        elif(abs(razlika) < 31):
            print(f"Kodiranje razlike")
            binNum += "11 "
            if(razlika > 0):
                binNum += bin(razlika + 1)[2:].zfill(5)
            else:
                binNum += bin(razlika + 30)[2:].zfill(5)
        else:
            print(f"Absolutno kodiranje")
            binNum = "|10 "
            if(razlika < 0):
                binNum += "1"
            else:
                binNum += "0"
            binNum += bin(abs(razlika))[2:].zfill(8)
        #fulBin += "   "
            
    elif(not first and x == prev_number):
        ponovitev += 1
        if(ponovitev > 7):
            fulBin += " |01 "
            fulBin += bin(ponovitev-1)[2:].zfill(3)
            print(f"Ponovitev {ponovitev}")
            print(f"01 {bin(ponovitev-1)[2:].zfill(3)}")
            fulBin += " "
            ponovitev = 0
        print(f"Ponovitev: {ponovitev}")
        #binNum += "01 "
    
    print(binNum)
    fulBin += binNum
    
    print("\n")
    prev_number = x
    first = False

if(ponovitev > 0):
    fulBin += " |01 "
    fulBin += bin(ponovitev-1)[2:].zfill(3)
    print(f"Ponovitev {ponovitev}")
    print(f"01 {bin(ponovitev-1)[2:].zfill(3)}")

fulBin += " 11"
print("Full Code")
print(fulBin)

fulBin = fulBin.replace(' ', '')
fulBin = fulBin.replace('|', '')

print(fulBin)
    

with open("output.txt", "w") as file:
    file.write(fulBin)

file.close

print(unpacked_data)
