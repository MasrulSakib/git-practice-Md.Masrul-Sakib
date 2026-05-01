def add(a, b):
    try:
        return float(a) + float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

def subtract(a, b):
    try:
        return float(a) - float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."

def multiply(a, b):
    try:
        return float(a) * float(b)
    except (ValueError, TypeError):
        return "Error: Both inputs must be numbers."