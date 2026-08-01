from telegram import (
    Update,
    InlineQueryResultPhoto,
)

from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    InlineQueryHandler,
    ContextTypes,
    filters,
)

from dotenv import load_dotenv

from renderer import render_latex

import os
import hashlib
import logging
import requests

# ----------------------------
# Logging
# ----------------------------

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)

logger = logging.getLogger(__name__)

# ----------------------------
# Environment
# ----------------------------

load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")

if TOKEN is None:
    raise RuntimeError(
        "BOT_TOKEN not found inside .env"
    )

# ----------------------------
# /start
# ----------------------------

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    text = (
        "👋 *Welcome to LaTeXGo!*\n\n"
        "Send any LaTeX expression and I'll convert it into a PNG image.\n\n"
        "*Example:*\n"
        "`\\frac{a+b}{c}`\n\n"
        "You can also use me inline:\n"
        "`@YourBotUsername \\int_0^\\infty e^{-x^2}dx`"
    )

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )

# ----------------------------
# /help
# ----------------------------

async def help_cmd(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "Examples:\n\n"
        "\\frac{a+b}{c}\n\n"
        "\\sqrt{x^2+y^2}\n\n"
        "\\int_0^\\infty e^{-x^2}dx\n\n"
        "\\sum_{i=1}^{n} i"
    )

# ----------------------------
# /about
# ----------------------------

async def about(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "📐 LaTeXGo\n\n"
        "Version: 1.5\n\n"
        "Render beautiful LaTeX equations directly from Telegram."
    )

# ----------------------------
# /ping
# ----------------------------

async def ping(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "🏓 Pong!"
    )

# ----------------------------
# Render LaTeX
# ----------------------------

async def render(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):
    if update.message is None:
        return

    expr = update.message.text.strip()

    if expr == "":
        return

    # Filter here
    latex_indicators = [
        "\\", "^", "_", "{", "}",
        "\\frac", "\\sqrt", "\\sum",
        "\\int", "\\lim", "\\prod"
    ]

    if not any(token in expr for token in latex_indicators):
        return

    try:
        image_path = render_latex(expr)

        with open(image_path, "rb") as photo:
            await update.message.reply_photo(
                photo=photo,
                caption="✅ Rendered by LaTeXGo",
            )

    except Exception as e:
        logger.exception(e)
# ----------------------------
# Unknown Commands
# ----------------------------

async def unknown(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "Unknown command.\n"
        "Use /help to see available commands."
    )
# ----------------------------
# Inline Mode
# ----------------------------

async def inline(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    query = update.inline_query.query.strip()

    if not query:
        return

    logger.info(
        "Inline request from %s : %s",
        update.effective_user.username,
        query,
    )

    try:

        url = (
            "https://latex.codecogs.com/png.image?"
            + requests.utils.quote(
                r"\dpi{600}\bg_white " + query
            )
        )

        result = InlineQueryResultPhoto(
            id=hashlib.md5(
                query.encode()
            ).hexdigest(),

            title="Render LaTeX",

            photo_url=url,

            thumbnail_url=url,

            caption=query,
        )

        await update.inline_query.answer(
            [result],
            cache_time=60,
            is_personal=True,
        )

    except Exception as e:

        logger.exception(e)

# ----------------------------
# Main
# ----------------------------

def main():

    logger.info("Starting LaTeXGo...")

    app = (
        ApplicationBuilder()
        .token(TOKEN)
        .build()
    )

    # ------------------------
    # Commands
    # ------------------------

    app.add_handler(
        CommandHandler(
            "start",
            start,
        )
    )

    app.add_handler(
        CommandHandler(
            "help",
            help_cmd,
        )
    )

    app.add_handler(
        CommandHandler(
            "about",
            about,
        )
    )

    app.add_handler(
        CommandHandler(
            "ping",
            ping,
        )
    )

    # ------------------------
    # Inline Mode
    # ------------------------

    app.add_handler(
        InlineQueryHandler(
            inline
        )
    )

    # ------------------------
    # Render Messages
    # ------------------------

    app.add_handler(
        MessageHandler(
            filters.TEXT
            & ~filters.COMMAND,
            render,
        )
    )

    # ------------------------
    # Unknown Commands
    # ------------------------

    app.add_handler(
        MessageHandler(
            filters.COMMAND,
            unknown,
        )
    )

    logger.info(
        "LaTeXGo is online."
    )

    app.run_polling(
        allowed_updates=Update.ALL_TYPES
    )


# ----------------------------
# Entry Point
# ----------------------------

if __name__ == "__main__":
    main()

# ----------------------------
# /start
# ----------------------------

async def start(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    user = update.effective_user.first_name

    text = f"""
👋 Hello {user}!

Welcome to *LaTeXGo* 📐

Simply send any LaTeX equation.

Example:

\\frac{{a+b}}{{c}}

Features:

✅ PNG Rendering
✅ Inline Mode
✅ High DPI
✅ Fast Rendering

Commands

/help
/about
/ping

Made with ❤️ using Python & Telegram.
"""

    await update.message.reply_text(
        text,
        parse_mode="Markdown",
    )

# ----------------------------
# /version
# ----------------------------

async def version(
    update: Update,
    context: ContextTypes.DEFAULT_TYPE,
):

    await update.message.reply_text(
        "📐 LaTeXGo\n\n"
        "Version : 1.5\n"
        "Python : python-telegram-bot\n"
        "Renderer : CodeCogs\n"
        "Platform : Telegram"
    )



