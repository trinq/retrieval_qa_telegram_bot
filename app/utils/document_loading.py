import os

def load_documents(doc_directory, chunk_size):
    documents = []
    
    # Walk through the directory and find all files with a .txt extension
    for root, dirs, files in os.walk(doc_directory):
        for file in files:
            if file.endswith(".txt"):
                file_path = os.path.join(root, file)
                with open(file_path, "r") as f:
                    # Read the contents of the file and split it into chunks
                    content = f.read()
                    chunks = [content[i:i+chunk_size] for i in range(0, len(content), chunk_size)]
                    # Add each chunk and its corresponding URL to the documents list
                    for i, chunk in enumerate(chunks):
                        url = f"{DOCUMENT_BASE_URL}/{file}#chunk{i+1}"
                        documents.append((chunk, url))
    
    return documents
