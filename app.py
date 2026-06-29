from flask import Flask, render_template, request, jsonify
import random, re, sqlite3
from datetime import datetime

app = Flask(__name__)

# SQLite Database Setup
DB_FILE = "codealpha_chatbot.db"

def init_db():
    conn = sqlite3.connect(DB_FILE)
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS tickets (
            id TEXT PRIMARY KEY,
            email TEXT NOT NULL,
            domain TEXT NOT NULL,
            message TEXT NOT NULL,
            timestamp TEXT NOT NULL
        )
    """)
    conn.commit()
    conn.close()

# Initialize Database on startup
init_db()

# ─── RETRIEVAL-BASED CHATBOT (Pattern Matching + Response Bank) ───
RESPONSES = {
    "greeting": {
        "patterns": [r"\b(hello|hi|hey|howdy|greetings|good morning|good evening|good afternoon)\b"],
        "responses": [
            "Hello! Welcome to CodeAlpha. 👋 I'm **AlphaBot**, your AI assistant. How can I help you today?",
            "Hi there! Nice to meet you. What can I assist you with regarding CodeAlpha and our technology tracks?",
            "Hey! Hope you're having a great day. I'm ready to answer any questions about our internships, cloud, or AI tracks!"
        ]
    },
    "goodbye": {
        "patterns": [r"\b(bye|goodbye|see you|take care|farewell|exit|quit)\b"],
        "responses": [
            "Goodbye! Have an amazing day! 😊 Feel free to chat with me anytime you have questions about CodeAlpha.",
            "See you later! Keep building and learning! 🚀",
            "Take care! Hope I was helpful. Goodbye!"
        ]
    },
    "name": {
        "patterns": [r"\b(your name|who are you|what are you|introduce yourself)\b"],
        "responses": [
            "I'm **AlphaBot** 🤖, the official AI assistant for CodeAlpha! I help students and clients understand our programs and technology topics.",
            "My name is **AlphaBot** ✦. I was trained to help you navigate CodeAlpha's services, internships, and educational tracks."
        ]
    },
    "help": {
        "patterns": [r"\b(help|support|assist|what can you do|capabilities|features|help me)\b"],
        "responses": [
            "I am here to guide you! 💡 Here is what I can assist you with:\n• 🏢 **CodeAlpha Internships:** domains, application process, and certificate requirements.\n• ☁️ **Cloud Computing:** services, AWS, Azure, GCP, and Cloud architectures.\n• 🧠 **AI & ML:** artificial intelligence concepts, machine learning, and chatbot structures.\n• 🐍 **Python & Coding:** Flask, Django, SQL databases, and general programming inquiries.\n\nYou can also click the shortcut cards on the dashboard or type any question below!"
        ]
    },
    "codealpha": {
        "patterns": [r"\b(codealpha|code alpha|internship|company|register|apply|join|tracks|domains)\b"],
        "responses": [
            "**CodeAlpha** is a premier software development and technical training organization. We host fully virtual, 1-month internship programs in high-demand tracks:\n• ☁️ **Cloud Computing**\n• 🧠 **Artificial Intelligence & Machine Learning**\n• 💻 **Web Development**\n• 📱 **Mobile App Development**\n• 🔒 **Cyber Security**\n\nWould you like to register or submit an inquiry? You can apply directly using our inline form by clicking **Apply/Register** on the welcome dashboard!",
            "At CodeAlpha, internships are designed to give students practical, hands-on project experience. Upon successful submission of task projects, you are awarded an **Internship Completion Certificate** and a **Recommendation Letter**. 🎓 Let me know if you'd like to apply!"
        ]
    },
    "cloud": {
        "patterns": [r"\b(cloud|aws|azure|google cloud|gcp|ec2|s3|lambda|serverless)\b"],
        "responses": [
            "Cloud computing offers scalability and on-demand delivery of compute power, storage, and databases over the internet. CodeAlpha provides internships focusing on major providers:\n• ☁️ **AWS** (Amazon Web Services): EC2, S3, RDS, and Lambda.\n• ☁️ **Azure** (Microsoft): Virtual Machines, Blob Storage, and Functions.\n• ☁️ **GCP** (Google Cloud Platform): Compute Engine, Cloud Storage.\n\nLearning cloud skills is essential for modern software engineering! 🚀",
            "Interested in cloud architectures? Some key concepts include serverless computing (AWS Lambda, Azure Functions), containerization (Docker, Kubernetes), and infrastructure as code. Let me know if you want to know about CodeAlpha's cloud tasks!"
        ]
    },
    "python": {
        "patterns": [r"\b(python|flask|django|fastapi|pip)\b"],
        "responses": [
            "Python is a versatile language highly favored in Web Development, AI, Data Science, and Cloud Automation. 🐍 Popular web frameworks include:\n• ⚡ **Flask:** Lightweight, modular, and great for microservices and REST APIs.\n• 🧱 **Django:** Full-featured, secure, and follows the \"batteries-included\" philosophy.\n\nCodeAlpha python tasks give you practical experience building real-world APIs and dashboards!",
            "Flask is the framework powering this very chatbot! It is simple to get started with and highly flexible. Python's rich library ecosystem is what makes it a powerhouse for developer workflows."
        ]
    },
    "ai": {
        "patterns": [r"\b(artificial intelligence|machine learning|ai|ml|deep learning|neural|gpt|llm)\b"],
        "responses": [
            "Artificial Intelligence (AI) and Machine Learning (ML) are transforming businesses! 🧠 Key chatbot approaches:\n• **Retrieval-based:** Matches user query patterns to predefined templates (fast, predictable, like me!).\n• **Generative:** Uses LLMs (like GPT) to generate text on the fly.\n\nCodeAlpha AI internships cover building model classification systems, regression analyses, and custom chatbots!",
            "Deep Learning uses artificial neural networks to solve highly complex tasks like image classification and natural language understanding. It is a subset of Machine Learning."
        ]
    },
    "sql": {
        "patterns": [r"\b(sql|database|mysql|postgresql|sqlite|query)\b"],
        "responses": [
            "SQL (Structured Query Language) is the industry standard for managing relational databases. Databases like MySQL, PostgreSQL, and SQLite are widely used in enterprise cloud applications. 🗄️",
            "Database security is vital! Make sure to prevent **SQL Injection** by using parameterized queries/prepared statements and sanitizing all user inputs before database processing."
        ]
    },
    "weather": {
        "patterns": [r"\b(weather|temperature|rain|sunny|forecast|climate)\b"],
        "responses": [
            "I'm currently running offline without direct weather API integration, but you can check a weather provider like weather.com or your default phone assistant for live local reports! 🌤️",
            "I don't have access to real-time weather sensors, but the sun is always shining in the world of code! ☀️"
        ]
    },
    "time": {
        "patterns": [r"\b(time|date|today|current time|what day)\b"],
        "responses": [
            f"The current date is **{datetime.now().strftime('%B %d, %Y')}** 📅",
            f"Today is **{datetime.now().strftime('%A, %B %d, %Y')}** 🗓️"
        ]
    },
    "thanks": {
        "patterns": [r"\b(thanks|thank you|thank|thx|appreciate)\b"],
        "responses": [
            "You are very welcome! 😊 Glad I could assist you. Let me know if you have other CodeAlpha questions!",
            "Anytime! I'm here to help. Good luck with your tech journey! 👍",
            "My pleasure! 🎉 Happy coding!"
        ]
    },
    "joke": {
        "patterns": [r"\b(joke|funny|laugh|humor|comedy)\b"],
        "responses": [
            "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂",
            "Why was the SQL query running slowly? It had too many JOINS! 😅",
            "How many programmers does it take to change a light bulb? None — that's a hardware problem! 💡💻"
        ]
    },
    "default": {
        "patterns": [],
        "responses": [
            "I'm not sure I fully understand. Could you rephrase your question? 🤔 You can ask about our cloud, AI, Python, or Web Dev internship tracks!",
            "I'm still training my database! If you want to connect with a representative or apply for an internship, try clicking **Apply/Register** on the welcome dashboard. 📋",
            "Hmm, I don't have a direct answer for that. Try asking about cloud computing, artificial intelligence, SQL security, or CodeAlpha company tracks!"
        ]
    }
}

def get_response(user_input: str) -> str:
    user_input_lower = user_input.lower().strip()
    for intent, data in RESPONSES.items():
        if intent == "default": continue
        for pattern in data["patterns"]:
            if re.search(pattern, user_input_lower, re.IGNORECASE):
                return random.choice(data["responses"])
    return random.choice(RESPONSES["default"]["responses"])

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "").strip()
    if not user_msg:
        return jsonify({"response": "Please say something! 😊"})
    bot_reply = get_response(user_msg)
    return jsonify({"response": bot_reply, "timestamp": datetime.now().strftime("%H:%M")})

@app.route("/submit_ticket", methods=["POST"])
def submit_ticket():
    data = request.json
    email = data.get("email", "").strip()
    domain = data.get("domain", "").strip()
    message = data.get("message", "").strip()
    if not email or not message:
        return jsonify({"success": False, "error": "Email and inquiry message are required."}), 400
    
    ticket_id = f"CA-{random.randint(1000, 9999)}"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    try:
        conn = sqlite3.connect(DB_FILE)
        c = conn.cursor()
        c.execute("INSERT INTO tickets (id, email, domain, message, timestamp) VALUES (?, ?, ?, ?, ?)",
                  (ticket_id, email, domain, message, timestamp))
        conn.commit()
        conn.close()
        
        ticket = {
            "id": ticket_id,
            "email": email,
            "domain": domain,
            "message": message,
            "timestamp": timestamp
        }
        print(f"New Ticket Logged to Database: {ticket}")
        return jsonify({"success": True, "ticket": ticket})
    except Exception as e:
        print(f"Database Error: {e}")
        return jsonify({"success": False, "error": "Could not log inquiry to database."}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5002)
