import requests
from bs4 import BeautifulSoup

from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        # Get the input value from the form
        input_prompt = request.form['input_prompt']
        # Search for memes related to the prompt
        meme_urls = search_memes(input_prompt)
        # Render the template with the meme URLs
        return render_template('index.html', meme_urls=meme_urls)
    else:
        return render_template('index.html')

def search_memes(prompt):
    # Replace 'url_to_scrape' with the URL of the webpage you want to scrape
    url_to_scrape = 'https://9gag.com/search?query=' + prompt
    # Send an HTTP request to the webpage
    response = requests.get(url_to_scrape)
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the webpage using BeautifulSoup
        soup = BeautifulSoup(response.text, 'html.parser')
        # Find all <img> tags with class="meme"
        meme_images = soup.find_all('img', class_='meme')
        # Extract and store the URLs of the meme images
        meme_urls = [img.get('src') for img in meme_images]
        return meme_urls
    else:
        return []

if __name__ == '__main__':
    app.run()