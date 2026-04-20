calculate_tax = (8_000_000)
# {"gross": 8000000, "tax": 360000, "net": 7640000, "rate": "12%"}

calculate_tax2 = (3_000_000)
# {"gross": 3000000, "tax": 0, "net": 3000000, "rate": "0%"}

def calculator_taks(salary: int) -> dict:
    if salary <= 5_000_000:
        rate = 0
        rate_str = "0%"
    elif salary <= 10_000_000:
        rate = 12
        rate_str = "12%"
    elif salary <= 20_000_000:
        rate = 18
        rate_str = "18%"
    else:
        rate = 25
        rate_str = "25%"
        
    tax_amount = int(salary * (rate / 100))
    net_salary = salary - tax_amount
    
    return {
        "gross": salary,
        "tax": tax_amount,
        "net": net_salary,
        "rate": rate_str
    }

print(calculator_taks(calculate_tax))
print(calculator_taks(calculate_tax2))