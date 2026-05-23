import re

text = """
Order ID: A123
Order ID: B456
Order ID: C789
"""

# Extract letter + numbers
matches = re.findall(r"([A-Z]\d+)", text)

print("Orders:", matches)

# Extract only numbers
numbers = re.findall(r"\d+", text)

