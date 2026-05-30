from analyzer import PasswordAnalyzer

def test_analysis():
    assert PasswordAnalyzer().analyze("Abc@123456789")["Score"] > 50
  
