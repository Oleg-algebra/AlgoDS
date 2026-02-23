import re

# Our sample "Common Text"
text = "Contact us at support@example.com or sales@shop.net. Phone: 555-1234. Born: 1990-05-20."

# A list of 10 common patterns to test
patterns = [
    (r'[a-z]+', "1. All sequences of lowercase letters"),
    (r'[A-Z][a-z]+', "2. Words starting with a Capital letter"),
    (r'\d+', "3. Any sequence of digits"),
    (r'\d{4}', "4. Exactly four digits in a row (years)"),
    (r'\w+@\w+\.\w+', "5. Simple Email structures"),
    (r'\d{3}-\d{4}', "6. Phone number format (3 digits, dash, 4 digits)"),
    (r'[^ ]+', "7. Anything that is NOT a space (words/symbols)"),
    (r'[aeiou]', "8. Every individual vowel"),
    (r's\w+', "9. Any word starting with 's'"),
    (r'\b\w{2}\b', "10. Exactly two-letter words")
]

print(f"Target Text: {text}\n" + "-"*60)

for pattern, description in patterns:
    matches = re.findall(pattern, text)
    print(f"{description:<45} | Matches: {matches}")