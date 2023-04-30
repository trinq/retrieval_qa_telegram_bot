import logging
from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from app.api.retrieval import retrieve_documents
from app.api.indexing import load_vector_store
from langchain.chat_models import ChatOpenAI
from langchain.chains import RetrievalQAWithSourcesChain

# Set up logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)
logger = logging.getLogger(__name__)

# Load environment variables
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Load vector store and LLM
vector_store = load_vector_store()
llm = ChatOpenAI(model_name="gpt-3.5-turbo", temperature=0, max_tokens=256)
chain_type_kwargs = {"prompt": ""}
chain = RetrievalQAWithSourcesChain.from_chain_type(
    llm=llm,
    chain_type="stuff",
    retriever=vector_store.as_retriever(),
    return_source_documents=True,
    chain_type_kwargs=chain_type_kwargs
)

# Define command handlers
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I am a Q&A bot. Ask me a question using the /ask command.')

def ask(update: Update, context: CallbackContext) -> None:
    """Retrieve an answer to the user's question."""
    query = " ".join(context.args)
    if query:
        results = retrieve_documents(query, vector_store, chain)
        answer = results["answer"]
        sources = results["sources"]
        source_urls = list(set([doc.metadata['source'] for doc in results['source_documents']]))
        response = f"Q: {query}\n\nA: {answer}\n\nSources: {sources}\n\nAll relevant sources: {source_urls}"
    else:
        response = "Please provide a question to search for."
    update.message.reply_text(response)

def fallback(update: Update, context: CallbackContext) -> None:
    """Fallback message for unsupported commands."""
    update.message.reply_text('Sorry, I did not understand that command. Please use the /ask command to ask me a question.')

# Set up handlers and start the bot
def main() -> None:
    updater = Updater(TELEGRAM_TOKEN)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("ask", ask))
    dispatcher.add_handler(MessageHandler(Filters.command, fallback))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
