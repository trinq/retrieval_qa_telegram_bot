
```
# Retrieval-Augmented Generation Q&A using Telegram Bot

This project is a Q&A system that uses a retrieval-augmented generation approach to answer questions. The system retrieves relevant documents from a database using a vector similarity search algorithm and generates an answer based on the retrieved documents and the original question. The Q&A system is deployed as a Telegram bot that can be used to ask questions and receive answers.

## Requirements

To use this Q&A system, you will need the following:

- Python 3.7 or later
- The packages listed in `requirements.txt`
- A Telegram account and an API token for a Telegram bot (see the Telegram documentation for instructions on how to create a bot and obtain an API token)
- A directory containing plain text documents to use as the database
- An OpenAI API key (optional, only required if using the OpenAI embeddings method for generating document vectors)

## Installation

1. Clone the repository:

```
git clone https://github.com/<username>/<repository>.git
```

2. Navigate to the project directory:

```
cd <repository>
```

3. Install the necessary packages:

```
pip install -r requirements.txt
```

4. Create a `.env` file in the project directory with the following variables:

```
TELEGRAM_BOT_TOKEN=<your Telegram bot token>
K=<the number of top results to return>
DOCUMENT_DIRECTORY=<the path to the directory containing the plain text documents>
OPENAI_API_KEY=<your OpenAI API key (optional)>
BASE_URL=<the URL of your deployed FastAPI app>
```

5. Start the Telegram bot:

```
python telegram_bot.py
```

## Usage

1. Start a chat with your Telegram bot.
2. Send a message containing your question.
3. The bot will retrieve the top results from the document database and send them back to you.

## Additional Notes

- If you need to index new documents, you can run the `indexing.py` script to create a new vector store. You may also need to modify the `load_documents()` function in `app/utils/document_loading.py` to properly load your new documents.
- The default vector store uses the FAISS library for similarity search, but you can also use other vector stores such as Pinecone, Weaviate, or OpenSearch by modifying the `app/utils/vector_store.py` module.
- The default method for generating document vectors uses the OpenAI GPT-3.5 language model, but you can also use other embeddings methods such as BERT, USE, or Doc2Vec by modifying the `app/utils/embeddings.py` module.
```