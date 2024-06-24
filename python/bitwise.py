# how to represent binary numbers in python
# you can use 0b followed by the binary number
# how ever it is still an integer
# syahmi
# by adding 0b python starts reading it as one one one
# instead of one hundred and eleven
ownerpermission = 0b111
print(ownerpermission)

filepermission = 0b111101001 
# now owner can read, write and execute
# group can read and execute
# others can execute only

# in data science/machine learning when you were given
# categorical data you must convert them to numbers 
# which machine can understand
# this itself called "feature engineering"
# gender representation 01 for female or 10 for male
# race representation 1000 for malay and 0100 for chinese

# this bit extraction can be use using bitwise and operator
mask = 0b000111000
print((filepermission & mask) >> 3) # we manage to get group permission over the file

# in order to perform bit extraction we use bitwise & operator
# we are interested in 4, 5, 6 bits only
# Original Data             111101001   &
# Our Mask                  000111000
# 4,5,6 bits extracted      000101000
# shift it to right 3 times 000000101   >> 3
print(bin((filepermission & mask) >> 3))


# Original Data             111101001   |
# Our Mask                  000111000
# 4,5,6 bits extracted      111111001
# The or operator is used to set a specific bit to 1
# Please remember there is no way to set a specific bit to 0 using or operator
# Or operator is also used in extracting region of interest in a image
print(bin(filepermission | mask))

# Original Data             01001010   ^
# Our Mask                  00101100
# 4,5,6 bits extracted      01100110
# xor is used for encryption
message = 0b01001010 # my content "J"
key = 0b00101100 # encryption key ","
encrypted_message = message ^ key
print(bin(encrypted_message))

decrypted_message = encrypted_message ^ key
print(bin(decrypted_message))


# 1s complement
givennumber = 5
# 5                 0101
# 1s Compliment     1010
# 2s Compliment = 1s Compliment + 1
print(~givennumber + 1) # ~ 1s compliment
print(-givennumber)     # - unary negative
print(+givennumber)     # + unary positive

# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9,  A,  B,  C,  D,  E,  F, 10, 11, 12
# 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18
hexadecimalnumber = 0xF
print(hexadecimalnumber)
print(hex(hexadecimalnumber))

# 0, 1, 2, 3, 4, 5, 6, 7, 10, 11, 12, 13, 14, 15, 16, 17, 20
# 0, 1, 2, 3, 4, 5, 6, 7,  8,  9, 10, 11, 12, 13, 14, 15, 16
octalnumber = 0o10
print(octalnumber)
print(oct(octalnumber))