# 📐 LaTeXGo

> Convert LaTeX expressions into beautiful, high-quality images directly from Telegram.

![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)
![Telegram Bot](https://img.shields.io/badge/Telegram-Bot-26A5E4.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Active-success.svg)

---

## ✨ Features

- 📷 Render any valid LaTeX expression into a high-quality PNG.
- 🚀 Inline Mode (`@LaTeXGoBot`) for rendering equations in any Telegram chat.
- ⚡ Fast cloud-based rendering using CodeCogs.
- 📐 Supports advanced mathematical notation.
- 🤖 Simple and intuitive interface.
- 📱 Works on desktop and mobile.

---

## 📸 Examples

### Input

```latex
\frac{a+b}{c}
```

### Output

Beautiful rendered equation.

---

### Supports

- Fractions
- Square Roots
- Summations
- Products
- Integrals
- Double & Triple Integrals
- Limits
- Matrices
- Piecewise Functions
- Greek Symbols
- Vectors
- Quantum Mechanics
- General Relativity Equations
- And much more...

---

# 🚀 Commands

| Command | Description |
|---------|-------------|
| `/start` | Start the bot and display a welcome message. |
| `/help` | Show usage instructions and LaTeX examples. |
| `/about` | Learn more about LaTeXGo. |
| `/ping` | Check whether the bot is online. |
| `/version` | Display the current bot version. |

---

# 💬 Inline Mode

Render equations directly inside any Telegram chat.

Example:

```text
@LaTeXGoBot \int_0^\infty e^{-x^2}\,dx
```

Telegram instantly previews the rendered equation before sending.

---

# 📖 Examples

Fraction

```latex
\frac{a+b}{c}
```

Integral

```latex
\int_0^\infty e^{-x^2}\,dx
```

Matrix

```latex
\begin{bmatrix}
1 & 2\\
3 & 4
\end{bmatrix}
```

Piecewise Function

```latex
f(x)=
\begin{cases}
x^2,&x>0\\
0,&x\le0
\end{cases}
```

Einstein Field Equation

```latex
R_{\mu\nu}-\frac12Rg_{\mu\nu}
+\Lambda g_{\mu\nu}
=
\frac{8\pi G}{c^4}T_{\mu\nu}
```

---

# 🛠 Installation

Clone the repository

```bash
git clone https://github.com/YOUR_USERNAME/LaTeXGo.git
```

Enter the project

```bash
cd LaTeXGo
```

Install dependencies

```bash
pip install -r requirements.txt
```

Create a `.env` file

```env
BOT_TOKEN=YOUR_TELEGRAM_BOT_TOKEN
```

Run the bot

```bash
python bot.py
```

---

# 📂 Project Structure

```
LaTeXGo/
│
├── bot.py
├── renderer.py
├── requirements.txt
├── .env.example
├── LICENSE
└── README.md
```

---

# 🧠 Tech Stack

- Python
- python-telegram-bot
- CodeCogs LaTeX API
- Requests
- python-dotenv

---

# 🔮 Roadmap

- [x] PNG Rendering
- [x] Inline Mode
- [x] High DPI Rendering
- [ ] Transparent PNG
- [ ] SVG Export
- [ ] PDF Export
- [ ] Render History
- [ ] User Settings
- [ ] Dark Theme
- [ ] Multiple Rendering Engines

---

# 🤝 Contributing

Contributions, feature requests, and bug reports are always welcome!

Feel free to open an Issue or submit a Pull Request.

---

# 📄 License

This project is licensed under the MIT License.

---

## ⭐ If you like this project

Give the repository a ⭐ on GitHub!

---

Made with ❤️ for students, researchers, teachers, and LaTeX enthusiasts.
