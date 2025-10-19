from app.calculator import Calculator

def test_calculator():
    """Test the calculator class with assertions."""
    calc = Calculator()
    
    # Test addition
    result = calc.add(2, 3)
    assert result == 5, f"Addition failed: expected 5, got {result}"
    assert result is not None, "add() should return a value"
    print(f"✓ Addition test passed: 2 + 3 = {result}")
    
    # Test subtraction
    result = calc.subtract(10, 4)
    assert result == 6, f"Subtraction failed: expected 6, got {result}"
    assert result is not None, "subtract() should return a value"
    print(f"✓ Subtraction test passed: 10 - 4 = {result}")
    
    # Test multiplication
    result = calc.multiply(3, 7)
    assert result == 21, f"Multiplication failed: expected 21, got {result}"
    assert result is not None, "multiply() should return a value"
    print(f"✓ Multiplication test passed: 3 * 7 = {result}")
    
    # Test division
    result = calc.divide(20, 4)
    assert result == 5.0, f"Division failed: expected 5.0, got {result}"
    assert result is not None, "divide() should return a value"
    print(f"✓ Division test passed: 20 / 4 = {result}")
    
    # Test division by zero
    try:
        calc.divide(10, 0)
        assert False, "Division by zero should raise an error"
    except ValueError as e:
        print(f"✓ Division by zero test passed: {e}")
    
    # Test power (homework - should return None currently)
    result = calc.power(2, 3)
    print(f"⚠ Power operation not implemented yet (homework): 2 ** 3 = {result}")
    
    print("\n✅ All calculator tests passed!")

if __name__ == "__main__":
    test_calculator()