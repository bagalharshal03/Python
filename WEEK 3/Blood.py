print("=== BLOOD DONATION ELIGIBLITY CHECK ===")

age = int(input("Enter your age: "))
weight = float(input("Enter your weight: "))

if age >= 18:
    print("Age requirement met. Proceeding to weight check...")

    if weight >= 50:
        print("Eligiblity Status: Eligible To Donate Blood!")

    else:
        print("Eligiblity Status: Rejected! Weight Must Be At Least 50kg!")

else:
    print("Eligiblity Status: Rejected! You Must Be 18 or Older To Donate Blood.")
