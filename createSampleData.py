import os, random

brandFile = open("brand/brandData", 'w')
customerFile = open("customer/customerData", 'w')
brandDealerFile = open("branddealer/branddealerData", 'w')
dealerFile = open("dealer/dealerData", 'w')
saleFile = open("sale/saleData", 'w')
vehicleFile = open("vehicle/vehicleData", 'w')
maleName = open("dist.male.first.txt", "r")
femaleName = open("dist.female.first.txt", "r")
brands = open("brands.csv", "r")
modelFile = open("cars.txt", "r")
models = modelFile.read(250000)
maleList = maleName.readlines()
femaleList = femaleName.readlines()
brandList = brands.readlines()
brandNames = []
brandModel = {}
roadList = [" Rd", " St", " Blvd", " Ave", " Ln", " Dr"]
engineList = ["V8","V6","W","Inine","Electric","Diesel","Petrol"]
colorList = ["Dark Blue", "Red", "Beige", "White", "Black", "Grey", "Dark Grey", "Blue", "Green", "Orange", "Yellow", "Purple", "Pearl", "Dark Green", "Light Grey"]
transmission = ["Standard", "Automatic"]
customerList = []
customerList2 = []
for i in range(0, 1000):
    customerList.append(i)
    customerList2.append(i)

for customerNum in range(0, 1000):
    male = False
    currCustStr = ""
    currSQLCommand = "INSERT INTO CUSTOMER VALUES(" + str(customerNum + 1) + ", "
    if random.random() > 0.5:
        male = True
        currSQLCommand += maleList[random.randint(0,1000)].split()[0] + ", "
    else:
        currSQLCommand += femaleList[random.randint(0, 1000)].split()[0] + ", "
    currSQLCommand += str(random.randint(1,1000))
    currSQLCommand += ", " + maleList[random.randint(0,1000)].split()[0] + roadList[random.randint(0,5)] + ", "
    currSQLCommand += str(random.randint(10000,99999))
    currSQLCommand += ", " + str(random.randint(1000000000, 9999999999))
    if male:
        currSQLCommand += ", Male, "
    else:
        currSQLCommand += ", Female, "
    currSQLCommand += str(random.randint(0,200000)) + ")\n"
    customerFile.write(currSQLCommand)
customerFile.close()

makers = models.split("<carname>")
for brand in brandList:
    brandFile.write("INSERT INTO BRAND VALUES(" + brand[:len(brand) - 2] + ")\n")
    currBrand = brand.split(",")[0]
    brandNames.append(currBrand)
    brandModel[currBrand] = []
    for modelList in makers:
        if currBrand in modelList:
            models = modelList.split("<carmodel>")
            for model in models:
                brandModel[currBrand].append(model.split("</")[0])
            brandModel[currBrand].remove(currBrand)

brandFile.close()


for dealerNum in range(0, 25):
    currSQLCommand = "INSERT INTO DEALER VALUES(" + str(dealerNum + 1) + ", "
    if random.random() > 0.5:
        currSQLCommand += maleList[random.randint(0, 1000)].split()[0] + ", "
    else:
        currSQLCommand += femaleList[random.randint(0, 1000)].split()[0] + ", "
    currSQLCommand += str(random.randint(1000000000, 9999999999)) + ")\n"
    dealerFile.write(currSQLCommand)
dealerFile.close()

brandDealer = {}
for branddealerNum in range(0, 25):
    brandDealer[branddealerNum] = []
    for i in range(0,random.randint(1,5)):
        currBrand = brandNames[random.randint(0,24)]
        if not currBrand in brandDealer[branddealerNum]:
            brandDealer[branddealerNum].append(currBrand)
            currSQLCommand = "INSERT INTO BRANDDEALER VALUES(" + currBrand + ", " + str(branddealerNum + 1) + ")\n"
            brandDealerFile.write(currSQLCommand)
brandDealerFile.close()

saleNum = 1
for vehicleNum in range(0, 2000):
    currSQLCommand = "INSERT INTO VEHICLE VALUES(" + str(vehicleNum + 1) + ", "
    currSQLCommand += random.sample(engineList,1)[0] + ", " + random.sample(colorList, 1)[0] + ", " + random.sample(transmission, 1)[0] + ", "
    currBrand = random.sample(brandNames, 1)[0]
    currDealer = random.randint(0, 24)
    while currBrand not in brandDealer[currDealer]:
        currBrand = random.sample(brandNames, 1)[0]
    currModel = random.sample(brandModel[currBrand], 1)[0]
    currSQLCommand += currBrand + ", " + currModel + ", "
    if random.random() > 0.5:
        currSQLCommand += "0, "
    else:
        currSQLCommand += str(random.randint(1, 250000)) + ", "
    currSQLCommand += str(currDealer + 1) + ", "
    if random.random() < .75:
        saleCommand = "INSERT INTO SALE VALUES(" + str(saleNum) + ", "
        saleCommand += str(random.randint(500, 70000)) + ", " + str(currDealer + 1) + ", "
        currSQLCommand += str(saleNum) + ", "
        customer = ""
        if len(customerList) > 0:
            customer = str(customerList.pop(random.randint(0,len(customerList) - 1)) + 1)
        else:
            customer = str(customerList2.pop(random.randint(0, len(customerList2) - 1)) + 1)
        currSQLCommand += customer + ")\n"
        saleCommand += customer + ")\n"
        saleNum += 1
        saleFile.write(saleCommand)
    else:
        currSQLCommand += "null, null)\n"
    vehicleFile.write(currSQLCommand)
saleFile.close()
vehicleFile.close()
