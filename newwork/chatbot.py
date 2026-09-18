import os
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
load_dotenv(Path(__file__).parent / ".env")
load_dotenv(Path(__file__).parent.parent / ".env")

# Streamlit Page Config
st.set_page_config(
    page_title="Generative AI ChatBot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for modern styling
st.markdown("""
<style>
    .chat-header {
        display: flex;
        align-items: center;
        gap: 12px;
        margin-bottom: 8px;
    }
    .model-badge {
        background-color: rgba(59, 130, 246, 0.15);
        color: #3b82f6;
        padding: 4px 10px;
        border-radius: 9999px;
        font-size: 0.82rem;
        font-weight: 600;
        display: inline-block;
        margin-bottom: 12px;
    }
    .suggestion-card {
        padding: 12px;
        border-radius: 8px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        cursor: pointer;
    }
    .stat-box {
        background-color: rgba(255, 255, 255, 0.04);
        border-radius: 8px;
        padding: 8px 12px;
        text-align: center;
    }
</style>
""", unsafe_allow_html=True)

# Initialize Session States
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

if "pending_prompt" not in st.session_state:
    st.session_state.pending_prompt = None

# Sidebar Configuration
with st.sidebar:
    st.markdown("## 🤖 Bot Settings")
    st.markdown("---")

    # Model Selection
    MODEL_OPTIONS = {
        "OpenAI GPT-OSS 20B (Fast Reasoning)": "openai/gpt-oss-20b",
        "OpenAI GPT-OSS 120B (Deep Reasoning)": "openai/gpt-oss-120b",
        "Qwen 3.8 27B (High Capability)": "qwen/qwen3.8-27b",
        "Qwen 3.6 27B": "qwen/qwen3.6-27b",
        "Groq Compound": "groq/compound",
        "Groq Compound Mini (Ultra Fast)": "groq/compound-mini"
    }

    selected_model_label = st.selectbox(
        "🧠 Model",
        options=list(MODEL_OPTIONS.keys()),
        index=0,
        help="Select the AI model powered by Groq's high-speed inference engine."
    )
    selected_model = MODEL_OPTIONS[selected_model_label]

    # Persona / System Prompt Presets
    PERSONAS = {
        "🤖 Helpful Assistant": "You are a helpful, knowledgeable, and polite AI assistant.",
        "💻 Software Engineer": "You are an expert full-stack software engineer and architect. Provide clean, secure, idiomatic, well-commented code and thorough explanations.",
        "🎓 Patient Tutor": "You are an encouraging, friendly tutor. Explain complex concepts simply with intuitive analogies, examples, and step-by-step guidance.",
        "⚡ Direct & Concise": "Be extremely concise, direct, and factual. Avoid pleasantries, filler, or unnecessary preamble.",
        "✍️ Creative Writer": "You are an imaginative storyteller, copywriter, and creative writing assistant.",
        "🛠️ Custom Persona": "CUSTOM"
    }

    selected_persona = st.selectbox(
        "🎭 Persona",
        options=list(PERSONAS.keys()),
        index=0,
        help="Choose the assistant's personality and tone."
    )

    if selected_persona == "🛠️ Custom Persona":
        system_prompt = st.text_area(
            "Custom System Prompt",
            value="You are a helpful assistant.",
            height=90,
            help="Define your own custom instructions for the model."
        )
    else:
        system_prompt = PERSONAS[selected_persona]

    # Advanced Model Hyperparameters
    with st.expander("⚙️ Advanced Parameters", expanded=False):
        temperature = st.slider(
            "Temperature",
            min_value=0.0,
            max_value=1.5,
            value=0.5,
            step=0.1,
            help="Lower values make output more deterministic; higher values make it more creative."
        )
        max_tokens = st.slider(
            "Max Tokens",
            min_value=256,
            max_value=8192,
            value=2048,
            step=256,
            help="Maximum number of tokens the model can generate per response."
        )

    # API Key Configuration
    with st.expander("🔑 API Key Settings", expanded=False):
        env_key = os.getenv("GROQ_API_KEY") or os.getenv("API_KEY") or ""
        custom_key = st.text_input(
            "Groq API Key",
            value=env_key,
            type="password",
            help="Enter your Groq API key (starts with gsk_)."
        )
        api_key = custom_key.strip() if custom_key.strip() else env_key
        if api_key:
            st.success("API Key configured! ✅")
        else:
            st.error("No API Key detected! ❌")

    st.markdown("---")

    # Conversation Statistics & Controls
    col_stat1, col_stat2 = st.columns(2)
    with col_stat1:
        st.metric("Messages", len(st.session_state.chat_history))
    with col_stat2:
        user_msgs = sum(1 for m in st.session_state.chat_history if m["role"] == "user")
        st.metric("Questions", user_msgs)

    # Clear Chat Button
    if st.button("🗑️ Clear Chat", use_container_width=True, type="secondary"):
        st.session_state.chat_history = []
        st.session_state.pending_prompt = None
        st.rerun()

    # Export Chat Button
    if st.session_state.chat_history:
        def generate_markdown_transcript():
            content = f"# Generative AI ChatBot Transcript\n\n"
            content += f"- **Model**: `{selected_model}`\n"
            content += f"- **Persona**: {selected_persona}\n\n---\n\n"
            for msg in st.session_state.chat_history:
                role = "User 👤" if msg["role"] == "user" else "Assistant 🤖"
                content += f"### {role}\n\n"
                if msg.get("reasoning"):
                    content += f"<details><summary>Thought Process</summary>\n\n{msg['reasoning']}\n\n</details>\n\n"
                content += f"{msg['content']}\n\n---\n\n"
            return content

        st.download_button(
            label="📥 Export Chat (.md)",
            data=generate_markdown_transcript(),
            file_name="chat_history.md",
            mime="text/markdown",
            use_container_width=True
        )

# Main UI Header
st.title("🤖 Generative AI ChatBot")
st.markdown(f"<div class='model-badge'>Active Model: {selected_model}</div>", unsafe_allow_html=True)

# Stop execution if API key is missing
if not api_key:
    st.warning("⚠️ Please provide a Groq API Key in the sidebar or set `GROQ_API_KEY` in your `.env` file to start chatting.")
    st.stop()

# Initialize LLM
try:
    llm = ChatGroq(
        model=selected_model,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens
    )
except Exception as e:
    st.error(f"Error initializing ChatGroq: {e}")
    st.stop()

# Starter Prompts when conversation is empty
if len(st.session_state.chat_history) == 0:
    st.markdown("👋 **Welcome! What would you like to explore today?**")
    st.markdown("##### 💡 Example Prompts:")
    col1, col2 = st.columns(2)
    starter_prompts = [
        ("🧠 Explain Quantum Computing", "Explain quantum computing in simple terms with an everyday analogy."),
        ("💻 Write a Python API with FastAPI", "Show me how to build a clean REST API using FastAPI with validation."),
        ("✉️ Draft a Professional Email", "Draft a polite and concise email requesting a project deadline extension."),
        ("🔍 Code Review & Optimization", "How can I optimize slow database queries and avoid the N+1 problem in web apps?")
    ]

    for idx, (label, prompt_text) in enumerate(starter_prompts):
        target_col = col1 if idx % 2 == 0 else col2
        if target_col.button(label, use_container_width=True, key=f"sugg_{idx}"):
            st.session_state.pending_prompt = prompt_text
            st.rerun()

# Display Conversation History
for message in st.session_state.chat_history:
    avatar = "👤" if message["role"] == "user" else "🤖"
    with st.chat_message(message["role"], avatar=avatar):
        # Show collapsible reasoning if available
        if message.get("reasoning"):
            with st.expander("💭 Thought Process", expanded=False):
                st.markdown(message["reasoning"])
        st.markdown(message["content"])

# Handle User Input (via chat input or suggestion button)
user_prompt = st.chat_input("Ask Chatbot anything...")
if not user_prompt and st.session_state.get("pending_prompt"):
    user_prompt = st.session_state.pop("pending_prompt")

if user_prompt:
    # Render and store user message
    with st.chat_message("user", avatar="👤"):
        st.markdown(user_prompt)
    st.session_state.chat_history.append({"role": "user", "content": user_prompt})

    # Prepare message context with system prompt and history
    messages = [
        {"role": "system", "content": system_prompt},
        *[
            {"role": m["role"], "content": m["content"]}
            for m in st.session_state.chat_history
        ]
    ]

    # Stream assistant response
    with st.chat_message("assistant", avatar="🤖"):
        reasoning_expander = None
        reasoning_box = None
        reasoning_text = ""
        full_content = ""
        message_placeholder = st.empty()

        try:
            for chunk in llm.stream(messages):
                # Capture reasoning content for models that support it (e.g. gpt-oss-20b)
                r_chunk = chunk.additional_kwargs.get("reasoning_content")
                if r_chunk:
                    reasoning_text += r_chunk
                    if reasoning_expander is None:
                        reasoning_expander = st.expander("💭 Thought Process", expanded=False)
                        reasoning_box = reasoning_expander.empty()
                    reasoning_box.markdown(reasoning_text)

                # Stream response content
                if chunk.content:
                    full_content += chunk.content
                    message_placeholder.markdown(full_content + "▌")

            # Final render without streaming cursor
            message_placeholder.markdown(full_content)

            # Store in session state
            st.session_state.chat_history.append({
                "role": "assistant",
                "content": full_content,
                "reasoning": reasoning_text if reasoning_text else None
            })

        except Exception as e:
            message_placeholder.empty()
            st.error(f"⚠️ Error generating response: {e}")
