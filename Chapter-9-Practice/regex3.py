import re

text = "Date: 2026-05-22"

match = re.search(r"(\d{4})-(\d{2})-(\d{2})", text)

print(match.group(0))  # whole match
print(match.group(1))  # year
print(match.group(2))  # month
print(match.group(3))  # day