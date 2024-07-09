'''
Tax Information Network (TIN) is an initiative by Income Tax Department of India (ITD) for the modernization of the current system for collection, processing, monitoring and accounting of direct taxes using information technology. The network will check the eligible entities based on Permanent Account Numbers (PAN).PAN contains ten-digits in which first five characters are letters, next four numerals, last character is a letter and all characters in PAN number is always uppercase.If the PAN given by the user follow the above format then it is a Valid PAN Number other wise Invalid PAN Number.
write a program to validate the PAN number.
 
Input and Output Format:
Input is string of any length of any case.
Output is string ,should print “Valid PAN Number” without quotes if input fits the PAN rules otherwise “Invalid PAN Number” without quotes.
Refer sample input and output for formatting specifications.
Sample Input 1:
ABCDE1234F
Sample Output 1:
Valid PAN Number

Sample Input 2:
12345ABCD3
Sample Output 2:
Invalid PAN Number
'''
pan = input().upper()
if len(pan) == 10:
    if pan[0:5].isalpha() and pan[5:9].isdigit():
        if pan[9].isalpha():
            print("Valid PAN Number")
        else:
            print("Invalid PAN Number")
    else:
        print("Invalid PAN Number")
else:
    print("Invalid PAN Number")