from telegram import Update
from telegram.ext import (
    Application,
    CommandHandler,
    MessageHandler,
    filters,
    ContextTypes
)

from config import TELEGRAM_TOKEN
from rag import preguntar


async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    await update.message.reply_text(
        "Hola 👋 Soy el asistente de logística. "
        "Puedes preguntarme sobre envíos, políticas y servicios."
    )


async def responder(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE
):

    pregunta = update.message.text

    respuesta = preguntar(pregunta)

    await update.message.reply_text(respuesta)


def main():

    app = Application.builder().token(
        TELEGRAM_TOKEN
    ).build()


    app.add_handler(
        CommandHandler(
            "start",
            start
        )
    )


    app.add_handler(
        MessageHandler(
            filters.TEXT & ~filters.COMMAND,
            responder
        )
    )


    print("Bot iniciado...")

    app.run_polling()


if __name__ == "__main__":
    main()