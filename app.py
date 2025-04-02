# import pickle
# import streamlit as st
# import numpy as np

# st.header("Book Recommender System using Machine Learning")

# model = pickle.load(open('Artifacts/model.pkl', 'rb'))
# books_name = pickle.load(open('Artifacts/books_name.pkl', 'rb'))
# final_rating = pickle.load(open('Artifacts/final_rating.pkl', 'rb'))
# book_pivot = pickle.load(open('Artifacts/book_pivot.pkl', 'rb'))

# def fetch_poster(book_ids):
#     poster_urls = []
#     for book_id in book_ids:
#         # Get book name from pivot table index
#         book_name = book_pivot.index[book_id]
        
#         # Find the book in final_rating
#         book_info = final_rating[final_rating['title'] == book_name]
        
#         if not book_info.empty:
#             poster_url = book_info.iloc[0]['image_url']
#             poster_urls.append(poster_url)
#         else:
#             poster_urls.append(None)  # Handle case where image not found
    
#     return poster_urls

# def recommend_book(book_name):
#     # Find the selected book's details first
#     selected_book_info = final_rating[final_rating['title'] == book_name]
#     selected_poster = selected_book_info.iloc[0]['image_url'] if not selected_book_info.empty else None
    
#     # Get recommendations
#     book_id = np.where(book_pivot.index == book_name)[0][0]
#     distances, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    
#     # Get recommended book names and posters
#     recommended_books = [book_pivot.index[i] for i in suggestions[0]]
#     recommended_posters = fetch_poster(suggestions[0])
    
#     return selected_poster, recommended_books, recommended_posters

# # UI Elements
# selected_books = st.selectbox(
#     "Type or select a book",
#     books_name
# )

# if st.button('Recommend'):
#     selected_poster, recommended_books, recommended_posters = recommend_book(selected_books)
    
#     st.subheader("You selected:")
#     col0 = st.columns(1)
#     with col0[0]:
#         st.image(selected_poster, width=150)
#         st.text(selected_books)
    
#     st.subheader("Recommended for you:")
#     cols = st.columns(5)
    
#     for i in range(1, 6):  # Show top 5 recommendations (skip the first one as it's the selected book itself)
#         with cols[i-1]:
#             if i < len(recommended_posters) and recommended_posters[i]:
#                 st.text(recommended_books[i])
#                 st.image(recommended_posters[i])
#             else:
#                 st.text(f"No image for {recommended_books[i]}")


#------------------------------------------------------------------------------------------------------------

# import pickle
# import streamlit as st
# import numpy as np
# from PIL import Image

# # Page configuration
# st.set_page_config(
#     page_title="Book Recommender",
#     page_icon="📚",
#     layout="wide"
# )

# # Custom CSS styling
# def local_css(file_name):
#     with open(file_name) as f:
#         st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# local_css("style.css")  # Create a style.css file with the CSS below

# # Load the model and data
# @st.cache_data
# def load_data():
#     model = pickle.load(open('Artifacts/model.pkl', 'rb'))
#     books_name = pickle.load(open('Artifacts/books_name.pkl', 'rb'))
#     final_rating = pickle.load(open('Artifacts/final_rating.pkl', 'rb'))
#     book_pivot = pickle.load(open('Artifacts/book_pivot.pkl', 'rb'))
#     return model, books_name, final_rating, book_pivot

# model, books_name, final_rating, book_pivot = load_data()

# def fetch_poster(book_ids):
#     poster_urls = []
#     for book_id in book_ids:
#         book_name = book_pivot.index[book_id]
#         book_info = final_rating[final_rating['title'] == book_name]
#         poster_urls.append(book_info.iloc[0]['image_url'] if not book_info.empty else None)
#     return poster_urls

# def recommend_book(book_name):
#     selected_book_info = final_rating[final_rating['title'] == book_name]
#     selected_poster = selected_book_info.iloc[0]['image_url'] if not selected_book_info.empty else None
    
#     book_id = np.where(book_pivot.index == book_name)[0][0]
#     distances, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors=6)
    
#     recommended_books = [book_pivot.index[i] for i in suggestions[0]]
#     recommended_posters = fetch_poster(suggestions[0])
    
