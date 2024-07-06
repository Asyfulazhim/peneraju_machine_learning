bookingfile = "Driver.txt"
with open(bookingfile, "rt") as file:
    booking = file.read()
    file.close()

    booking = booking.replace("  ","")
    with open (bookingfile, "w")as file:
        file.write(booking)
        
    print(booking)
