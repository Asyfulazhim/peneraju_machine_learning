bookingfile = "Car.txt"
with open(bookingfile, "rt") as file:
    booking = file.read()
    file.close()

    booking = booking.replace("Not Active","Inactive")
    with open (bookingfile, "w")as file:
        file.write(booking)
        
    print(booking)
