import streamlit as st
from supabase import Client, create_client
import os
from dotenv import load_dotenv

load_dotenv()

# Show title and description.
st.title("💬 Chatbot")
st.write(
    "Noto Lola AI woof woof"
)

def get_supabase_client() -> Client:
    """
    Create and cache Supabase client instance
    Uses Streamlit's cache to avoid recreating the client on every rerun
    """
    supabase_url = os.environ.get("SUPABASE_PROJECT_URL")
    supabase_key = os.environ.get("SUPABASE_API_KEY")
    
    if not supabase_url or not supabase_key:
        raise ValueError(
            "Missing Supabase credentials. "
            "Please set SUPABASE_URL and SUPABASE_KEY environment variables."
        )
    
    return create_client(supabase_url, supabase_key)


        
def get_user_dogs(supabase: Client ):
    """
    Fetch all dogs for a specific user
    """
    response = supabase.table("dogs").select("*").execute()
    return response.data

# Ask user for their OpenAI API key via `st.text_input`.
# Alternatively, you can store the API key in `./.streamlit/secrets.toml` and access it
# via `st.secrets`, see https://docs.streamlit.io/develop/concepts/connections/secrets-management
user_name = st.text_input("Username")

print( get_user_dogs( get_supabase_client() ) )
# openai_api_key = st.text_input("OpenAI API Key", type="password")
if not user_name:
    st.info("Please add your OpenAI API key to continue.")
    
else:
#     # Create an OpenAI client.
#     client = OpenAI(api_key=openai_api_key)

#     # Create a session state variable to store the chat messages. This ensures that the
#     # messages persist across reruns.
    if "messages" not in st.session_state:
        st.session_state.messages = []

     # Display the existing chat messages via `st.chat_message`.
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

     # Create a chat input field to allow the user to enter a message. This will display
     # automatically at the bottom of the page.
    if prompt := st.chat_input("What is up?"):

        # Store and display the current prompt.
        st.session_state.messages.append({"role": "user", "content": user_name + ": " + prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

#         # Generate a response using the OpenAI API.
#         stream = client.chat.completions.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 {"role": m["role"], "content": m["content"]}
#                 for m in st.session_state.messages
#             ],
#             stream=True,
#         )

#         # Stream the response to the chat using `st.write_stream`, then store it in 
#         # session state.
#         with st.chat_message("assistant"):
#             response = st.write_stream(stream)
#         st.session_state.messages.append({"role": "assistant", "content": response})
