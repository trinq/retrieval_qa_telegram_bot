import os
import pathlib
from langchain.docstore.document import Document
from langchain.document_loaders import TextLoader

def load_documents(directory):
    """
    Load plain text documents from the specified directory and return them as a list of Document objects.

    :param directory: The path to the directory containing the documents.
    :return: A list of Document objects, one for each document in the directory.
    """
    loader = TextLoader()
    documents = []
    for file in os.listdir(directory):
        if file.endswith(".txt"):
            with open(os.path.join(directory, file), "r") as f:
                content = f.read()
            document = Document(page_content=content, metadata={"filename": file})
            document = loader.load(document)
            documents.append(document)
    return documents
