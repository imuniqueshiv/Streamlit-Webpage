import streamlit as st

from introspection import introspection  # Import introspection data from the separate file
from poetry_data import poetry_data  # Import poetry data from the separate file

# Set page configuration
st.set_page_config(page_title="MY library", page_icon=":writing_hand:", layout="wide")

# Custom CSS for styling
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700&family=Roboto:wght@300;400&display=swap');

    body {
        background: linear-gradient(135deg, #f4f1de, #f2cc8f);
        color: #3d405b;
        font-family: 'Roboto', sans-serif;
        scroll-behavior: smooth;
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
        animation: fadeIn 2s ease-in-out;
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
    @keyframes fadeIn {
        from { opacity: 0; }
        to { opacity: 1; }
    }
    .stButton button {
        background-color: #81b29a;
        color: white;
        border-radius: 5px;
        padding: 10px 20px;
        font-size: 16px;
        transition: background-color 0.3s ease, transform 0.3s ease;
    }
    .stButton button:hover {
        background-color: #e07a5f;
        transform: scale(1.05);
    }
    .stTextInput input {
        font-size: 16px;
        padding: 10px;
        border-radius: 5px;
        border: 1px solid #81b29a;
        transition: border-color 0.3s ease;
    }
    .stTextInput input:focus {
        border-color: #e07a5f;
        outline: none;
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
        transition: color 0.3s ease, transform 0.3s ease;
    }
    .poetry-title:hover {
        color: #3d405b;
        transform: translateX(10px);
    }
    .poetry-card {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
        cursor: pointer;
    }
    .poetry-card:hover {
        transform: scale(1.05);
    }
    .full-poetry {
        background-color: rgba(255, 255, 255, 0.8);
        padding: 20px;
        border-radius: 10px;
        margin-top: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 1s ease-in-out;
    }
    .footer {
        text-align: center;
        padding: 20px;
        background-color: rgba(255, 255, 255, 0.8);
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        animation: fadeIn 2s ease-in-out;
    }
    .floating-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        background-color: #81b29a;
        color: white;
        border: none;
        border-radius: 50%;
        width: 60px;
        height: 60px;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: background-color 0.3s ease, transform 0.3s ease;
        display: none; /* Initially hidden */
        align-items: center;
        justify-content: center;
    }
    .floating-button:hover {
        background-color: #e07a5f;
        transform: scale(1.1);
    }
    </style>
    """, unsafe_allow_html=True)

# JavaScript for interactivity
st.markdown("""
    <script>
    window.onscroll = function() { scrollFunction(); };

    function scrollFunction() {
        let mybutton = document.getElementById("scrollTopBtn");
        if (document.body.scrollTop > 20 || document.documentElement.scrollTop > 20) {
            mybutton.style.display = "flex";
        } else {
            mybutton.style.display = "none";
        }
    }

    function topFunction() {
        document.body.scrollTop = 0;
        document.documentElement.scrollTop = 0;
    }
    </script>
    """, unsafe_allow_html=True)

# HEADER SECTION WITH BACKGROUND IMAGE AND TYPEWRITER EFFECT
with st.container():
    st.markdown("""
        <div class="header-section">
            <h1 class="typewriter">Where Words Paint Emotions</h1>
            <p style="color: metallic; font-family: 'Playfair Display', serif; font-size: 24px; font-weight: bold;">
            "I weave stories rich in emotion, blending imagination with human experiences, using nature-inspired metaphors to create a lasting impact."
            </p>
            <p>This is a collection of my written works. Feel free to browse through them.</p>
        </div>
        """, unsafe_allow_html=True)
    st.write("Click on the links below to view the contents.")
    st.write("1. [My Blog Posts](https://sites.google.com/view/shiv-raj-singh/home)")
    st.write("2. [My social media profiles](https://www.instagram.com/imuniqueshiv/?hl=en)")
# Sidebar Section
st.sidebar.title("Settings")

# Dark Mode Toggle with Icon
dark_mode = st.sidebar.toggle("🌙 Dark Mode", value=False)
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
        .sidebar-bio {
            color: #ffffff !important;
            background: rgba(61, 64, 91, 0.9) !important;
        }
        .sidebar-bio h2 {
            color: #81b29a !important;
        }
        .sidebar-bio p {
            color: #ffffff !important;
        }
        .sidebar-social a {
            background: rgba(61, 64, 91, 0.9) !important;
            color: #ffffff !important;
        }
        .sidebar-social a:hover {
            background: rgba(129, 178, 154, 0.9) !important;
        }
        </style>
        """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
        .sidebar-bio {
            background: rgba(255, 255, 255, 0.9) !important;
        }
        .sidebar-social a {
            background: rgba(255, 255, 255, 0.9) !important;
            color: #3d405b !important;
        }
        .sidebar-social a:hover {
            background: rgba(129, 178, 154, 0.9) !important;
            color: white !important;
        }
        </style>
        """, unsafe_allow_html=True)

# About Me Section with Enhanced Styling
st.sidebar.header("About Me")
st.sidebar.markdown(
    """
    <style>
    .sidebar-bio {
        font-family: 'Playfair Display', serif;
        font-size: 18px;
        line-height: 1.6;
        color: #3d405b;
        padding: 15px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 10px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    .sidebar-bio h2 {
        font-size: 24px;
        color: #4682b4; /* SteelBlue */
        margin-bottom: 10px;
    }
    .sidebar-bio p {
        margin: 0;
        color: #3d405b;
    }
    .sidebar-bio strong {
        color: #20b2aa; /* LightSeaGreen */
    }
    .sidebar-social {
        display: flex;
        flex-direction: column;
        gap: 10px;
        margin-top: 20px;
    }
    .sidebar-social a {
        display: flex;
        align-items: center;
        text-decoration: none;
        color: #3d405b;
        font-size: 16px;
        padding: 10px;
        background: rgba(255, 255, 255, 0.9);
        border-radius: 5px;
        box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease, box-shadow 0.3s ease, background 0.3s ease, color 0.3s ease;
    }
    .sidebar-social a:hover {
        transform: translateX(5px);
        box-shadow: 0 4px 8px rgba(0, 0, 0, 0.2);
    }
    .sidebar-social a i {
        margin-right: 10px;
        font-size: 20px;
    }
    </style>
    <div class="sidebar-bio">
        <h2>👋 Hi, I’m Shiv Raj Singh (@imuniqueshiv)</h2>
        <p><strong>🎓 B.Tech 1st Year | AI & ML</strong></p>
        <p><strong>👀 Passionate about Technology, Sports, and Creative Writing</strong></p>
        <p><strong>💡 Exploring the Boundaries of Imagination and Innovation</strong></p>
        <p><strong>📚 Avid Reader | 🎨 Art Enthusiast | 🌍 Traveler</strong></p>
    </div>
    <div class="sidebar-social">
        <a href="https://medium.com/@imuniqueshiv" target="_blank">
            <i class="fab fa-medium"></i> Medium
        </a>
        <a href="https://www.instagram.com/imuniqueshiv/?hl=en" target="_blank">
            <i class="fab fa-instagram"></i> Instagram
        </a>
        <a href="https://www.linkedin.com/in/shiv-raj-singh-387973299/" target="_blank">
            <i class="fab fa-linkedin"></i> LinkedIn
        </a>
        <a href="https://github.com/imuniqueshiv" target="_blank">
            <i class="fab fa-github"></i> GitHub
        </a>
    </div>
    """, unsafe_allow_html=True
)

# Add Font Awesome for Icons
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True,
)
# Add Font Awesome for Icons
st.markdown(
    """
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0-beta3/css/all.min.css">
    """,
    unsafe_allow_html=True,
)
# SEARCH BAR
st.write("---")
st.header("Search Poetry")
search_query = st.text_input("Enter a keyword to search poetry", "")
clear_search = st.button("Clear Search")

if clear_search:
    search_query = ""

# Filter poetry based on search query
filtered_poetry = [poem for poem in poetry_data if search_query.lower() in poem["title"].lower() or search_query.lower() in poem["content"].lower()]
# Display songs titles with "Like" button and comments

filtered_thoughts = [thought for thought in introspection if search_query.lower() in thought["title"].lower() or search_query.lower() in thought["content"].lower()]
st.write("---")

st.header("Introspection")
for thought in filtered_thoughts:
    with st.expander(f"💭 {thought['title']}"):
        st.markdown(f"<div class='poetry-card' style='white-space: pre-line; background-color: #2c3e50; color: #ffffff;'>{thought['content']}</div>", unsafe_allow_html=True)
        # Like button
        if st.button(f"❤️ Like {thought['title']}"):
            st.write(f"You liked '{thought['title']}'!")
        # Comments section
        comment = st.text_input(f"Add a comment for '{thought['title']}'", "")
        if comment:
            st.write(f"Your comment: {comment}")

# Display poetry titles with "Like" button and comments
st.write("---")
st.header("My Poetry")
for poem in filtered_poetry:
    with st.expander(f"📖 {poem['title']}"):
        st.markdown(f"<div class='poetry-card' style='white-space: pre-line; background-color: #2c3e50; color: #ffffff;'>{poem['content']}</div>", unsafe_allow_html=True)
        # Like button
        if st.button(f"❤️ Like {poem['title']}"):
            st.write(f"You liked '{poem['title']}'!")
        # Comments section
        comment = st.text_input(f"Add a comment for '{poem['title']}'", "")
        if comment:
            st.write(f"Your comment: {comment}")
# Floating Button for Quick Navigation
st.markdown("""
    <button id="scrollTopBtn" class="floating-button" onclick="topFunction()">↑</button>
    """, unsafe_allow_html=True)

# Footer
st.write("---")
st.markdown("""
    <div class="footer" style="background-color: #2c3e50; color: #ffffff;">
        Writing © 2024 by Shiv Raj Singh is licensed under Attribution-NonCommercial-NoDerivatives 4.0 International.
        To view a copy of this license, visit <a href="http://creativecommons.org/licenses/by-nc-nd/4.0/" style="color: #81b29a;">http://creativecommons.org/licenses/by-nc-nd/4.0/</a>
    </div>
    """, unsafe_allow_html=True)
