import re

with open("WR-SWITCH-MIB.txt") as f:
#    with open("out.txt", "w") as f1:
    for line in f:
        if "OBJECT-TYPE" in line:
            if "Counter32" in line:
                continue
#            print(f.readline())
            #            if "Integer" in f.readline() or "INTEGER" in f.readline():
            my_string = line
#            print(my_string)
            splitString = my_string.split(' ')
#            print("splitString: ",splitString)
            objectName = splitString[0]
            if objectName=='':
                objectName = splitString[1]
            if objectName=='':
                objectName = splitString[4]

#            print("objectName:",objectName)
            
#            splitObjectName = re.findall('[a-zA-Z][^A-Z]*', objectName) #uses regex!
            splitObjectName = re.findall('[A-Z]+[^A-Z]*', objectName) #uses regex!
#            print("splitObjectName:",splitObjectName)
            splitObjectName2 = re.findall('[A-Z][^A-Z]*', objectName) #without "wrs" part 
            
            combine = ''.join(splitObjectName2)
            
            objectNameLower = combine.lower()
            #            print("objectNameLower",objectNameLower)
            
            #            print(splitObjectName)
            #            print(splitObjectName[0])
            numWords = len(splitObjectName)

            nextLine = f.readline()
#            print("nextLine: ",nextLine)
            
            type = 'i'
            # Add in these types later (mostly string-like)
            if "OCTET" in nextLine or "Display" in nextLine or "Wrs" in nextLine or "Address" in nextLine:
#                print("non-int type here!")
                continue
            
            #            if "Display" or "Wrs" or "OCTET" or "PhysAddress" in nextLine:
            #                continue
            
            #            print(type)
            print(f"record(longin, \"icarus_wrs_1/{objectNameLower}\")")
            print("{")
            if (numWords == 1): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]}\") ")
            if (numWords == 2): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]}\") ")
            if (numWords == 3): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]}\") ")
            if (numWords == 4): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]}\") ")
            if (numWords == 5): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]}\") ")
            if (numWords == 6): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]} {splitObjectName[5]}\") ")
            if (numWords == 7): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]} {splitObjectName[5]} {splitObjectName[6]}\") ")
            if (numWords == 8): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[0]} {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]} {splitObjectName[5]} {splitObjectName[6]} {splitObjectName[7]}\") ")
            print("  field(SCAN, \"10 second\")")
            print("  field(DTYP, \"Snmp\")")
            print(f"  field(INP, \"@icarus-wrs01 public %(P){objectName}.0 ( 100 {type}\")") #f-string in Py3! Pretty cool (% is deprecated)
            print("}")
            print("")



