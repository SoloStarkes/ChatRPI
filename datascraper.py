


import requests
from bs4 import BeautifulSoup

import os
import openai

url = 'https://www.nbcnews.com/news/us-news/firefighters-battle-lahaina-maui-fire-rcna105142'

def data_scrape(url):


    response = requests.get(url)

    if response.status_code == 200:
        #this has the website text with all the html code
        #print(response.text)
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # this has the text of the website without the html tags and stuff 
        return soup.text
    
    else:
        return -1
        print('Failed to retrieve the page. Status code:', response.status_code)




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
                print(url)
                info = data_scrape(url)
                print(info)
                message_list.append( {"role": "system", "content": info})

                



                # You can further process this URL or send a request to scrape data from the website

    else:
        print("Failed to retrieve search results.")

api_key = "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"



message_list=[
    {"role": "system", "content": "You are a helpful assistant."},
  ]
def create_response(user_input):
    message_list.append( {"role": "user", "content": user_input})
    openai.api_key = os.getenv("OPENAI_API_KEY")
    completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=message_list
    )
  
    print(completion.choices[0].message.content)



user_input = input("Enter a message: ")
#search_websites_with_keyword("rpi")

ex_url = "https://www.rpi.edu/"
some_info = data_scrape(ex_url)
message_list.append( {"role": "system", "content": some_info})

create_response(user_input)



