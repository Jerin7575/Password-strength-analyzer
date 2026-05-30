import math, re

COMMON = {"password","123456","qwerty","admin123"}

class PasswordAnalyzer:
    def analyze(self, password:str):
        score = 0
        issues = []

        if len(password) >= 12: score += 25
        else: issues.append("Password shorter than 12 characters")

        if re.search(r"[A-Z]", password): score += 15
        else: issues.append("Missing uppercase letters")

        if re.search(r"[a-z]", password): score += 15
        else: issues.append("Missing lowercase letters")

        if re.search(r"\d", password): score += 15
        else: issues.append("Missing numbers")

        if re.search(r"[^A-Za-z0-9]", password): score += 15
        else: issues.append("Missing special characters")

        entropy = self.entropy(password)
        score += min(15, int(entropy/6))

        if password.lower() in COMMON:
            issues.append("Known breached/common password")
            score = max(0, score-40)

        strength = (
            "Very Weak" if score < 20 else
            "Weak" if score < 40 else
            "Moderate" if score < 60 else
            "Strong" if score < 80 else
            "Very Strong"
        )

        return {
            "Score": score,
            "Strength": strength,
            "Entropy(bits)": round(entropy,2),
            "Issues": issues or ["None"]
        }

    def entropy(self, password:str):
        charset = 0
        if re.search(r"[a-z]", password): charset += 26
        if re.search(r"[A-Z]", password): charset += 26
        if re.search(r"\d", password): charset += 10
        if re.search(r"[^A-Za-z0-9]", password): charset += 32
        return len(password) * math.log2(max(charset,1))
