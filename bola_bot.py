import os
from telegram import Update
from telegram.ext import Application, CallbackQueryHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]

GAME_URL = "https://zairovasoliha08-pixel.github.io/bolajon-tetris/"

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    if query.game_short_name == "bolajon_oyini":
        await query.answer(url=GAME_URL)

app = Application.builder().token(TOKEN).build()
app.add_handler(CallbackQueryHandler(game))

print("Bola bot ishlayapti...")
app.run_polling()
