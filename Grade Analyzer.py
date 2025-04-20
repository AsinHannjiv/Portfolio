#Make a program that allows for numeric entry of 4 test scores
#Will compute the test average and detemine a letter grade
#Also need to code logic to drop the lowest grade and average the other 3

#Get the name of the tester, their test scores and ask if they want to determine and drop the lowest grade

sName = input("Name of the person that we are calculating the grades for:")

iTest1 = int(input("Test 1:"))
iTest2 = int(input("Test 2:"))
iTest3 = int(input("Test 3:"))
iTest4 = int(input("Test 4:"))

sDrop_Grade = input("Do you wish to Drop the Lowest Grade Y or N?")

#Make sure the Test Grades are not negative values
if iTest1 < 0 or iTest2 < 0 or iTest3 < 0 or iTest4 < 0:
    print("Test scores must be greater than 0")
    raise SystemExit

#Can only Enter Y or N to continue code
if sDrop_Grade != "Y" and sDrop_Grade != "N":
    print("Enter Y or N to Drop the Lowest Grade.")
    raise SystemExit

#Deterrmine the lowest grade and drop it if asked for then find the avg of the remaining else find the avg of all four test grades
if sDrop_Grade == "Y":
    if iTest1 <= iTest2 and iTest1 <= iTest3 and iTest1 <= iTest4:
        sLowest_Grade = iTest1
        fAvg = float((iTest2 + iTest3 + iTest4)/3)
        print(sName, "test average is:", format(fAvg, ",.1f"))
    elif iTest2 <= iTest1 and iTest2 <= iTest3 and iTest2 <= iTest4:
        sLowest_Grade = iTest2
        fAvg = float((iTest1 + iTest3 + iTest4)/3)
        print(sName, "test average is:", format(fAvg, ",.1f"))
    elif iTest3 <= iTest1 and iTest3 <= iTest2 and iTest3 <= iTest4:
        sLowest_Grade = iTest3
        fAvg = float((iTest1 + iTest2 + iTest4)/3)
        print(sName, "test average is:", format(fAvg, ",.1f"))
    else:
        sLowest_Grade = iTest4
        fAvg = float((iTest1 + iTest2 + iTest3)/3)
        print(sName, "test average is:", format(fAvg, ",.1f"))
else:
    fAvg = float((iTest1 + iTest2 + iTest3 + iTest4)/4)
    print(sName, "test average is:", format(fAvg, ",.1f"))

#Find the test average's letter grade
if fAvg >= 97.0:
    print("Letter Grade for the test is: A+")
elif fAvg >= 94.0:
    print("Letter Grade for the test is: A")
elif fAvg >= 90.0:
    print("Letter Grade for the test is: A-")
elif fAvg >= 87.0:
    print("Letter Grade for the test is: B+")
elif fAvg >= 84.0:
    print("Letter Grade for the test is: B")
elif fAvg >= 80.0:
    print("Letter Grade for the test is: B-")
elif fAvg >= 77.0:
    print("Letter Grade for the test is: C+")
elif fAvg >= 74.0:
    print("Letter Grade for the test is: C")
elif fAvg >= 70.0:
    print("Letter Grade for the test is: C-")
elif fAvg >= 67.0:
    print("Letter Grade for the test is: D+")
elif fAvg >= 64.0:
    print("Letter Grade for the test is: D")
elif fAvg >= 60.0:
    print("Letter Grade for the test is: D-")
else:
    print("Letter Grade for the test is: F")
    
    
