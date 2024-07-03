from os.path import exists

def keyboardInput(datatype, caption, errorMessage):
    value = None
    isInvalid = True
    while(isInvalid):
        try:
            value = datatype(input(caption))
        except:
            print(errorMessage)
        else:
            isInvalid = False
    return value

filename = "fruits.txt"
# if exists(filename):
#     pass
# else:
#     open(filename, 'xt')
def createFile(filename):
    if not exists(filename):
        try:
            filehandler = open(filename, "xt")
        except Exception as e:
            print("Something went wrong when we try to create the file:", e)
        else:
            createTitle(filename)
        finally:
            # filehandler is an object/instance of file class
            # filehandler has many method like read, write and close
            filehandler.close()

# whenever you comeout with block the resource will be closed automatically
def createTitle(filename):
    try:
        with open(filename, 'wt') as filehandler:
            # here | (pipe) is used as delimiter
            # it will seperate the data
            # we can use deliiter to split the line into
            # multiple data
            filehandler.write("Product|Quantity|Price")
    except Exception as e:
            print("Something went wrong when we create the header:", e)

def addProduct(filename):
    try:
        product = keyboardInput(str, "Product:", "Product must be string")
        quantity = keyboardInput(int, "Quantity:", "Quantity must be integer")
        price = keyboardInput(float, "Price:", "Price must be float")
        with open(filename, "at") as filehandler:
            filehandler.write(f"\n{product}|{quantity}|{price}")
    except Exception as e:
        print("Something went wrong when we append the product:", e)


filename = "fruits.txt"
createFile(filename)
