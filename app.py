from pydantic import BaseModel, Field
import subprocess

import streamlit as st

import ollama
from ollama import ChatResponse

MODEL = 'qwen3_4b_32k' # Type "ollama list" in terminal to see available models

class PythonScript(BaseModel):
    script: str = Field(description="The Python script to be executed.")
    comments: str = Field(description="Any additional notes or comments about the script.")
    external_libraries: list[str] = Field(description="List of external libraries used in the script.")


class LLM:
    def __init__(self, system_message: str, model: str = MODEL):
        self.system_message = system_message
        self.messages = [
            {"role": "system", "content": system_message}
        ]
        self.model = model

    def generate(self, message: str, format: str) -> ChatResponse:
        """
        Generate a chat response using the Ollama model.

        This method appends the user message to the conversation history, sends it to the
        Ollama chat model, and appends the assistant's response back to the history.

        Args:
            message (str): The user's input message to send to the chat model.
            format (str): The desired format for the response output.

        Returns:
            ChatResponse: The complete response object from the Ollama chat model,
                         containing the assistant's reply and metadata.

        Note:
            The method uses a low temperature (0.1) for more deterministic responses
            and automatically maintains conversation history in self.messages.
        """
        self.messages.append({"role": "user", "content": message})
        response: ChatResponse = ollama.chat(
            model=self.model,
            messages=self.messages,
            format=format,
            options={'temperature': 0.1}
        )
        self.messages.append({"role": "assistant", "content": response.message.content})
        return response


# Initialize chat history in session state
if 'chat_history' not in st.session_state:
    st.session_state.chat_history = []
if 'current_code' not in st.session_state:
    st.session_state.current_code = None
if 'current_comments' not in st.session_state:
    st.session_state.current_comments = None
if 'current_libraries' not in st.session_state:
    st.session_state.current_libraries = []

st.title("Python Script Generator Chat")

# Display chat history
for i, (role, message) in enumerate(st.session_state.chat_history):
    if role == 'user':
        st.chat_message("user").write(message)
    else:
        st.chat_message("assistant").write(message)

user_input = st.chat_input("Describe what you want help doing or give feedback on the script")

if user_input:
    st.session_state.chat_history.append(('user', user_input))
    st.chat_message("user").write(user_input)
    # Build system message and conversation context
    system_message = """
    You are a Python coder. Your task is to construct a Python script based on the user's input and feedback.
    The script should be in a form of a Streamlit app, so make use of the Streamlit library for user interface elements. 
    Example: If a user want to upload a file, user st.file_uploader. If the user wants to input text, use st.text_input. Etc.
    **IMPORTANT! The user can not change anything in the script, only interact with it via Streamlit UI elements.** 
    Therefore, don't user placeholders like "your_file" or "your_text". Instead, use Streamlit UI elements to get the input from the user.
    If the user gives feedback, improve the previous script accordingly.
    """
    # Build conversation context
    conversation = "\n".join([
        f"User: {msg}" if role == 'user' else f"Assistant: {msg}"
        for role, msg in st.session_state.chat_history
    ])
    llm = LLM(system_message=system_message)
    response = llm.generate(conversation, format=PythonScript.model_json_schema())
    answer = PythonScript.model_validate_json(response.message.content)
    code = answer.script
    comments = answer.comments
    libraries = answer.external_libraries
    st.session_state.current_code = code
    st.session_state.current_comments = comments
    st.session_state.current_libraries = libraries
    st.session_state.chat_history.append(('assistant', comments + "\n\n" + code))
    st.chat_message("assistant").write(comments)
    st.code(code, language='python')
    for library in libraries:
        try:
            __import__(library)
        except ImportError:
            st.write(f"Installing {library}...")
            subprocess.check_call(["pip", "install", library])
    with open("pages/user_app.py", "w") as f:
        f.write(code)

elif st.session_state.current_code:
    st.chat_message("assistant").write(st.session_state.current_comments)
    with st.expander("View the code"):
        st.code(st.session_state.current_code, language='python')
