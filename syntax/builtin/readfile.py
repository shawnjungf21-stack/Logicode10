import os
def writefile(filename: str, filepath: str, content: str):
    os.makedirs(filepath, exist_ok=True)
    full_path = os.path.join(filepath, filename)
    with open(full_path, "w", encoding="utf-8") as f:
        f.write(content)
    print(f"File written: {full_path}")
def readfile(filename: str, filepath: str):
    full_path = os.path.join(filepath, filename)
    if not os.path.exists(full_path):
        print(f"Error: File not found at {full_path}")
        return None
    with open(full_path, "r", encoding="utf-8") as f:
        content = f.read()
    print(f"File read: {full_path}")
    return content
if __name__ == "__main__":
    writefile("example.txt", "./testdir", "Hello from Logicode!")
    data = readfile("example.txt", "./testdir")
    print("File content:", data)
