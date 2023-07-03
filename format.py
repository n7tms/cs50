import re

name = input("What's your name? ").strip()
matches = re.search(r"^(.+), *(.+)$", name)
if matches:
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")

# The above code is equivalent to vvv
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)

# The walrus operator " := " assigns the value on the right to the variable on the left,
# and then allows the IF statement to test the boolean logic on that variable.