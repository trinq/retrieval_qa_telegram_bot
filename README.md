
# Telegram Bot

This is a Telegram bot that provides answers to user queries using a retrieval-augmented generation approach. It uses the Langchain library for chaining together multiple capabilities including integration with LLMs (e.g. ChatGPT) and FAISS for vector similarity search.

## Installation

1. Clone this repository to your local machine.
2. Create a virtual environment for the project: `python3 -m venv venv`.
3. Activate the virtual environment: `source venv/bin/activate`.
4. Install the dependencies: `pip install -r requirements.txt`.
5. Set up the environment variables by creating a `.env` file in the project directory and adding the following lines:

```
TELEGRAM_TOKEN=<your-telegram-bot-token>
OPENAI_API_KEY=<your-openai-api-key>
```

6. Start the FastAPI app: `uvicorn app.main:app --reload`.
7. Start the Telegram bot: `python telegram_bot.py`.

## Usage

Once you've installed and started the Telegram bot, you can interact with it using the Telegram app. Simply search for the bot in Telegram and start a conversation with it.

To ask the bot a question, type `/ask <your-question>` in the chat window. The bot will use a retrieval-augmented generation approach to generate an answer to your question.

## Credits

This project was inspired by the [GovTech developer portal](https://www.developer.tech.gov.sg/), which uses a similar approach to provide answers to user queries. The code for this project was adapted from the Langchain library and other open-source projects.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.