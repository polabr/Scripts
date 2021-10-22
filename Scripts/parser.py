import re

with open("WR-SWITCH-MIB.txt") as f:
#    with open("out.txt", "w") as f1:
    for line in f:
        if "OBJECT-TYPE" in line:
            if "Counter32" in line:
                continue
#            print(line);
            my_string = line
#            print(my_string)
            splitString = my_string.split(' ')
            objectName = splitString[0]
#            print(objectName)
            
            splitObjectName = re.findall('[a-zA-Z][^A-Z]*', objectName) #uses regex!
            splitObjectName2 = re.findall('[A-Z][^A-Z]*', objectName) #without "wrs" part 
#            print('splitObjectName2 ',splitObjectName2)
            combine = ''.join(splitObjectName2)
#            print('combine ',combine)
            objectNameLower = combine.lower()
#            print("objectNameLower",objectNameLower)

#            print(splitObjectName)
#            print(splitObjectName[0])
            numWords = len(splitObjectName)
#            print("numWords: ",numWords)
            if "Integer" in f.readline():
                type = 'i'
        
#            print(type)
            print(f"record(longin, \"icarus_wrs_1/{objectNameLower}\")")
            print("{")
            if (numWords == 3): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[1]} {splitObjectName[2]}\") ")
            if (numWords == 4): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]}\") ")
            if (numWords == 5): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]}\") ")
            if (numWords == 6): #This includes the "wrs" out front as a word
                print(f"  field(DESC, \"WRS {splitObjectName[1]} {splitObjectName[2]} {splitObjectName[3]} {splitObjectName[4]} {splitObjectName[5]}\") ")
            print("  field(SCAN, \"10 second\")")
            print("  field(DTYP, \"Snmp\")")
            print(f"  field(INP, \"@icarus-wrs01 public %(P){objectName}.0 ( 100 {type}\")") #f-string in Py3! Pretty cool (% is deprecated)
            print("}")
            print("")

            
#            line2 = f.readline()
#            print(line2)
#            break
            #            f1.write(line)
B
