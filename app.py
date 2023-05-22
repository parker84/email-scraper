
import requests 
from bs4 import BeautifulSoup
import streamlit as st
import re

st.set_page_config(page_title='Email Scraper', page_icon='⚒️', initial_sidebar_state="auto", menu_items=None)
st.title("⚒️ Email Scraper")

url = st.text_input("Enter URL to scrape emails from", "https://stan.store/brydon")

response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')
# use regular expressions to find email addresses
emails = re.findall(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b', str(soup))
emails = list(set(emails))

st.text(str(emails))

st.warning("⚠️ Warning: Note that not all websites may contain email addresses or allow email harvesting, and harvesting email addresses without permission may be a violation of the website's terms of service or applicable laws. Be sure to read and understand the website's terms of service and any applicable laws or regulations before scraping any website.")
