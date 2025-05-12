#Make a program to sales analyzer for real estate
#Function to validate and return inputs as a float
def getFloatInput(InputIn):
    while True:
        try:
            value = float(input(InputIn))
            if value > 0:
                return value
            else:
                print("Input a number greater than 0.")
        except ValueError:
            print("Please enter a positive numeric value.")

#Function to find median
def getMedian(fSalesIn):
    fSalesIn.sort()
    length = len(fSalesIn)
    if length % 2 == 1:
        return fSalesIn[length // 2]
    else:
        mid1 = fSalesIn[length // 2]
        mid2 = fSalesIn[length // 2 - 1]
        return (mid1 + mid2) / 2

#Main function
def main():
    fsales = []
    #Loop that repeats until user enter N to exit
    while True:
        fsales.append(getFloatInput("Enter property sales value: ")) 
        while True:
            choice = input("Enter another value (Y or N): ").lower()
            if choice in ["y", "n"]:
                break
            print("Please enter 'Y' or 'N'.")
        if choice == "n":
            break

    fsales.sort() #Sort the list from smallest to largest value
    
    #Output each entry in the sorted list
    for x, value in enumerate(fsales, start = 1):
        print("Property", x, "${:,.2f}".format(value))
    
    
    fmin_value = min(fsales) #Find minimum and output
    print("Minimum:", "${:,.2f}".format(fmin_value))
    fmax_value = max(fsales) #Find maximum and output
    print("Maximum:", "${:,.2f}".format(fmax_value))
    ftotal_value = sum(fsales) #Get the total value and output
    print("Total:", "${:,.2f}".format(ftotal_value))
    faverage_value = ftotal_value / len(fsales) #Calculate the avg value and output
    print("Average:", "${:,.2f}".format(faverage_value))
    fmedian_value = getMedian(fsales) #Get the median from the getMedian function and output
    print("Median:", "${:,.2f}".format(fmedian_value))
    fcommission_value = ftotal_value * 0.03 #Determine the commission and output
    print("Commission:", "${:,.2f}".format(fcommission_value))
    
#Call main
main()