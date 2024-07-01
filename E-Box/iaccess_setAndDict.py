'''
The ICICI Bank are digitizing their KYC( Know Your Customer ) wing. The first step in their intiative is to parse a comma seperated string, which has user details.  Can you please automate this task of reading a comma seperated string and display the details of the user?
 
Address is given comma-separated in the following order.
(door-no,street,area,city,state,zipcode,country)
split the string and print it in the format shown in the Sample Output.
 
Input Format:
Input is a comma seperated string, details of the customer.
 
Output Format:
Refer to sample output for formatting specifications and more details.
 
Sample Input 1:
721,12th stage,Gokulam,Mysuru,Karnataka,570002,India
 
Sample Output 1:
Door-no:721
Street:12th stage
Area:Gokulam
City:Mysuru
State:Karnataka
Zipcode:570002
Country:India
'''
#solution
# s  =input()
# s = s.split(',')  
# print(f"Door-no: {s[0]}")
# print(f"Street: {s[1]}")
# print(f"Area: {s[2]}")
# print(f"City: {s[3]}")
# print(f"State: {s[4]}")
# print(f"Zipcode: {s[5]}")
# print(f"Country: {s[6]}")

'''
Input Formate Specifications:

The first line of input Contains Set1 integer.
The second line of Input Contains set2  Integer.
Output Format Specifications:

The first line of Output contains set1 is a subset of set2 (True /False ).
The second line of Output contains set2 is a subset of set1(True /False ).
The next line of Output contains  set1 is a superset of set2(True /False ).
The final line of Output contains set2 is a superset of set1(True /False ).
Sample input and output will be shown below.
'''
#solution
# s1 = set(map(int,input().split()))
# s2 = set(map(int,input().split()))
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))


