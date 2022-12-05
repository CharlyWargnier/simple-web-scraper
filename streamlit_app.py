
import requests
from bs4 import BeautifulSoup
import streamlit as st

st.image('scraper.png', width=100)

st.header("Simple web scraper built with ChatGPT")

url = st.text_input("Enter URL to scrape:", "https://streamlit.io/")

#@st.cache

def scrape_page(url):
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    return soup

soup = scrape_page(url)

tab1, tab2 = st.tabs(["Scraped text", "Found links"])

with tab2:

    st.subheader("Links on the website:")

    for link in soup.find_all("a"):

        st.write(link.get("href"))

with tab1:

    st.write("Website text:", soup.get_text())


