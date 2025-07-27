"""Provides utility functions for the application, such as text preprocessing."""

import re

def preprocess_text(text: str) -> str:
    """
    Cleans and preprocesses text by removing extra whitespace and newlines,
    while preserving code blocks.
    """
    if not isinstance(text, str):
        return ""

    # Preserve code blocks (anything between triple backticks or indented)
    code_pattern = r'```[\\s\\S]*?```|(?:^|\\n)(?: {4,}|\\t)[^\\n]*(?:\\n(?: {4,}|\\t)[^\\n]*)*'
    code_blocks = re.findall(code_pattern, text, re.MULTILINE)

    # Replace code blocks with placeholders
    for i, block in enumerate(code_blocks):
        text = text.replace(block, f"__CODE_BLOCK_{i}__")

    # Clean text (remove extra whitespace, normalize)
    text = re.sub(r'\\s+', ' ', text)
    text = re.sub(r'\\n+', '\\n', text)
    text = text.strip()

    # Restore code blocks
    for i, block in enumerate(code_blocks):
        text = text.replace(f"__CODE_BLOCK_{i}__", block)

    return text
