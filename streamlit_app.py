import streamlit as st
from datetime import datetime
import pandas as pd

# CSS
st.markdown(
    """
    <style>
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

        .css-18e3th9 {
            background-color: rgba(255, 255, 255, 0.85);
            padding: 2rem;
            border-radius: 1rem;
            box-shadow: 0 0 15px rgba(0,0,0,0.1);
        }

        .stTextInput > div > div > input {
            background-color: #ffffff;
            color: #000000;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Initialize
if 'search_history' not in st.session_state:
    st.session_state.search_history = []

if 'bookmarks' not in st.session_state:
    st.session_state.bookmarks = []

# Title
st.title("Mission Integration and Ops Data Solutioning")
st.write("Use the search directory below to find relevant data and resources.")

# Search Input
search_query = st.text_input("🔍 Search Directory", "")

# Advanced Filtering
with st.expander("Advanced Filters"):
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        selected_category = st.selectbox("Category", options=["All", "Test 1", "Test 2", "Test 3"])

    with col2:
        file_type = st.multiselect("File Type", options=["PDF", "Image", "Document", "Report"])

    with col3:
        start_date = st.date_input("Start Date", datetime(2023, 1, 1))
        end_date = st.date_input("End Date", datetime(2025, 1, 1))

    with col4:
        tags_input = st.text_input("Keywords / Tags (comma-separated)")

# Save Search History
if search_query and search_query not in st.session_state.search_history:
    st.session_state.search_history.insert(0, search_query)  # most recent first
    if len(st.session_state.search_history) > 5:  # keep last 5
        st.session_state.search_history.pop()

# Search Results
st.markdown("### Search Results")
if search_query:
    st.write(f"Showing results for: **{search_query}**")
    st.write("🔍 No results found. (Implement search logic here)")

    # --- Simulate a bookmarkable result ---
    if st.button("⭐ Bookmark This Search"):
        if search_query not in st.session_state.bookmarks:
            st.session_state.bookmarks.append(search_query)
            st.success("Search bookmarked!")
        else:
            st.info("This search is already bookmarked.")

else:
    st.info("Enter a keyword to search the directory or use filters above.")

# --- Display Recent Searches ---
if st.session_state.search_history:
    st.markdown("###  Recent Searches")
    for past_search in st.session_state.search_history:
        if st.button(f" {past_search}"):
            st.session_state.search_query = past_search

# Bookmark Section
if st.session_state.bookmarks:
    st.markdown("### 📌 Bookmarked Searches")
    for b in st.session_state.bookmarks:
        st.write(f"🔖 {b}")

    # --- Export Bookmarks to CSV ---
    export_df = pd.DataFrame(st.session_state.bookmarks, columns=["Search Query"])
    csv_data = export_df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="📤 Export Bookmarks to CSV",
        data=csv_data,
        file_name="bookmarked_searches.csv",
        mime="text/csv"
    )




