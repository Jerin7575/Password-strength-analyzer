from analyzer import PasswordAnalyzer
from generator import PasswordGenerator

def main():
    print("Password Strength Analyzer")
    pwd = input("Enter password: ")
    analyzer = PasswordAnalyzer()
    report = analyzer.analyze(pwd)
    for k,v in report.items():
        print(f"{k}: {v}")

if __name__ == "__main__":
    main()
