# gemini_clone
# 🤖 Gemini Chat Clone

A sleek, minimal chat interface powered by **Google's Gemini 1.5 Flash model**, built with **Streamlit** and **LangChain**. This clone provides a real-time chat experience where users can interact conversationally with an advanced language model.

---

## 🚀 Features

* 💬 Conversational memory with chat history
* ⚡ Real-time responses from Gemini LLM
* 🧠 Built using LangChain for modularity
* 🌐 Clean and responsive UI with Streamlit
* 🔐 Environment variable support for API security

---

## 📦 Tech Stack

| Tool / Library          | Purpose                                    |
| ----------------------- | ------------------------------------------ |
| Python                  | Core programming language                  |
| Streamlit               | UI for the chat interface                  |
| LangChain               | Prompt management and conversation history |
| Google Gemini 1.5 Flash | Underlying LLM engine                      |
| python-dotenv           | API key management                         |

---

## 🛠️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/gemini-chat-clone.git
cd gemini-chat-clone
```

### 2. Create a `.env` File

```env
GOOGLE_API_KEY=your_google_api_key_here
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit App

```bash
streamlit run app.py
```

---

## 🧪 Sample Prompt

**User:**

> What's the capital of Japan?

**Gemini:**

> The capital of Japan is Tokyo.

---

## 📌 Notes

* Make sure your Google API key has access to the Gemini 1.5 Flash model.
* This app supports multi-turn conversations and maintains history using `st.session_state`.

---

## 🤝 Contributions

Pull requests, suggestions, and bug reports are welcome!

---

## 📄 License

MIT License

---

Enjoy chatting with Gemini! 🌟
