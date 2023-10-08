from flask import Flask, render_template, request
import requests
from bs4 import BeautifulSoup

app = Flask(__name__)

def get_memes(word):
	# Replace 'url_to_scrape' with the URL you want to scrape images from
	url_to_scrape = f'https://www.google.com/search?q={word}+memes&tbm=isch'

	# Send an HTTP GET request to the URL
	response = requests.get(url_to_scrape)

	# Check if the request was successful (status code 200)
	if response.status_code == 200:
		# Parse the HTML content of the page using BeautifulSoup
		soup = BeautifulSoup(response.text, 'html.parser')

		# Find all img tags in the parsed HTML
		img_tags = soup.find_all('img')

		# Extract the 'src' attribute from each img tag
		img_urls = [img['src'] for img in img_tags if 'src' in img.attrs]

		# Print the list of image URLs
		return img_urls
	else:
		print(f"Failed to retrieve the page. Status code: {response.status_code}")

#To rederect
#9GAG
#memebase.cheezburger.com

@app.route("/", methods = ["GET", "POST"])
def hello_world():
    if request.method == "POST":
        print(request.form["subject"])
        return render_template('index.html', meme_urls = get_memes(request.form["subject"]))
    else:
        return render_template('index.html', meme_urls = [])
    