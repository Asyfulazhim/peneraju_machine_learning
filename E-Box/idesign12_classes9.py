class College:
    def __init__(self, college_id,college_name, city = None , state= None,pincode= None, contactNumber= None, emailId= None):
        self.college_id = college_id
        self.college_name = college_name
        self.city = city
        self.state = state
        self.pincode = pincode
        self.contactNumber = contactNumber
        self.emailId = emailId

    def print_address (self):
        return f"id : {self.college_id}\nName : {self.college_name}\nCity : {self.city}\nState : {self.state}\nPincode : {self.pincode}\n"

    def print_email (self):
        return f"Name : {self.college_name}\nContact Number : {self.contactNumber}\nEmail : {self.emailId}\n"


print("1. Enter College address and Display")
print("2. Enter  the contact details and Display")
print("3. exit")


n = -1
while n !=3:
    n = int(input("Enter your choice\n"))
    if n==1:
        college_id = input("Enter the College id\n")
        college_name = input("Enter the College name\n")
        city = input("Enter the City\n")
        state = input("Enter the State\n")
        pincode = input("Enter the Pincode")
        p1 = College(college_id,college_name, city , state,pincode)
        print(p1.print_address())
    
    elif n==2:
        college_name = input("Enter the name of the College\n")
        contactNumber = input("Enter the contact number\n")
        emailId = input("Enter the email id\n")
        p2 = College(None, college_name,None, None, None, contactNumber, emailId)
        print(p2.print_email())
    else:
        break
