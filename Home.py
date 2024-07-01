import streamlit as st

st.sidebar.page_link("Home.py")
st.header("Word Counter")
text = st.text_area("Enter Here")

def word_counter(text):
    word = text.split()
    wordlen = len(word)
    return wordlen

def char_count(text):
    characters = len(text.replace(" ", "").replace("\n", ""))
    return characters

if st.button("count"):
    word_count = word_counter(text)
    char_count = char_count(text)
    st.write(f"Words: {word_count}")
    st.write(f"Characters: {char_count}")