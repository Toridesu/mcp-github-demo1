"""
A sample Python script demonstrating basic functionality
"""

def greet(name: str = "World") -> str:
    """
    Returns a greeting message
    
    Args:
        name (str): Name to greet, defaults to "World"
        
    Returns:
        str: Greeting message
    """
    return f"Hello, {name}! Welcome to Claude Desktop MCP!"

def calculate_sum(numbers: list[int]) -> int:
    """
    Calculates sum of numbers
    
    Args:
        numbers (list[int]): List of numbers to sum
        
    Returns:
        int: Sum of numbers
    """
    return sum(numbers)

if __name__ == "__main__":
    # Basic greeting
    print(greet())
    
    # Personalized greeting
    print(greet("Claude"))
    
    # Number calculation
    numbers = [1, 2, 3, 4, 5]
    print(f"Sum of {numbers} is {calculate_sum(numbers)}")