#     return selected_poster, recommended_books, recommended_posters

# # App Header with Background
# st.markdown("""
#     <div class="header">
#         <h1>📚 BOOK RECOMMENDER SYSTEM USING MACHINE LEARNING</h1>
#         <p>Discover your next favorite book!</p>
#     </div>
# """, unsafe_allow_html=True)

# # Main Content
# with st.container():
#     st.markdown("""
#         <div class="search-box">
#             <h3>Find similar books</h3>
#     """, unsafe_allow_html=True)
    
#     selected_books = st.selectbox(
#         "Type or select a book",
#         books_name,
#         key="book_select"
#     )
    
#     if st.button('Recommend Books', key="recommend_btn"):
#         with st.spinner('Finding your perfect reads...'):
#             selected_poster, recommended_books, recommended_posters = recommend_book(selected_books)
            
#             # Selected Book Display
#             st.markdown("---")
#             st.markdown("""
#                 <div class="selected-book">
#                     <h2>You selected:</h2>
#                 </div>
#             """, unsafe_allow_html=True)
            
#             col1, col2 = st.columns([1, 3])
#             with col1:
#                 if selected_poster:
#                     st.image(selected_poster, width=200)
#                 else:
#                     st.image("https://via.placeholder.com/200x300?text=No+Image", width=200)
#             with col2:
#                 st.markdown(f"""
#                     <div class="book-info">
#                         <h3>{selected_books}</h3>
#                         <p>Here are some similar books you might enjoy:</p>
#                     </div>
#                 """, unsafe_allow_html=True)
            
#             # Recommendations
#             st.markdown("---")
#             st.markdown("""
#                 <div class="recommendations">
#                     <h2>Recommended For You</h2>
#                 </div>
#             """, unsafe_allow_html=True)
            
#             cols = st.columns(5)
#             for i in range(1, 6):
#                 with cols[i-1]:
#                     card = st.container()
#                     card.markdown("""
#                         <style>
#                             .card {
#                                 padding: 15px;
#                                 border-radius: 10px;
#                                 background: white;
#                                 box-shadow: 0 4px 8px rgba(0,0,0,0.1);
#                                 transition: transform 0.3s;
#                                 height: 100%;
#                             }
#                             .card:hover {
#                                 transform: translateY(-5px);
#                             }
#                         </style>
#                     """, unsafe_allow_html=True)
                    
#                     with card:
#                         if i < len(recommended_posters) and recommended_posters[i]:
#                             st.markdown(f"<div class='book-title'>{recommended_books[i]}</div>", unsafe_allow_html=True)
#                             st.image(recommended_posters[i], width=150)
#                         else:
#                             st.markdown(f"<div class='book-title'>{recommended_books[i]}</div>", unsafe_allow_html=True)
#                             st.image("https://via.placeholder.com/150x225?text=No+Image", width=150)

# # Footer
# st.markdown("---")
# st.markdown("""
#     <div class="footer">
#         <p>Made by Sushant Chandra Poddar</p>
#     </div>
# """, unsafe_allow_html=True)

#---------------------------------------------------------------------------------------------------------------------------------------

import pickle
import streamlit as st
import numpy as np
from PIL import Image

# Page configuration
st.set_page_config(
    page_title="Book Recommender",
    page_icon="📚",
    layout="wide"
)

# Custom CSS styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

local_css("style.css")  # Create a style.css file with the CSS below

# Load the model and data
@st.cache_data
def load_data():
    model = pickle.load(open('Artifacts/model.pkl', 'rb'))
    books_name = pickle.load(open('Artifacts/books_name.pkl', 'rb'))
    final_rating = pickle.load(open('Artifacts/final_rating.pkl', 'rb'))
    book_pivot = pickle.load(open('Artifacts/book_pivot.pkl', 'rb'))
    return model, books_name, final_rating, book_pivot

model, books_name, final_rating, book_pivot = load_data()

def fetch_poster(book_ids):
    poster_urls = []
    for book_id in book_ids:
        book_name = book_pivot.index[book_id]
        book_info = final_rating[final_rating['title'] == book_name]
        poster_urls.append(book_info.iloc[0]['image_url'] if not book_info.empty else None)
    return poster_urls

