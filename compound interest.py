
import matplotlib.pyplot as plt
import csv as csv
from datetime import datetime
import json


# Lists to hold years and amounts
years = []
amounts_v = []
amounts_si_v = []
amounts = []
amounts_si = []
rates = []

# Input values
P = int(input("Enter the principal amount: "))
P_CI = P
cum_interest = 0
T = int(input("Enter time in years: "))
multiple_rates = T

if multiple_rates > 1:
    for y in range(multiple_rates):
        r = float(input(f"Enter rate for year : "))
        rates.append(r)

Rt = float(input("Enter the fixed rate: "))
n = int(input("Enter number of times interest is compounded per year: "))

# Simple and Compound Interest Calculation
for year in range(T):
    years.append(year+1)

    # Use rate for that year
    if multiple_rates > 1:
        rate = rates[year]
        # Simple Interest
        cum_interest += (P * rate / 100)
        si_amount_v = P + cum_interest
        amounts_si_v.append(si_amount_v)
  

        # Compound Interest
        ci_amount_v = P_CI * (1 + (rate / (100 * n))) ** (n)
        amounts_v.append(ci_amount_v)
        P_CI = ci_amount_v
    else:
        print("Error")
        break
    rate = Rt
    # Simple Interest
    si_amount = P + (P * rate * (year+1) / 100)
    amounts_si.append(si_amount)

    # Compound Interest
    ci_amount = P * (1 + (rate / (100 * n))) ** (n * (year+1))
    amounts.append(ci_amount)
save_grph = input("Do you want to save the graph? (y/n): ")
save_data = input("Do you want to save the data? (y/n): ")
if save_data.lower() == "y":
    with open(f"interest_results_{now}", mode="w", newline='') as file:
        writer = csv.writer(file)
        # Write the header row
        writer.writerow(["Year", "Fixed Compound", "Varying Compound", "Fixed Simple", "Varying Simple"])
        # Write data rows
        for i in range(T):
            writer.writerow([
                years[i],  
                round(amounts[i], 2),
                round(amounts_v[i], 2),
                round(amounts_si[i], 2),
                round(amounts_si_v[i], 2)
            ])
    # Print success message once after the file is written
    print(f"Successfully saved the data as interest_results{now}")
else:
    print("Okay, the data shan't be saved")


# Plotting
plt.plot(years, amounts, linestyle='-', marker='o', color='blue', label="Compound Interest (Fixed Rate)")
plt.plot(years, amounts_v, linestyle='--', marker='x', color='orange', label="Compound Interest (Varying Rate)")
plt.plot(years, amounts_si, linestyle='-', marker='s', color='green', label="Simple Interest (Fixed Rate)")
plt.plot(years, amounts_si_v, linestyle='--', marker='d', color='purple', label="Simple Interest (Varying Rate)")
plt.title("Simple vs. Compound Interest Over Time")
plt.xlabel("Years")
plt.ylabel("Amount")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
if save_grph.lower() == "y":
    plt.savefig(f"graph_{now}s.png")
    print(f"Successfully saved the graph as graph_{now}.png")
else:
    print("Okay, the graph shan't be saved as said")


