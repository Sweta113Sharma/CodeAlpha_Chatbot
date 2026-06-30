# AlphaBot — CodeAlpha AI Chatbot Redesign

**AlphaBot** is a professional, retrieval-based chatbot that serves as a customer support assistant for **CodeAlpha** virtual internship programs. It provides instant, empathetic responses to student inquiries about internship tracks, certification requirements, and technical topics—reducing support overhead while improving student experience.

Featuring a modern, minimal wabi-sabi aesthetic (white, beige, black, and brown), it combines seamless UI/UX with powerful backend persistence.

---

## Table of Contents

- [Features](#features)
- [Quick Start](#quick-start)
- [Technology Stack](#technology-stack)
- [Installation & Local Running](#installation--local-running)
- [Project Structure](#project-structure)
- [Configuration](#configuration)
- [Website Integration Guide](#website-integration-guide)
- [API Endpoints](#api-endpoints)
- [DB Schema](#db-schema-tickets)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Contact](#contact)

---

## Features

- **Minimal Beige Theme:** Designed with a warm, minimalist palette (white, beige, charcoal, and warm brown) utilizing premium modern typography (`Outfit` & `Plus Jakarta Sans`) and glassmorphic card designs for visual elegance.
- **Persistent SQLite Database:** Refactored backend ticket routing to persistently log student application submissions and inquiries inside `codealpha_chatbot.db`.
- **Conversation Cache Persistence:** Serializes messaging history to the browser's `localStorage` so users never lose their conversation threads on page reload.
- **Clean History Utilities:** Clear chat logs instantly and restore the default dashboard directly from the trash launcher in the header.
- **Text-to-Speech (TTS) Voice Narration:** Listen to bot replies spoken aloud with a native Web Speech API (`window.speechSynthesis`) toggle wrapper.
- **Click-to-Copy Actions:** Copy messages cleanly to your clipboard using custom action buttons under each response card.
- **Floating Launcher Embed Script:** Integrates as a floating widget on any host website layout via an `<iframe>` launcher overlay.

---

## Quick Start

**Prerequisites:** Python 3.x, pip

```bash
git clone https://github.com/Sweta113Sharma/CodeAlpha_Chatbot.git
cd CodeAlpha_Chatbot
pip install -r requirements.txt
python app.py
```

Visit **http://localhost:5002** in your browser. The chatbot will be ready to use immediately.

---

## Technology Stack

- **Backend:** Flask (Python 3.x), SQLite3
- **Frontend:** Vanilla JavaScript, Modern CSS, HTML5 semantic layout
- **Narration:** Web Speech API (`SpeechSynthesisUtterance`)
- **Branding Assets:** Google Fonts, FontAwesome 6
- **Database:** SQLite3 with persistent ticket logging

---

## Installation & Local Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Sweta113Sharma/CodeAlpha_Chatbot.git
   cd CodeAlpha_Chatbot
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Start the server:**
   ```bash
   python app.py
   ```
   The application will boot up at **`http://localhost:5002`**.

4. **Access the application:**
   - Open your browser and navigate to `http://localhost:5002`
   - Start chatting with AlphaBot!

---

## Project Structure

```
CodeAlpha_Chatbot/
├── app.py                          # Flask backend server & routes
├── requirements.txt                # Python dependencies
├── static/
│   ├── css/                        # Stylesheet files (theme, layout, components)
│   └── js/                         # Frontend JavaScript (chatbot logic, localStorage)
├── templates/                      # HTML templates (main interface)
├── codealpha_chatbot.db            # SQLite database (auto-generated)
├── embed_code.html                 # Embedding script for external websites
├── codealpha_tech_demo.html        # Live sandbox preview
└── README.md                       # This file
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

---

## Website Integration Guide

To embed **AlphaBot** as a floating chat bubble in the bottom-right corner of any web page:

1. Copy the integration script from [`embed_code.html`](./embed_code.html)
2. Paste it right before the closing `</body>` tag on your host website
3. The chatbot will appear as a floating widget

**Live Sandbox Preview:**
A live sandbox preview demonstrating the chatbot integrated on top of the official CodeAlpha website is available locally in [`codealpha_tech_demo.html`](./codealpha_tech_demo.html). Open this file in your browser to see a working demo.

---

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main chatbot interface |
| `/chat` | POST | Send message to chatbot & receive AI response |
| `/history` | GET | Retrieve conversation cache |
| `/tickets` | GET | Fetch all submitted tickets from database |
| `/clear` | POST | Clear chat history & reset to default state |

---

## DB Schema: `tickets`

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | TEXT (Primary Key) | Unique ticket reference (e.g. `CA-4184`) |
| `email` | TEXT | Student email address |
| `domain` | TEXT | Selected technical track |
| `message` | TEXT | Student cover note / inquiry details |
| `timestamp` | TEXT | Submission date & time (ISO 8601 format) |

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| **Port 5002 already in use** | Change the port in `app.py` or kill the existing process: `lsof -ti:5002 \| xargs kill -9` |
| **SQLite database locked** | Restart the Flask server: `python app.py` |
| **TTS (Text-to-Speech) not working** | Verify browser compatibility (Chrome, Firefox, Safari supported). Check system audio settings. |
| **Chat history not persisting** | Ensure `localStorage` is enabled in browser settings. Check browser console for errors. |
| **Chatbot not responding** | Verify Flask server is running. Check `app.py` logs for backend errors. |
| **Static files not loading (CSS/JS)** | Ensure the `static/` directory exists with correct file structure. Hard-refresh browser (Ctrl+Shift+R). |

---

## Contributing

We welcome contributions! To get started:

1. **Fork the repository**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_Chatbot.git
   ```

2. **Create a feature branch**
   ```bash
   git checkout -b feature/awesome-feature
   ```

3. **Make your changes & test locally**
   ```bash
   python app.py
   ```

4. **Commit with clear messages**
   ```bash
   git commit -m 'Add awesome feature: describe what you added'
   ```

5. **Push to your branch**
   ```bash
   git push origin feature/awesome-feature
   ```

6. **Open a Pull Request**
   - Provide a clear description of changes
   - Reference any related issues

---

## License

This project is licensed under the MIT License — see the [LICENSE](./LICENSE) file for details.

---

## Contact

For questions, feedback, or collaboration opportunities:

- **Email:** [sweta113sharma@example.com](mailto:sweta113sharma@example.com)
- **GitHub:** [@Sweta113Sharma](https://github.com/Sweta113Sharma)
- **CodeAlpha:** [CodeAlpha Virtual Internship](https://codealpha.tech)

---

**Built with ❤️ for the CodeAlpha community**
