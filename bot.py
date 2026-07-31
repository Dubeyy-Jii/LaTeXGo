from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters
from renderer import render_latex
from dotenv import load_dotenv
import os

load_dotenv()
TOKEN=os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Send any LaTeX math expression and I'll return it as a PNG."
    )

async def help_cmd(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(r"Example: \frac{a}{b}")

async def handle(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text=update.message.text.strip()
    try:
        img=render_latex(text)
        with open(img,"rb") as f:
            await update.message.reply_photo(f)
    except Exception:
        await update.message.reply_text("❌ Invalid LaTeX expression.")

app=ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start",start))
app.add_handler(CommandHandler("help",help_cmd))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND,handle))

if __name__=="__main__":
    app.run_polling()
