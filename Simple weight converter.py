weight=int(input("weight:"))
unit=input("lbs or kg")
if unit.upper() == "LBS":
    converted = weight* 0.45
    print(f"Your weight is {converted} kilos")
else:
    converted = weight // 0.45
    print(f"Your weight is {converted} pounds")