principal = 1000      # in dollars
rate = 0.05           # 5% annual interest rate as a decimal
time = 3

interest = principal * rate * time

print(f"Principal Amount: ${principal}")
print(f"Annual Interest Rate: {rate * 100}%")
print(f"Time Period: {time} years")
print(f"Simple Interest Earned: ${interest:.2f}")