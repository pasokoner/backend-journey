gallons_in_car = 8
miles_to_work = 105
miles_per_gallon = 22

# Don't touch above this line

gallons_needed = miles_to_work / miles_per_gallon

if gallons_in_car >= gallons_needed:
    print(
        f"You have {gallons_in_car:.2f} gallons and need {gallons_needed:.2f} gallons. You have enough gas to make it!"
    )
else:
    print(
        f"You have {gallons_in_car:.2f} gallons and need {gallons_needed:.2f} gallons. You need more gas!"
    )
