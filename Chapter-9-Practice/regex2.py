import re

text = "User ID: 12345"

match = re.search(r"\d+", text)

if match:
    print("Found a match:", match.group())