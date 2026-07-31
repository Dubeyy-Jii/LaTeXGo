# LaTeXGo 🚀

Convert LaTeX equations into beautiful, high-quality images directly from Telegram.

LaTeXGo is a lightweight Telegram bot that renders mathematical expressions into PNG images, making it easy to share formulas in chats, notes, presentations, and study groups.

---

## ✨ Features

- 📐 Render LaTeX equations instantly
- 🖼️ High-quality PNG output
- ⚡ Fast and lightweight
- 🤖 Simple Telegram interface
- 📱 Works on Windows, Linux, and Android (Termux)

---

## Example

Input:

```latex
\int_0^\infty e^{-x^2}\,dx=\frac{\sqrt{\pi}}{2}
```

Output:

*A beautifully rendered mathematical equation.*

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/LaTeXGo.git
cd LaTeXGo
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a `.env` file:

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Obtain your bot token from **@BotFather**.

---

## Usage

Start the bot:

```bash
python bot.py
```

Open Telegram, start your bot, and send any LaTeX expression.

Example:

```latex
\frac{a+b}{c}
```

The bot will reply with the rendered equation as an image.

---

## Project Structure

```
LaTeXGo/
├── bot.py
├── renderer.py
├── requirements.txt
├── .env.example
└── README.md
```

---

## Roadmap

- [ ] Inline equation support
- [ ] SVG export
- [ ] PDF export
- [ ] Dark & light themes
- [ ] User preferences
- [ ] Equation history
- [ ] Syntax error highlighting

---

## Contributing

Contributions, feature requests, and bug reports are always welcome.

If you find this project useful, consider giving it a ⭐ on GitHub.

---

## License

This project is licensed under the MIT License.

---

Made with ❤️ for students, educators, researchers, and the mathematics community.
