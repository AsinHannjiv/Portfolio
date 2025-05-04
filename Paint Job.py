#Make a function called getFloatInput to receive str as a parameter
#To be used as the prompt input
#Convert and return as float
#Validate data within function

def getFloatInput(Input):
    while True:
        try:
            validate = float(input(Input + ":"))
            if validate <= 0:
                print("Input a non-zero positive numeric value")
            else:
                return validate
        except ValueError:
            print("Input must be a positive numeric value")
            
#Inputs
fWallSpace = getFloatInput("Enter wall space in square feet")
fPaintPrice = getFloatInput("Enter Paint Price per gallon")
fFeet_GalPaint = getFloatInput("Enter feet per gallon")
fLaborHrs_Gal = getFloatInput("How many labor hours per gallon")
fLaborCharge_Hr = getFloatInput("Labor charge per hour")

sState = input("State job is in:")
sLast_Name = input("Customer Last Name:")

sFile = sLast_Name + "_PaintJobOutput.txt"
#Import math
import math

#Create Functions
#Function to hold logic
def main():
    #Code to output into a file
    sPaint_file = open(sFile, "w")
    
    iGallons = getGallonsOfPaint(fFeet_GalPaint, fWallSpace)
    
    fLaborHrs = getLaborHours(fLaborHrs_Gal, iGallons)
     
    fPaintCost = getPaintCost(iGallons, fPaintPrice)
   
    fLaborCost = getLaborCost(fLaborHrs, fLaborCharge_Hr)
       
    fSalesTax = getSalesTax(sState, fLaborCost, fPaintCost)
    
    fTotalCost = showCostEstimate(fPaintCost, fLaborCost, fSalesTax)
    
    sPaint_file.write(str(iGallons) + "\n")
    sPaint_file.write(str(fLaborHrs) + "\n")
    sPaint_file.write(str(fPaintCost) + "\n")
    sPaint_file.write(str(fLaborCost) + "\n")
    sPaint_file.write(str(fSalesTax) + "\n")
    sPaint_file.write(str(fTotalCost) + "\n")
    
    sPaint_file.close()
    print("File:", sFile, "was created.")
    
#Function to get the how many gallons is needed for the job rounded up and returns as a int
def getGallonsOfPaint(fFeet_Gal, fWallSq):
    iGalofPaint = math.ceil(fWallSq / fFeet_Gal)
    print("Gallons of paint:", iGalofPaint)
    return iGalofPaint

#Function to find hours of labor as float
def getLaborHours(fLaborHrs_GalIn, iGallonsIn):
    fLabor_Hr = float(fLaborHrs_GalIn * iGallonsIn)
    print("Hours of Labor:", fLabor_Hr)
    return fLabor_Hr

#Function that finds paint cost to paint wall and return it as float
def getPaintCost(iGallonsIn, fPaintPriceIn):
    fPaint_Cost = float(iGallonsIn * fPaintPriceIn)
    print("Paint cost:", "${:,.2f}".format(fPaint_Cost))
    return fPaint_Cost

#Function that finds labor cost and return it as float
def getLaborCost(fLaborHrsIn, fLaborCharge_HrIn):
    fLabor_Cost = float(fLaborHrsIn * fLaborCharge_HrIn)
    print("Labor charges:", "${:,.2f}".format(fLabor_Cost))
    return fLabor_Cost

#Function that find the tax rate for the input state
def getSalesTax(sStateIn, fLaborCostIn, fPaintCostIn):
    
    if sStateIn == "CT":
        sSales_Tax = 0.06
    elif sStateIn == "MA":
        sSales_Tax = 0.0625
    elif sStateIn == "ME":
        sSales_Tax = 0.085
    elif sStateIn == "NH":
        sSales_Tax = 0.0
    elif sStateIn == "RI":
        sSales_Tax = 0.07
    elif sStateIn == "VT":
        sSales_Tax = 0.06
    else:
        sSales_Tax = 0
    fTax = float((fLaborCostIn + fPaintCostIn)*sSales_Tax)
    print("Tax:", "${:,.2f}".format(fTax))
    return fTax
    
#Function to calculate and get the cost estimate
def showCostEstimate(fPaintCostIn, fLaborCostIn, fSalesTaxIn):
    fTotal_Cost = "${:,.2f}".format((fPaintCostIn + fLaborCostIn + fSalesTaxIn))
    print("Total cost:", fTotal_Cost)
    return fTotal_Cost

#Start Point
main() 