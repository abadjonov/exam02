def atm_operation(balance: int, action: str, amount: int) -> int:
    if amount < 0:
        return "Error: Manfiy summa kiritib bo'lmaydi"
    
    if action == "deposit":
        return balance + amount
    elif action == "withdraw":
        if amount > balance:
            return "Error: Mablag' yetarli emas"
        return balance - amount
    else:
        return "Error: Noto'g'ri amal"

print(atm_operation(100000, "deposit", 50000))  
print(atm_operation(100000, "withdraw", 20000))  

