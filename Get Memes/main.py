from selenium import webdriver
from selenium.webdriver.common.by import By

# Replace 'url_to_scrape' with the URL of the webpage you want to scrape
url_to_scrape = 'https://9gag.com/search?query=words'

# Replace 'path_to_webdriver' with the path to your WebDriver executable
# Example for Chrome:
path_to_webdriver = '/path/to/chromedriver'

# Create a WebDriver instance (e.g., for Chrome)
driver = webdriver.Chrome(executable_path=path_to_webdriver)

# Navigate to the webpage
driver.get(url_to_scrape)

# Find all <source> elements with type="video/mp4"
video_sources = driver.find_elements(By.CSS_SELECTOR, 'source[type="video/mp4"]')

# Extract and print the URLs
for source in video_sources:
    video_url = source.get_attribute('src')
    print(f"Video URL: {video_url}")

# Close the WebDriver
driver.quit()
