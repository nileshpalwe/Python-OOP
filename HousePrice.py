# Enter your code here. Read input from STDIN. Print output to STDOUT
class HouseForSale:
    def __init__(self,houseNumber,houseType,salePrice,arealnSqft,isFurnished):
        self.houseNumber = houseNumber 
        self.houseType = houseType
        self.salePrice = salePrice
        self.arealnSqft = arealnSqft
        self.isFurnished = isFurnished
        
    def calculateNewPrice(self,new_rate):
        self.new_rate = new_rate
        salePrice = arealnSqft * new_rate
        if (isFurnished == "SEMI FURNISHED"):
            salePrice = 1.1 * salePrice
        elif (isFurnished == "FULLY FURNISHED"):
            salePrice = 1.2 * salePrice
        else:
            salePrice = salePrice
        
        return(salePrice)
    
class Realtor(HouseForSale):
    def __init__(self,realtorld,newRate,listOfHouseForSale):
        self.realtorld = realtorld
        self.newRate = newRate
        self.listOfHouseForSale = listOfHouseForSale
        
        
    def getAvailableHouses(self,saleprice,housetype):
        self.saleprice = saleprice
        self.housetype = housetype
        if ((saleprice >= salePrice)  and (housetype == houseType)):
            print(houseNumber + " " + houseType + " " + salePrice + " " + arealnSqft + " " + salePrice)
        else:
            print("Not in budget")
            
        
        
        
if __name__ == '__main__':
    count = int(input("Number of entries : "))
    for i in range(count):
        houseNumber = int(input("Enter house number (example : 101,102.. etc): "))
        houseType = input("enter house type (example: 1BHK, 2BHK, 3BHK) : ")
        salePrice = float(input("saleprice of house : "))
        arealnSqft = int(input("area of house : "))
        isFurnished = input("furnish type (example : SEMI FURNISHED, FULLY FURNISHED) : ")
    new_rate = float(input("New Rate (Rate per SqFt) : "))
    housetype = input("Type of house you want (example: !BHK, 2BHK, 3BHK) : ")
    saleprice = float(input("Enter ypur budget : "))
    hs = HouseForSale(houseNumber, houseType, salePrice, arealnSqft, isFurnished)
    cnp = HouseForSale.calculateNewPrice(HouseForSale,new_rate)
    get = Realtor.getAvailableHouses(hs,saleprice,housetype)  
    print(hs)
    print(cnp)
    print(get)
                
