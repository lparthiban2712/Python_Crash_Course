
from pathlib import Path
path = Path("chapter_10/pi_digits.txt")  # Update with the correct path
contents = path.read_text()
lines=contents.splitlines()
print(lines)
pi_value = ""
for line in lines:
    print(line)
    pi_value += line
print(pi_value)
print(len(pi_value))

