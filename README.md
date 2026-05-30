# Password Strength Analyzer

## Overview

Password Strength Analyzer is a Python-based cybersecurity application designed to evaluate the strength and security of user passwords. The tool analyzes passwords using various security metrics such as length, character complexity, entropy, common patterns, and breached password detection. It provides detailed feedback and recommendations to help users create stronger and more secure passwords.

The project also includes a secure password generator and optional password history protection using encrypted password storage.

---

## Features

### Password Strength Analysis
- Password length validation
- Uppercase and lowercase letter detection
- Number and special character detection
- Character diversity analysis
- Entropy calculation
- Password strength scoring (0–100)
- Strength classification:
  - Very Weak
  - Weak
  - Moderate
  - Strong
  - Very Strong

### Security Feedback
- Identifies password weaknesses
- Provides personalized recommendations
- Detects predictable patterns and common passwords

### Password Generator
- Generate secure random passwords
- Customizable password length
- Support for symbols, numbers, and uppercase characters

### Breach Detection
- Checks passwords against a local list of commonly leaked passwords
- Warns users about compromised passwords

### Password History Protection (Optional)
- SQLite database support
- Password hashing using bcrypt
- Prevents password reuse
- Stores password creation timestamps

### Educational Module
- Password entropy explanation
- Hashing and salting concepts
- Brute-force attack awareness
- Dictionary attack awareness
- Credential stuffing awareness

---

## Project Structure

```text
PasswordStrengthAnalyzer/
│
├── main.py
├── analyzer.py
├── generator.py
├── entropy.py
├── database.py
├── breach_checker.py
├── utils.py
│
├── data/
│   └── common_passwords.txt
│
├── database/
│   └── passwords.db
│
├── tests/
│   └── test_analyzer.py
│
├── screenshots/
│
└── README.md
```

---

## Requirements

- Python 3.8+
- SQLite3
- bcrypt

Install dependencies:

```bash
pip install bcrypt
```

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/PasswordStrengthAnalyzer.git
```

2. Navigate to the project directory:

```bash
cd PasswordStrengthAnalyzer
```

3. Install required packages:

```bash
pip install -r requirements.txt
```

4. Run the application:

```bash
python main.py
```

---

## Sample Output

```text
====================================
PASSWORD SECURITY REPORT
====================================

Password Length      : 14
Uppercase Letters    : 3
Lowercase Letters    : 6
Numbers              : 2
Special Characters   : 3

Entropy Score        : 78.4 bits
Security Score       : 92/100

Strength             : VERY STRONG

Issues Found         : None

Recommendations      :
✓ Excellent password

====================================
```

---

## Security Considerations

- Plaintext passwords are never stored.
- Password history is protected using bcrypt hashing.
- Commonly breached passwords are detected.
- Secure random generation is used for password creation.
- Password reuse prevention is supported.

---

## Testing

Run unit tests using:

```bash
pytest tests/
```

---

## Future Enhancements

- GUI using Tkinter or CustomTkinter
- Flask web dashboard
- Machine learning-based password risk assessment
- PDF security report generation
- Multi-user support
- Cloud-based breach database integration

---

## Learning Outcomes

This project helps users understand:

- Password security principles
- Entropy calculation
- Cryptographic hashing
- Secure password generation
- Password attack techniques
- Cybersecurity best practices

---

## Author

Developed as a Cybersecurity and Python Programming Project for academic and portfolio purposes.

## License

This project is licensed under the MIT License.
