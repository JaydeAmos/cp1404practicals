TARIFF_11 = 0.244618
TARIFF_31 = 0.136928

print("Electricity Bill Estimator")
cents_per_hour = float(input("Enter cents per kWh: "))
daily_use_hourly = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
daily_cost = cents_per_hour * daily_use_hourly
bill_estimate = daily_cost * number_of_days
print("Estimated Bill ${:.2f}".format(bill_estimate))

print("Electricity Bill Estimator 2.0")
tariff = int(input("Which tariff? 11 or 31 "))
daily_use_hourly = float(input("Enter daily use in kWh: "))
number_of_days = int(input("Enter number of billing days: "))
if tariff == "11":
    daily_cost = TARIFF_11 * daily_use_hourly
    bill_estimate = daily_cost * number_of_days
    print("Estimated Bill ${:.2f}".format(bill_estimate))

elif tariff == "31":
    daily_cost = TARIFF_31 * daily_use_hourly
    bill_estimate = daily_cost * number_of_days
    print("Estimated Bill ${:.2f}".format(bill_estimate))
