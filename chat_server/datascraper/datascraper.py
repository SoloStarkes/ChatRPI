from dotenv import load_dotenv
import asyncio
import aiohttp
from bs4 import BeautifulSoup
import os
import openai

load_dotenv()
api_key = os.getenv("API_KEY7")

# Function to check if website can be scraped successfully
async def fetch_data(session, url):
    async with session.get(url) as response:
        if response.status == 200:
            return await response.text()
        else:
            print(f"Failed to fetch data from {url}. Status code: {response.status}")
            return None

# Extracts data from specified URL
async def scrape_website(url):
    async with aiohttp.ClientSession() as session:
        html = await fetch_data(session, url)
        if html:
            soup = BeautifulSoup(html, 'html.parser')
            # Extract data from the BeautifulSoup object as needed
            # For example:
            title = soup.title.text
            return {"url": url, "title": title}

# List of URL's to scrape data from. Scraping happens asynchronous
async def main():
    # Add more URls as needed
    urls = [
        'https://www.rpi.edu/',
        'https://catalog.rpi.edu/',
        'https://president.rpi.edu/'
    ]

    # List of data that has been scraped from the different URLs
    scraped_data = []
    tasks = []
    for url in urls:
        task = asyncio.create_task(scrape_website(url))
        tasks.append(task)

    # If data scraping of specififed URL is a success, add to scraped_data and
    # return the array
    scraped_results = await asyncio.gather(*tasks)
    for result in scraped_results:
        if result:
            scraped_data.append(result)

    return scraped_data

if __name__ == "__main__":
    # Message list and user input for the chatbot as well as the scraped data
    # from websites to feed it
    message_list = []
    user_input = input("Enter a message: ")
    scraped_data = asyncio.run(main())
    for data in scraped_data:
        # Convert the content dictionary to string
        content_str = f"{data['url']}: {data['title']}"
        message_list.append({"role": "system", "content": content_str})
        #message_list.append({"role": "system", "content": data})
    openai.api_key = api_key
    for i in range(len(message_list)):
        print(message_list[i])
    message_list.append({"role": "user", "content": user_input})
    completion = openai.ChatCompletion.create(
        model = "gpt-3.5-turbo",
        messages = message_list,
    )
    print(completion.choices[0].message.content)
    

'''
import time 
import requests
from bs4 import BeautifulSoup
import os
import openai

api_key = os.getenv("API_KEY7")

def data_scrape(url, timeout=2):
    try:
        start_time = time.time()
        response = requests.get(url, timeout=timeout)
        end_time = time.time()
        elapsed_time = end_time - start_time
        
        if response.status_code == 200:
            print("Successful response")
            if elapsed_time > timeout:
                print("Request took more than 2 seconds. Skipping...")
                return -1
            soup = BeautifulSoup(response.text, 'html.parser')
            return soup.text
        else:
            print('Failed to retrieve the page. Status code:', response.status_code)
            return -1
    except requests.exceptions.Timeout:
        print('Request timed out after', timeout, 'seconds. Skipping...')
        return -1
    except Exception as e:
        print('An error occurred:', str(e))
        return -1

def search_websites_with_keyword(keyword):
    # Define the search query
    search_query = f"intitle:{keyword}"  # This query searches for "rpi" in the title of web pages

    # Send a GET request to Google Search with the query
    search_url = f"https://www.google.com/search?q={search_query}"
    headers = {"User-Agent": "Your User Agent Here"}  # Replace with your User-Agent header
    response = requests.get(search_url, headers=headers)
    
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content of the search results page
        soup = BeautifulSoup(response.text, "html.parser")

        # Find and extract search result links
        search_results = soup.find_all("a")
        for result in search_results:
            link = result.get("href")
            if link and link.startswith("/url?q="):
                # Extract the actual URL from the Google search result link
                url = link[7:]  # Remove "/url?q=" prefix
                info = data_scrape(url)
                if (info != -1):
                    message_list.append( {"role": "system", "content": info})
                # You can further process this URL or send a request to scrape data from the website

    else:
        print("Failed to retrieve search results.")

def create_response(user_input, message_list=[]):
    time.sleep(1)
    message_list.append( {"role": "user", "content": user_input})
    print(message_list)
    openai.api_key = api_key
    print("starting creation")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_list,
    )
    print("created")
    print(completion.choices[0].message.content)
    message_list.pop()
    
    return completion.choices[0].message.content

if __name__ == "__main__":
    message_list=[
    {"role": "system", "content": "You are a helpful assistant."},
  ]
    user_input = input("Enter a message: ")
    search_websites_with_keyword("rpi")

    ex_url = "https://www.rpi.edu/"
    #some_info = data_scrape(ex_url)
    message_list.append( {"role": "system", "content": some_info})

    create_response(user_input, message_list)
'''