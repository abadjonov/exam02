def format_name(full_name: str) -> str:
    parts = full_name.split()
    if len(parts) >= 2:
        surname = parts[0]      
        name = parts[1]    
    
        if len(parts) > 2:
            patronymic = parts[2]
            return f"{name} {patronymic}, {surname}"
        else:
            return f"{name}, {surname}"
    else:
        return full_name

print(format_name("Aliyev Vali G'aniyevich"))