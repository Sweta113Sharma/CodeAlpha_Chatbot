# AlphaBot ✦ — CodeAlpha AI Chatbot Redesign

**AlphaBot** is a highly professional, human-friendly, retrieval-based chatbot designed to integrate seamlessly as a customer support assistant for **CodeAlpha** virtual internship programs. 

Featuring a modern, minimal wabi-sabi aesthetic (white, beige, black, and brown), it provides instant, empathetic responses regarding internship tracks, certification rules, and technical topics, backed by persistent SQLite storage and voice-synthesis narration.

---

##  Features

- **Minimal Beige Theme:** Designed with a warm, minimalist palette (white, beige, charcoal, and warm brown) utilizing premium modern typography (`Outfit` & `Plus Jakarta Sans`) and glassmorphic card overlays.
- **Persistent SQLite Database:** Refactored backend ticket routing to persistently log student application submissions and inquiries inside `codealpha_chatbot.db`.
- **Conversation Cache Persistence:** Serializes messaging history to the browser's `localStorage` so users never lose their conversation threads on page reload.
- **Clean History Utilities:** Clear chat logs instantly and restore the default dashboard directly from the trash launcher in the header.
- **Text-to-Speech (TTS) Voice Narration:** Listen to bot replies spoken aloud with a native Web Speech API (`window.speechSynthesis`) toggle wrapper.
- **Click-to-Copy Actions:** Copy messages cleanly to your clipboard using custom action buttons under each response card.
- **Floating Launcher Embed Script:** Integrates as a floating widget on any host website layout via an `<iframe>` launcher overlay.

---

## Technology Stack

- **Backend:** Flask (Python 3.x), SQLite3
- **Frontend:** Vanilla JavaScript, Modern CSS, HTML5 semantic layout
- **Narration:** Web Speech API (`SpeechSynthesisUtterance`)
- **Branding Assets:** Google Fonts, FontAwesome 6

---

## Installation & Local Running

1. **Clone the repository:**
   ```bash
   git clone https://github.com/YOUR_USERNAME/CodeAlpha_Chatbot.git
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

---

## Website Integration Guide

To embed **AlphaBot** as a floating chat bubble in the bottom-right corner of any web page, paste the integration script inside [`embed_code.html`](./embed_code.html) right before the closing `</body>` tag of your site code.

A live sandbox preview demonstrating the chatbot integrated on top of the official CodeAlpha website is available locally in [`codealpha_tech_demo.html`](./codealpha_tech_demo.html).

---

## DB Schema: `tickets`

| Field | Type | Description |
| :--- | :--- | :--- |
| `id` | TEXT (Primary Key) | Unique ticket reference (e.g. `CA-4184`) |
| `email` | TEXT | Student email address |
| `domain` | TEXT | Selected technical track |
| `message` | TEXT | Student cover note / inquiry details |
| `timestamp` | TEXT | Submission date & time |
