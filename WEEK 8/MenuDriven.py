print("--- OLA Ride Booking ---")

print("1. Bike")
print("2. Car")
print("3. Auto")

vehicle = int(input("Select Vehicle: "))
pickup = input("Enter Pickup Location: ")
drop = input("Enter Drop Location: ")
distance = int(input("Enter Distance (KM): "))

if vehicle == 1:
    vname = "Bike"
    fare = distance * 50

elif vehicle == 2:
    vname = "Car"
    fare = distance * 80

elif vehicle == 3:
    vname = "Auto"
    fare = distance * 150

else:
    print("Invalid Vehicle")
    

print("Total cost = Rs.", fare)

print("----- Online Payment -----")
print("1. Google Pay")
print("2. PhonePe")
print("3. Paytm")
print("4. Cash")

pay = int(input("Choose Payment Option: "))

if pay == 1:
    payment = "Google Pay"
elif pay == 2:
    payment = "PhonePe"
elif pay == 3:
    payment = "Paytm"
elif pay == 4:
    payment = "Cash"
else:
    print("Invalid Payment Option")
    

print("Enter Payment Details")
payer = input("Enter Name: ")
mobile = input("Enter Mobile Number: ")
pin = input("Enter your pin")

print("Payment Successful!")
print("Paid Through :", payment)
print("Customer Name :", payer)
print("Mobile Number :", mobile)
print("Amount Paid : Rs.", fare)


print("===== BOOKING CONFIRME =====")
print("Platform  : RAPIDO")
print("Customer  :", payer)
print("Mobile    :", mobile)
print("Vehicle   :", vname)
print("Pickup    :", pickup)
print("Drop      :", drop)
print("Distance  :", distance, "KM")
print("Cost      :", fare)
print("Payment   :", payment)
print("Status    : Ride Booked Successfully")