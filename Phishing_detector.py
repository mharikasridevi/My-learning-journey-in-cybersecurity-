print("Phishing Email Detector")

email_text = input("Paste email text: ").lower()

suspicious_words = [
    "urgent",
    "click here",
    "verify account",
    "password",
    "bank",
    "winner",
    "claim prize"
]

score = 0

for word in suspicious_words:
    if word in email_text:
        score += 1

print("Suspicious keywords found:", score)

if score >= 3:
    print("High Risk: Possible Phishing Email")
elif score >= 1:
    print("Medium Risk: Be Careful")
else:
    print("Low Risk")
