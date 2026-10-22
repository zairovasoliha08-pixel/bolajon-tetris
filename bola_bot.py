import os
import threading
from http.server import HTTPServer, SimpleHTTPRequestHandler

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CallbackQueryHandler, CommandHandler, ContextTypes

TOKEN = os.environ["BOT_TOKEN"]
GAME_URL = "https://zairovasoliha08-pixel.github.io/bolajon-tetris/"

def web_server():
    port = int(os.environ.get("PORT", 10000))
    HTTPServer(("0.0.0.0", port), SimpleHTTPRequestHandler).serve_forever()

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🎮 Tetris o‘ynash", callback_game={})]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 Salom!\n\n🎮 Tetris o‘ynashni xohlaysanmi?\n👇 Tugmani bos:",
        reply_markup=reply_markup
    )

async def game(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query

    if query.game_short_name == "bolajon_oyini":
        await query.answer(url=GAME_URL)

threading.Thread(target=web_server, daemon=True).start()

app = Application.builder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(game))

print("Bola bot ishlayapti...")
app.run_polling()
