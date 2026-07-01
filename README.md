
```
  ___    __    ____  _   _     ____   __   _____
 / _ \  / /   / ___ \| | | |   / __ \ / /  |_   _|
| | | |/ /   | |   | | |_| |  | |  | / /     | |
| |_| / / _  | |   | |  _  |  | |__| / / _   | |
 \ _ / / (_) | |___| | | | |   \ __ / / (_)  | |
  \ /  \_____\ \ __/ |_| |_|    \_ \_\      |_|
   v                 for CodeAlpha
```

# AlphaBot — CodeAlpha AI Chatbot Redesign

**AlphaBot** is a professional, retrieval-based chatbot that serves as a customer support assistant for **CodeAlpha** virtual internship programs. It provides instant, empathetic responses to student inquiries with a modern, minimal wabi-sabi aesthetic.

Featuring a beautiful design with white, beige, black, and brown tones, it combines seamless UI/UX with powerful backend persistence.

```
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
```

## Table of Contents

```
┌─────────────────────────────────────┐
│  Navigation Guide                   │
├─────────────────────────────────────┤
│ • Features                          │
│ • Quick Start                       │
│ • Technology Stack                  │
│ • Installation & Local Running      │
│ • Project Structure                 │
│ • Configuration                     │
│ • Website Integration Guide         │
│ • API Endpoints                     │
│ • DB Schema                         │
│ • Troubleshooting                   │
│ • Contributing                      │
│ • License                           │
│ • Contact & Social Links            │
└─────────────────────────────────────┘
```

---

## Features

```
╔════════════════════════════════════════════════════════════╗
║                    CORE CAPABILITIES                       ║
╚════════════════════════════════════════════════════════════╝
```

- **Minimal Beige Theme:** Designed with a warm, minimalist palette utilizing premium modern typography (`Outfit` & `Plus Jakarta Sans`) and glassmorphic components

- **Persistent SQLite Database:** Refactored backend ticket routing to persistently log student application submissions and inquiries inside `codealpha_chatbot.db`

- **Conversation Cache Persistence:** Serializes messaging history to the browser's `localStorage` so users never lose their conversation threads on page reload

- **Clean History Utilities:** Clear chat logs instantly and restore the default dashboard directly from the trash launcher in the header

- **Text-to-Speech (TTS) Voice Narration:** Listen to bot replies spoken aloud with a native Web Speech API (`window.speechSynthesis`) toggle wrapper

- **Click-to-Copy Actions:** Copy messages cleanly to your clipboard using custom action buttons under each response card

- **Floating Launcher Embed Script:** Integrates as a floating widget on any host website layout via an `<iframe>` launcher overlay

---

## Quick Start

```
START HERE IN 3 SIMPLE STEPS
════════════════════════════════════════
```

**Prerequisites:** Python 3.x, pip

```bash
git clone https://github.com/Sweta113Sharma/CodeAlpha_Chatbot.git
cd CodeAlpha_Chatbot
pip install -r requirements.txt
python app.py
```

Visit **http://localhost:5002** in your browser. The chatbot will be ready to use immediately.

```
✓ Clone the repository
✓ Install dependencies  
✓ Start the server
✓ Open browser → Enjoy AlphaBot
```

---

## Technology Stack

```
╔═══════════════════════════════════════════════════════════╗
║              TECHNICAL ARCHITECTURE                       ║
╠═══════════════════════════════════════════════════════════╣
║                                                           ║
║  Backend Layer         │  Frontend Layer                  ║
║  ──────────────────   │  ──────────────                  ║
║  • Flask (Python 3.x) │  • Vanilla JavaScript            ║
║  • SQLite3            │  • Modern CSS                     ║
║  • REST API           │  • HTML5 Semantic Layout         ║
║                                                           ║
║  Additional Services                                      ║
║  ─────────────────────────────────────────              ║
║  • Web Speech API (TTS Narration)                        ║
║  • Google Fonts & FontAwesome 6                          ║
║  • Browser localStorage                                   ║
║                                                           ║
╚═══════════════════════════════════════════════════════════╝
```

