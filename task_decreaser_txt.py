import re

filename = "tasks.txt"  # Replace with the name of your file

# Read the contents of the file
with open(filename, "r",encoding="utf-8") as f:
    text = f.read()

# Decrease all integers (surrounded by whitespace) in the text by one using regular expressions
new_text = re.sub(r"(?<=\s)(\d+)(?=\s)", lambda x: str(max(int(x.group(1))-1, 0)) if int(x.group(1)) >0 else (print("Integer value reached zero!"), "0"), text)

# Write the modified text back to the file
with open(filename, "w",encoding="utf-8") as f:
    f.write(new_text)
    f.write('wrote')