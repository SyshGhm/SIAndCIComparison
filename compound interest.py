print("hi")
import matplotlib.pyplot as plt

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

# Plotting
plt.plot(years, amounts, marker='o', color='green', label="Compound Interest With Fixed Rate")
plt.plot(years, amounts_v, marker='o', color='blue', label="Compound Interest With Varying Rate")
plt.plot(years, amounts_si, marker='o', color='red', label="Simple Interest With Fixed Rate")
plt.plot(years, amounts_si_v, marker='o', color='brown', label="Simple Interest With Varying Rate")
plt.title("Interest Over Time")
plt.xlabel("Years")
plt.ylabel("Amount")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
