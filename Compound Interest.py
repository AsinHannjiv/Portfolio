#Write a code to ask for input of principal, interest rate, compounding times of year and term number of years
#convert into a float
fPv = float(input("Enter the starting principal: "))
fR = float(input("Enter the annual interest rate: "))
fr = float(fR/100)
fm = float(input("How many times per year is the interest compund? "))
ft = int(input("For how many years will the account earn interest? "))

#Calculate
fFV = fPv*(1+(fr/fm))**(fm*ft)

#print out the Future Value
print("At the end of", ft, "years you will have", "$ {:2,.2f}".format(fFV))