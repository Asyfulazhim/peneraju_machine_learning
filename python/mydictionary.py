# JavaScript Object Notation (JSON)

foreigner = {
    "firtsname": "Peter", 
    "lastname" : "Parker",
    "passportnumber" : "E492389",
    "incometaxnumber" : "SG834934",
    "pcbamount": 892,
    "lastmonth" : 5,
    "lastyear" : 2024,
    "previousmonth" : [(4,2024,891),(3,2024,895),(2,2024,893),(1,2024,982)],
    "addresses": {
        "office":{
            "street": "Wall Street",
            "city": "New York",
        },
        "home": {
            "street": "Main Street",
            "city": "Los Angeles",
        }
    }
    
}

print("First Name:", foreigner["firtsname"])
print("Last Name:", foreigner["lastname"])
print("Passport Number:", foreigner["passportnumber"])
print("Income Tax Number:", foreigner["incometaxnumber"])
print("PCB Amount:", foreigner["pcbamount"])
print("Last Month:", foreigner["lastmonth"])
print("Last Year:", foreigner["lastyear"])

for month, year, amount in foreigner["previousmonth"]:
    print(f"Transaction: {month}-{year} RM{amount}")

officeAddress = foreigner["addresses"]["office"]
print("Office Address: ", officeAddress["street"], officeAddress["city"])
print("=" * 100)
homeAddress = foreigner["addresses"]["home"]
print("Home Address: ", homeAddress["street"], homeAddress["city"])
print("=" * 100)
# or can access directly as follow
print("Office Address: ", foreigner["addresses"]["office"]["street"], foreigner["addresses"]["office"]["street"])
print("Home Address: ", foreigner["addresses"]["home"]["street"], foreigner["addresses"]["home"]["street"])
print("=" * 100)
#isintance is built in function to determine the type of variable

print(foreigner.keys())
for key in foreigner.keys():
    if(isinstance(foreigner[key],list)):
        for item in foreigner[key]:
            print(item)
    else:
        print(foreigner[key])
print("=" * 100)
#use method item
for key, value in foreigner.items():
    if(isinstance(value,dict)):
        for k, v in value.items():
            print(f"{k}: {v}")
print("=" * 100)
# add key and item in dictionary name salary
foreigner["salary"] = 5000
print(foreigner)

print("=" * 100)
#delete item from dict using pop
foreigner.pop("pcbamount")
print(foreigner)


