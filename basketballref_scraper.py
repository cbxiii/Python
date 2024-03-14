import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

url = 'https://www.basketball-reference.com/leagues/NBA_2023_per_game.html'
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # find table with per game stats
    table = soup.find('table')

    # extract column headers
    headers = [th.text for th in table.find('thead').find_all('th')]

    # extract player data from rows
    data = []
    for row in table.find('tbody').find_all('tr'):
        row_data = [th.text for th in row.find_all(['th', 'td'])]
        data.append(row_data)
    
    # create dataframe 
    df = pd.DataFrame(data, columns=headers)
    print(df)

    # export dataframe to csv
    df.to_csv('2023_nba_data.csv')

    # add delay between requests to avoid overwhelming website
    time.sleep(1)

else:
    print('Failed to fetch the URL:', url)
