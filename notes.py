import streamlit as st
import random
import string

# Function to generate a unique key
def generate_unique_key(length=8):
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(length))

# Initialize session state if it's not already initialized
if 'notes' not in st.session_state:
    st.session_state['notes'] = {}

# Sidebar for navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Select a Page", ("Sender", "Receiver"))

# Sender page
if page == "Sender":
    st.title('Create a Secret Note')
    note_content = st.text_area("Enter your secret note here:")
    if st.button('Generate Key & Save Note'):
        if note_content:
            unique_key = generate_unique_key()
            st.session_state['notes'][unique_key] = note_content
            st.success(f'Note saved! Key: **{unique_key}**')
            st.text('Share this key with the recipient to access the note.')
        else:
            st.warning('Please enter a note before saving.')

# Receiver page
elif page == "Receiver":
    st.title('Retrieve Your Secret Note')
    input_key = st.text_input("Enter the unique key to retrieve your note:")
    if st.button('View Note'):
        if input_key in st.session_state['notes']:
            note = st.session_state['notes'][input_key]
            st.write("Your secret note:")
            st.write(note)

            # Delete the note after viewing
            del st.session_state['notes'][input_key]
            st.success('Note has been deleted after viewing.')
        else:
            st.warning('Invalid key. Please check and try again.')