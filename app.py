import streamlit as st
from poetry_data import poetry_data  # Import poetry data from the separate file

# Set page configuration
st.set_page_config(page_title="MY library", page_icon=":writing_hand:", layout="wide")

# Custom CSS for aesthetic design, animations, and effects
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap');

    body {
        background: linear-gradient(135deg, #f4f1de, #f2cc8f);
        color: #3d405b;
        font-family: 'Roboto', sans-serif;
    }
    h1, h2, h3, h4, h5, h6 {
        font-family: 'Playfair Display', serif;
        color: #3d405b;
    }
    .header-section {
        background-image: url('https://images.unsplash.com/photo-1507842217343-583bb7270b66?ixlib=rb-1.2.1&auto=format&fit=crop&w=1953&q=80');
        background-size: cover;
        background-position: center;
        padding: 100px 20px;
        text-align: center;
        color: white;
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .header-section h1 {
        font-size: 48px;
        animation: fadeInDown 1.5s ease-in-out;
    }
    .header-section p {
        font-size: 20px;
        animation: fadeInUp 1.5s ease-in-out;
    }
    @keyframes fadeInDown {
        from { opacity: 0; transform: translateY(-50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    @keyframes fadeInUp {
        from { opacity: 0; transform: translateY(50px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .stButton button {
        background-color: #81b29a;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease;
    }
    .stButton button:hover {
        background-color: #e07a5f;
    }
    .stTextInput input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #81b29a;
    }
    .stMarkdown {
        font-size: 18px;
        line-height: 1.6;
    }
    .poetry-title {
        font-size: 22px;
        font-weight: bold;
        color: #e07a5f;
        cursor: pointer;
        transition: color 0.3s ease;
    }
    .poetry-title:hover {
        color: #3d405b;
    }
    .full-poetry {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in-out;
    }
    @keyframes fadeIn {
        from { opacity: 0; transform: translateY(20px); }
        to { opacity: 1; transform: translateY(0); }
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .typewriter {
        overflow: hidden;
        border-right: 0.15em solid #e07a5f;
        white-space: nowrap;
        margin: 0 auto;
        letter-spacing: 0.15em;
        animation: typing 3.5s steps(40, end), blink-caret 0.75s step-end infinite;
    }
    @keyframes typing {
        from { width: 0; }
        to { width: 100%; }
    }
    @keyframes blink-caret {
        from, to { border-color: transparent; }
        50% { border-color: #e07a5f; }
    }
    </style>
    """, unsafe_allow_html=True)

# HEADER SECTION WITH BACKGROUND IMAGE AND TYPEWRITER EFFECT
with st.container():
    st.markdown("""
        <div class="header-section">
            <h1 class="typewriter">Writer's Introspection</h1>
            <p>This is a collection of my written works. Feel free to browse through them.</p>
        </div>
        """, unsafe_allow_html=True)
    st.write("Click on the links below to view the contents.")
    st.write("1. [My Blog Posts](https://sites.google.com/view/shiv-raj-singh/home)")
    st.write("2. [My social media profiles](https://www.instagram.com/imuniqueshiv/?hl=en)")

# SIDEBAR SECTION
st.sidebar.title("Settings")
dark_mode = st.sidebar.toggle("Dark Mode", value=False)
if dark_mode:
    st.markdown("""
        <style>
        body {
            background: linear-gradient(135deg, #1e1e1e, #3d405b);
            color: #ffffff;
        }
        h1, h2, h3, h4, h5, h6 {
            color: #ffffff;
        }
        .poetry-title {
            color: #81b29a;
        }
        .poetry-title:hover {
            color: #f2cc8f;
        }
        .full-poetry {
            background-color: rgba(61, 64, 91, 0.8);
            color: #ffffff;
        }
        .footer {
            background-color: rgba(61, 64, 91, 0.8);
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)

# About Me Section
st.sidebar.header("About Me")
st.sidebar.markdown(
    """
    👋 Hi, I’m Shiv Raj Singh (@imuniqueshiv)
    🎓 B.Tech 1st Year | AI & ML
    👀 Interested in Technology, Sports, and Writing
    💡 Exploring the Imaginative World
    """
)
st.sidebar.write("[Medium >](https://medium.com/@imuniqueshiv)")

# SEARCH BAR
st.write("---")
st.header("Search Poetry")
search_query = st.text_input("Enter a keyword to search poetry", "")
clear_search = st.button("Clear Search")

if clear_search:
    search_query = ""

# Filter poetry based on search query
filtered_poetry = [poem for poem in poetry_data if search_query.lower() in poem["title"].lower() or search_query.lower() in poem["content"].lower()]

# Display poetry titles with "Like" button and comments
st.write("---")
st.header("My Poetry")
for poem in filtered_poetry:
    with st.expander(f"📖 {poem['title']}"):
        st.markdown(f"<div class='full-poetry' style='white-space: pre-line;'>{poem['content']}</div>", unsafe_allow_html=True)
        # Like button
        if st.button(f"❤️ Like {poem['title']}"):
            st.write(f"You liked '{poem['title']}'!")
        # Comments section
        comment = st.text_input(f"Add a comment for '{poem['title']}'", "")
        if comment:
            st.write(f"Your comment: {comment}")

# Footer
st.write("---")
st.markdown("""
    <div class="footer">
        Writing © 2024 by Shiv Raj Singh is licensed under Attribution-NonCommercial-NoDerivatives 4.0 International. 
        To view a copy of this license, visit <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/">http://creativecommons.org/licenses/by-nc-nd/4.0/</a>
    </div>
    """, unsafe_allow_html=True)