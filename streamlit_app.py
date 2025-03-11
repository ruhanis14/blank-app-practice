import streamlit as st

# Custom CSS for professional NASA-style theme
st.markdown(
    """
    <style>
        /* Set background color and font */
        body {
            background-color: #f5f7fa;
            color: #1e1e1e;
            font-family: 'Segoe UI', sans-serif;
        }

        .stApp {
            background-image: url("https://images.unsplash.com/photo-1602016753442-2f54a9b7b2f5?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
            background-size: cover;
            background-repeat: no-repeat;
            background-position: center;
        }

        /* Transparent container background for readability */
        .css-18e3th9 {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }

        /* Input and text colors */
        .stTextInput > div > div > input {
            background-color: #ffffff;
            color: #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# App content
st.title("🚀 Mission Integration and Ops Data Solutioning")

st.write("Use the search directory below to find relevant data and resources.")

# Create a search input
search_query = st.text_input("Search Directory:", "")

# Placeholder for search results (Replace with actual search logic)
if search_query:
    st.write(f"Showing results for: **{search_query}**")
    # Implement search logic here (e.g., filtering a dataset, searching a database, etc.)
    st.write("🔍 No results found. (Implement search logic here)")
else:
    st.write("Enter a keyword to search the directory.")

