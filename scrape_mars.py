# dependencies
import time
from bs4 import BeautifulSoup as bs
import requests
from splinter import Browser
from selenium import webdriver
import pandas as pd

def intital_browser():
	executable_path = {"executable_path": "chromedriver.exe"}
	return Browser("chrome", **executable_path, headless=False)

def scrape():
	browser = intital_browser()

	# empty dictionary to hold empy data
	mars_data = {}

	# the Mars news page

	marsNews_url = "https://mars.nasa.gov/news/"
	browser.visit(marsNews_url)

	# search or the news using Scrape and Soup

	hmlt = broser.html
	mars_news = bs(html, 'html.parser')

	# Find title and summary

	news_title = mars_news.find('div', 'content_title').text

	


