fDeposit = 0
fIRP = 0
iNum_Months = 0
fGoal = 0

#Inputs and validations
while fDeposit < 1:
    try:
        fDeposit = float(input("What is the Original Deposit (positive value):"))
        if fDeposit < 1:
            raise ValueError("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
    if fDeposit >= 1:
        break

while True:
    try:
        fIRP = float(input("What is the Interest Rate Percentage (positive value):"))
        if fIRP < 1:
            raise ValueError("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
    if fIRP >= 1:
        break

while True:
    try:
        iNum_Months = int(input("What is the Number of Months (positive value):"))
        if iNum_Months < 1:
            raise ValueError("Input must be a positive numeric value")
    except ValueError:
        print("Input must be a positive numeric value")
    if iNum_Months >= 1:
        break

while True:
    try:
        fGoal = float(input("What is the Goal amount (can enter 0 but not negative):"))
        if fGoal < 0:
            raise ValueError("Input must be 0 or greater")
    except ValueError:
        print("Input must be 0 or greater")
    if fGoal >= 0:
        break
    
#Convert Interest Percentage to decimal variable and divide it by 12
fMIR = fIRP/100/12
    
#Output the monthly interest for each month up to the amount of compounding months entered
fAcc_Bal = fDeposit

for x in range(1, iNum_Months +1):
    fInterest_Month = fAcc_Bal * fMIR
    fAcc_Bal += fInterest_Month
    print("Month:", "{:,}".format(x), "Account Balance is:", "${:,.2f}".format(fAcc_Bal))
    
#Find how long it would take to reach the goal amount
fAcc_Bal = fDeposit
imonths = 0
while fAcc_Bal <= fGoal:
    fInterest_Month = fAcc_Bal * fMIR
    fAcc_Bal += fInterest_Month
    imonths += 1

#format and output
print("It will take:", "{:,}".format(imonths), "months to reach the goal of", "${:,.2f}".format(fGoal))
    
    
    