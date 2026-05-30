import secrets, string

class PasswordGenerator:
    def generate(self, length=16):
        chars = string.ascii_letters + string.digits + string.punctuation
        return "".join(secrets.choice(chars) for _ in range(length))
