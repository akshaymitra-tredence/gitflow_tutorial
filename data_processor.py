def process_data(items):
    """
    Process a list of items: filter even numbers and square them.
    Enterprise example: simple but with type hints and docstring.
    """
    if not isinstance(items, list):
        raise TypeError("Input must be a list")
    
    result = []
    for item in items:
        if isinstance(item, (int, float)) and item % 2 == 0:
            result.append(item ** 2)
    return result

# Example usage (for testing)
if __name__ == "__main__":
    sample = [1, 2, 3, 4, "hello", 6.0, 8]
    print("Processed:", process_data(sample))  # Expected: [4, 16, 36, 64]