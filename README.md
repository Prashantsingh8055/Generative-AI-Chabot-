# Generative AI ChatBot 🤖

A sleek, interactive AI chat application built with Python, Streamlit, and Groq-powered language models. This project lets you chat with multiple models, switch conversational personas, fine-tune generation settings, and export conversations in a clean Markdown format.

<p align="center">
  <img src="https://github.com/user-attachments/assets/0c127eee-73db-4db5-ba74-d43d5f1d61ae" alt="Generative AI ChatBot Dashboard" width="100%" />
</p>

## ✨ Highlights

- Multi-model support via Groq-powered AI models
- Real-time streaming responses in the chat UI
- Persona-based assistant behavior (Helpful Assistant, Tutor, Engineer, Writer, etc.)
- Adjustable temperature and max token controls
- Sidebar configuration for API key management
- Conversation history with export to Markdown
- Simple, clean interface powered by Streamlit

## 🧠 Supported Models

The app includes a range of model presets such as:

- OpenAI GPT-OSS 20B (Fast Reasoning)
- OpenAI GPT-OSS 120B (Deep Reasoning)
- Qwen 3.8 27B (High Capability)
- Qwen 3.6 27B
- Groq Compound
- Groq Compound Mini (Ultra Fast)

## 🏗️ Tech Stack

- Python 3.13
- Streamlit
- LangChain Groq
- Python-dotenv
- Groq API

## 📁 Project Structure

```text
Generative-AI-Chabot-
├── README.md
├── pyproject.toml
├── requirement.txt
├── uv.lock
├── .env.example (if added locally)
├── newwork/
│   └── chatbot.py
├── src/
│   └── new_folder/
│       └── __init__.py
└── .gitignore
```

## 🚀 Getting Started

### 1) Clone the repository

```bash
git clone https://github.com/Prashantsingh8055/Generative-AI-Chabot-.git
cd Generative-AI-Chabot-
```

### 2) Create a virtual environment

```bash
python -m venv .venv
source .venv/bin/activate   # Linux/macOS
.venv\Scripts\activate      # Windows
```

### 3) Install dependencies

Using pip:

```bash
pip install -r requirement.txt
```

Or with uv:

```bash
uv sync
```

### 4) Add your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

You may also provide the key directly in the sidebar within the app.

### 5) Run the application

```bash
streamlit run newwork/chatbot.py
```

Once started, the app opens in your browser and you're ready to chat.

## 🎯 Core Features

### Conversational AI Experience
The chatbot supports dynamic conversations with streaming text generation for a responsive user experience.

### Persona Customization
Choose from predefined personas or define your own custom instructions to shape the assistant's behavior.

### Parameter Tuning
Customize:

- Temperature
- Max Tokens
- Model selection

### Chat Export
Export your full conversation transcript as a Markdown file for saving or sharing.

## 🧪 Example Use Cases

- Ask coding questions and get explanations
- Draft professional emails and messages
- Generate technical documentation and summaries
- Learn complex topics with a patient tutoring tone
- Prototype ideas using different AI personas

## 🔒 Environment Variables

| Variable | Description |
| --- | --- |
| `GROQ_API_KEY` | Your API key for accessing Groq models |
| `API_KEY` | Alternative fallback key name supported by the app |

## 📦 Dependency Overview

This app depends on:

- `streamlit` for the frontend UI
- `langchain-groq` to integrate Groq models
- `python-dotenv` to load environment variables

## 📌 Notes

This project is a polished chatbot demo designed for experimentation, learning, and practical AI-powered conversations. It is highly customizable and can be extended with features like:

- chat memory persistence
- user authentication
- database-backed conversation history
- document Q&A support
- multi-agent workflows

## 🤝 Contributing

Contributions, suggestions, and enhancements are welcome. If you want to improve the UI, add features, or optimize the chatbot experience, feel free to open an issue or submit a pull request.

## 📜 License

This project is currently distributed without a formal license file. If you plan to use it for production or distribution, consider adding an appropriate open-source license.

---

Built with passion for AI, conversation design, and modern Python applications.
