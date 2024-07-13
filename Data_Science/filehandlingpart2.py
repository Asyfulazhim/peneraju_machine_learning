import json

try: 
    with open('fruitsdictionary.json') as file:
        data = json.load(file)
    for product in data:
        print(product["product"])
        print(product["quantity"])
        print(product["price"])

except Exception as e:
    print("Something went wrong")