---

## Installation & Local Running

```
┏━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┓
┃  STEP-BY-STEP INSTALLATION GUIDE               ┃
┗━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━┛
```

**Step 1: Clone the repository**
```bash
git clone https://github.com/Sweta113Sharma/CodeAlpha_Chatbot.git
cd CodeAlpha_Chatbot
```

**Step 2: Install the dependencies**
```bash
pip install -r requirements.txt
```

**Step 3: Start the server**
```bash
python app.py
```
The application will boot up at **`http://localhost:5002`**.

**Step 4: Access the application**
- Open your browser and navigate to `http://localhost:5002`
- Start chatting with AlphaBot!

```
Success Indicators:
  ✓ Server running on http://localhost:5002
  ✓ Database initialized (codealpha_chatbot.db)
  ✓ Chat interface loaded
```

---

## Project Structure

```
CodeAlpha_Chatbot/
│
├─ app.py                          ► Flask backend server & routes
├─ requirements.txt                ► Python dependencies
│
├─ static/
│  ├─ css/                         ► Stylesheet files (theme, layout, components)
│  └─ js/                          ► Frontend JavaScript (chatbot logic, localStorage)
│
├─ templates/                      ► HTML templates (main interface)
│
├─ codealpha_chatbot.db            ► SQLite database (auto-generated)
├─ embed_code.html                 ► Embedding script for external websites
├─ codealpha_tech_demo.html        ► Live sandbox preview
│
└─ README.md                       ► This file
```

---

## Configuration

Create a `.env` file in the project root to customize settings (optional):

```env
FLASK_ENV=development
FLASK_DEBUG=True
DATABASE_PATH=./codealpha_chatbot.db
FLASK_PORT=5002
```

If no `.env` file is present, the application uses default values defined in `app.py`.

```
Note: Default configuration works out-of-the-box for local development.
Customize only if you need non-standard settings.
```

---

## Website Integration Guide

```
╔══════════════════════════════════════════════════╗
║   EMBED ALPHABOT ON YOUR WEBSITE IN 2 STEPS     ║
╚══════════════════════════════════════════════════╝
```

To embed **AlphaBot** as a floating chat bubble in the bottom-right corner of any web page:

**Step 1:** Copy the integration script from [`embed_code.html`](./embed_code.html)

**Step 2:** Paste it right before the closing `</body>` tag on your host website

The chatbot will appear as a floating widget automatically.

**Live Sandbox Preview:**
A live sandbox preview demonstrating the chatbot integrated on top of the official CodeAlpha website is available locally in [`codealpha_tech_demo.html`](./codealpha_tech_demo.html).

```
┌─────────────────────────────────┐
│    Floating Widget Behavior     │
├─────────────────────────────────┤
│ Location: Bottom-right corner   │
│ Minimizable: Yes                │
│ Persistent: Yes (localStorage)  │
│ Mobile Responsive: Yes          │
└─────────────────────────────────┘
```

---

## API Endpoints

```
╔════════════════════════════════════════════════════════════╗
║               AVAILABLE ROUTES & METHODS                   ║
╠════════════════════════════════════════════════════════════╣
║                                                            ║
║  Endpoint       │ Method │ Description                    ║
║  ───────────────┼────────┼────────────────────────────    ║
║  /              │ GET    │ Main chatbot interface         ║
║  /chat          │ POST   │ Send message & receive AI      ║
║                 │        │ response                       ║
║  /history       │ GET    │ Retrieve conversation cache    ║
║  /tickets       │ GET    │ Fetch all submitted tickets    ║
║  /clear         │ POST   │ Clear history & reset state    ║
║                                                            ║
╚════════════════════════════════════════════════════════════╝
```

---

## DB Schema: `tickets`