def recommend_book(book_name, num_recommendations=5):
    selected_book_info = final_rating[final_rating['title'] == book_name]
    selected_poster = selected_book_info.iloc[0]['image_url'] if not selected_book_info.empty else None
    
    book_id = np.where(book_pivot.index == book_name)[0][0]
    # Get more recommendations than needed to account for the selected book possibly being in results
    distances, suggestions = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), 
                            n_neighbors=num_recommendations+2)
    
    recommended_books = [book_pivot.index[i] for i in suggestions[0]]
    recommended_posters = fetch_poster(suggestions[0])
    
    # Filter out the selected book from recommendations if it appears
    filtered_books = []
    filtered_posters = []
    for book, poster in zip(recommended_books, recommended_posters):
        if book != book_name and len(filtered_books) < num_recommendations:
            filtered_books.append(book)
            filtered_posters.append(poster)
    
    return selected_poster, filtered_books, filtered_posters

# App Header with Background
st.markdown("""
    <div class="header">
        <h1>📚 BOOK RECOMMENDER SYSTEM USING MACHINE LEARNING</h1>
        <h4>Discover your next favorite book!</h4>
    </div>
""", unsafe_allow_html=True)

# Main Content
with st.container():
    st.markdown("""
        <div class="search-box">
            <h3>Find similar books</h3>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([3, 2])
    with col1:
        selected_books = st.selectbox(
            "Type or select a book",
            books_name,
            key="book_select"
        )
    with col2:
        num_recommendations = st.slider(
            "Number of recommendations",
            min_value=1,
            max_value=10,
            value=5,
            key="rec_slider"
        )
    
    if st.button('Get Recommendations', key="recommend_btn"):
        with st.spinner(f'Finding {num_recommendations} perfect reads for you...'):
            selected_poster, recommended_books, recommended_posters = recommend_book(selected_books, num_recommendations)
            
            # Selected Book Display
            st.markdown("---")
            st.markdown("""
                <div class="selected-book">
                    <h2>You selected:</h2>
                </div>
            """, unsafe_allow_html=True)
            
            col1, col2 = st.columns([1, 3])
            with col1:
                if selected_poster:
                    st.image(selected_poster, width=250)
                else:
                    st.image("https://via.placeholder.com/200x300?text=No+Image", width=150)
            with col2:
                st.markdown(f"""
                    <div class="book-info">
                        <h3>{selected_books}</h3>
                        <p>Here are some similar books you might enjoy:</p>
                    </div>
                """, unsafe_allow_html=True)
            
            # Recommendations
            st.markdown("---")
            st.markdown(f"""
                <div class="recommendations">
                    <h2>Recommended For You ({num_recommendations} books)</h2>
                </div>
            """, unsafe_allow_html=True)
            
            # Dynamically create columns based on number of recommendations
            cols = st.columns(min(num_recommendations, 5))  # Max 5 columns in a row
            
            for i in range(len(recommended_books)):
                # Create new row if needed (every 5 books)
                if i > 0 and i % 5 == 0:
                    cols = st.columns(min(num_recommendations - i, 5))
                
                with cols[i % 5]:
                    card = st.container()
                    card.markdown("""
                        <style>
                            .card {
                                padding: 15px;
                                border-radius: 10px;
                                background: white;
                                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                                transition: transform 0.3s;
                                height: 100%;
                                margin-bottom: 20px;
                            }
                            .card:hover {
                                transform: translateY(-5px);
                            }
                        </style>
                    """, unsafe_allow_html=True)
                    
                    with card:
                        if recommended_posters[i]:
                            st.markdown(f"<div class='book-title'>{recommended_books[i]}</div>", unsafe_allow_html=True)
                            st.image(recommended_posters[i], width=200)
                        else:
                            st.markdown(f"<div class='book-title'>{recommended_books[i]}</div>", unsafe_allow_html=True)
                            st.image("https://via.placeholder.com/150x225?text=No+Image")

# Footer
st.markdown("---")
st.markdown("""
    <div class="footer">
        <p>Made By Sushant Chandra Poddar</p>
    </div>
""", unsafe_allow_html=True)