# TexifyBot

**TexifyBot** is a Telegram bot that renders LaTeX equations as high-resolution PNG images.

Send a LaTeX expression directly to the bot, or use Telegram Inline Mode to render equations inside other chats.

## Features

- 📐 LaTeX equation rendering
- 🖼️ High-resolution PNG output
- ⚡ Fast rendering
- 🔎 Telegram Inline Mode
- 🛠️ `/start`, `/help`, `/about`, `/ping`, and `/version` commands
- 🐍 Built with Python

## Requirements

- Python 3.10+ recommended
- A Telegram bot token from BotFather

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/TexifyBot.git
cd TexifyBot
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Configuration

Create a `.env` file in the project directory:

```env
BOT_TOKEN=your_telegram_bot_token_here
```

**Never commit your `.env` file or your real bot token to GitHub.**

A safe template is provided as `.env.example`.

## Run

```bash
python bot.py
```

The bot will start polling Telegram for updates.

## Usage

Send an equation such as:

```latex
\frac{a+b}{c}
```

Other examples:

```latex
\sqrt{x^2+y^2}
```

```latex
\int_0^\infty e^{-x^2}dx
```

```latex
\sum_{i=1}^{n} i
```

### Inline Mode

You can also use the bot inline:

```text
@YourBotName \int_0^\infty e^{-x^2}dx
```

Inline Mode must be enabled for your bot through BotFather.

## Project Structure

```text
TexifyBot/
├── bot.py
├── renderer.py
├── requirements.txt
├── README.md
├── .env.example
├── .gitignore
└── LICENSE
```

## Deployment

The bot can be deployed as a background worker on services that support long-running Python processes.

## License

This project is licensed under the MIT License. See `LICENSE`.

## Inspiration 

https://github.com/vdrhtc/InLaTeXbot