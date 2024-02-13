
import requests
from bs4 import BeautifulSoup

import json
import string
import os


   
def scrape_data(site_url:str) -> list:
    """ 
    Scrape data from a given URL 
    Return a list of all dictionary records on a page  
    """
    data = []
    
    try:
        request = requests.get(url=site_url)
    except:
        print(f"Couldnt access web address {site_url}")
    else:
        soup = BeautifulSoup(request.content, "html.parser")
        
        table_rows = soup.find_all('tr')
        for row in table_rows[1:]:
            payload = {
                    "name": row.find_all('td')[0].text,
                    "what": row.find_all('td')[1].text,
                    "region": row.find_all('td')[2].text,
                    "country": row.find_all('td')[3].text,
                    "lat": eval(row.find_all('td')[4].text),
                    "long": eval(row.find_all('td')[5].text),
                    "elev ft": eval(row.find_all('td')[6].text),
                    "pop est": eval(row.find_all('td')[7].text)
                }
            data.append(payload)
    return data


def get_url(index, letter):
    """ Url pattern """
    base_url = "https://www.fallingrain.com/world/NI/"
    index_str = f"0{index}" if index in range(1, 10) else str(index)
    return f"{base_url}{index_str}/a/{letter}"



def save_records(records, folder, name):
    """ save records to json file """
    file_path = os.path.join(folder, f"{name}.json")
    with open(file_path, 'w', encoding="utf-8") as json_file:
        json.dump(records, json_file, indent=4)
        
        
def main():
    folder = "scraped_data/"
    os.makedirs(folder, exist_ok=True)

    letters = tuple(filter(str.isupper, string.ascii_letters))
    
    for index in range(1,60):  # 1-60
        records = []
        
        for letter in letters:  # A-Z
            url = get_url(index, letter)
            
            # make a request
            request = requests.get(url)
            
            if request.status_code != 200:
                continue
            else:
                # scrape data
                data = scrape_data(url)
                records.extend(data)


       
        try:
            if len(records) != 0 and "region" in records[0]:
                name = records[0]['region'].lower()
                save_records(records, folder, name)
        except IndexError as err:
            print(records)
            print(f"Error: {err}")

    


if __name__ == "__main__":
    main()
    
  