```
╔═══════════════════════════════════════════════════════════╗
║              DATABASE TABLE STRUCTURE                     ║
╠═════════════════╦═══════════╦═════════════════════════════╣
║ Field           ║ Type      ║ Description                 ║
╠═════════════════╬═══════════╬═════════════════════════════╣
║ id              ║ TEXT (PK) ║ Unique ticket ref (CA-4184) ║
║ email           ║ TEXT      ║ Student email address       ║
║ domain          ║ TEXT      ║ Selected technical track    ║
║ message         ║ TEXT      ║ Student inquiry details     ║
║ timestamp       ║ TEXT      ║ Submission date (ISO 8601)  ║
╚═════════════════╩═══════════╩═════════════════════════════╝
```

---

## Troubleshooting

```
╔══════════════════════════════════════════════════════════╗
║          COMMON ISSUES & SOLUTIONS                       ║
╚══════════════════════════════════════════════════════════╝
```

| Issue | Solution |
|-------|----------|
| **Port 5002 already in use** | Change the port in `app.py` or: `lsof -ti:5002 \| xargs kill -9` |
| **SQLite database locked** | Restart the Flask server: `python app.py` |
| **TTS not working** | Verify browser compatibility (Chrome, Firefox, Safari). Check audio settings. |
| **Chat history not persisting** | Ensure `localStorage` is enabled in browser. Check console for errors. |
| **Chatbot not responding** | Verify Flask server is running. Check `app.py` logs. |
| **Static files not loading** | Ensure `static/` directory exists. Hard-refresh: Ctrl+Shift+R |

```
For additional help, check the logs or open an issue on GitHub.
```

---

## Contributing

```
╔════════════════════════════════════════════════════════╗
║     WE WELCOME YOUR CONTRIBUTIONS                      ║
╚════════════════════════════════════════════════════════╝
```

We welcome contributions! To get started:

**Step 1: Fork the repository**
```bash
git clone https://github.com/YOUR_USERNAME/CodeAlpha_Chatbot.git
```

**Step 2: Create a feature branch**
```bash
git checkout -b feature/awesome-feature
```

**Step 3: Make your changes & test locally**
```bash
python app.py
```

**Step 4: Commit with clear messages**
```bash
git commit -m 'Add awesome feature: describe what you added'
```

**Step 5: Push to your branch**
```bash
git push origin feature/awesome-feature
```

**Step 6: Open a Pull Request**
- Provide a clear description of changes
- Reference any related issues

```
Your contributions make this project better for everyone!
```

---

## License

```
╔════════════════════════════════════════════════════════╗
║              MIT LICENSE                               ║
║  This project is open-source and free to use          ║
╚════════════════════════════════════════════════════════╝
```

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## Contact & Social Links

```
╔════════════════════════════════════════════════════════╗
║              GET IN TOUCH                              ║
╠════════════════════════════════════════════════════════╣
║                                                        ║
║  Email:   sweta.dollysharma@outlook.com               ║
║  GitHub:  @Sweta113Sharma                             ║
║  LinkedIn: www.linkedin.com/in/swetasharmaa           ║
║  Website: CodeAlpha Virtual Internship                ║
║                                                        ║
╚════════════════════════════════════════════════════════╝
```

For questions, feedback, or collaboration opportunities:

- **Email:** [sweta.dollysharma@outlook.com](mailto:sweta.dollysharma@outlook.com)
- **GitHub:** [@Sweta113Sharma](https://github.com/Sweta113Sharma)
- **LinkedIn:** [www.linkedin.com/in/swetasharmaa](https://www.linkedin.com/in/swetasharmaa)
- **CodeAlpha:** [CodeAlpha Virtual Internship](https://codealpha.tech)

---

```
╔══════════════════════════════════════════════════════════╗
║   Built with dedication for the CodeAlpha community     ║
║                                                          ║
║            Version 1.0 | 2026                           ║
╚══════════════════════════════════════════════════════════╝
```
