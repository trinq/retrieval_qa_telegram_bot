import re

def preprocess_text(text: str) -> str:
    # Apply any necessary text preprocessing steps to the input text
    text = text.lower()
    text = re.sub(r"[^a-z0-9\s]", "", text)
    text = re.sub(r"\s+", " ", text)

    return text

def extract_text(documents: list) -> list:
    # Extract text from the input documents
    texts = []

    for doc in documents:
        # Extract the text from the document using regex, XPath, or other methods
        text = # your code here

        texts.append(text)

    return texts
