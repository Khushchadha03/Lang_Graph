import json
from typing import Any, Dict

def calculator(expression: str) -> str:
    """A calculator tool for mathematical expressions."""
    try:
        result: Any = eval(expression.strip())
        return str(result)
    except Exception as e:
        return f"Calculation error: {e}"

def text_analyzer(text: str) -> str:
    """Analyze text properties."""
    word_count = len(text.split())
    char_count = len(text)
    lines = len(text.split('\n'))
    
    analysis = {
        "word_count": word_count,
        "character_count": char_count,
        "line_count": lines,
        "avg_word_length": round(char_count / word_count, 2) if word_count > 0 else 0
    }
    
    return json.dumps(analysis, indent=2)

def string_transformer(text: str, operation: str = "upper") -> str:
    """Transform strings with various operations."""
    operations = {
        "upper": text.upper(),
        "lower": text.lower(),
        "title": text.title(),
        "reverse": text[::-1],
        "word_count": str(len(text.split())),
        "char_count": str(len(text))
    }
    return operations.get(operation, f"Unknown operation: {operation}")