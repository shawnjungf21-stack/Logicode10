try:
    with open("pt.py", "r", encoding="utf-8") as f:
        content = f.read()
    print(content)
except FileNotFoundError:
    print("no.")