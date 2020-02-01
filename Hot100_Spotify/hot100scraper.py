#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import datetime as dt
from datetime import datetime
from IPython.core.display import display, HTML
from bs4 import BeautifulSoup
import requests

def hot100scraper(url):
    '''
    accepts url for Billboard Hot 100 website as a string
    returns dataframe of Hot 100 tracks
    '''

    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "lxml")
        entry_dict = {}

        for i in range(len(soup.find_all('li', class_="chart-list__element display--flex"))):
            single_ranking = soup.find_all('li', class_="chart-list__element display--flex")[i]
            rank = int(single_ranking.find('span',class_='chart-element__rank__number').text)
            song_title = single_ranking.find('span',class_='chart-element__information__song text--truncate color--primary').text
            artist = single_ranking.find('span',class_='chart-element__information__artist text--truncate color--secondary').text
            rank_change = single_ranking.find('span',class_='chart-element__information__delta__text text--default').text
            last_week = single_ranking.find('span', class_="chart-element__meta text--center color--secondary text--last").text
            peak_rank = int(single_ranking.find('span', class_="chart-element__meta text--center color--secondary text--peak").text)
            weeks_on_chart = int(single_ranking.find('span', class_="chart-element__meta text--center color--secondary text--week").text)
            chart_week = datetime.strptime(soup.find('button',class_='date-selector__button button--link').text.strip(),'%B %d, %Y')
            
            #some additional calculated stats
            artist_list = ([artist.strip() for artist in artist.replace('Nas X','Nas_X')
                                                               .replace(' X ','&')
                                                               .replace('Featuring','&')
                                                               .replace('featuring','&')
                                                               .replace(' x ','&')
                                                               .replace('Presents','&')
                                                               .replace(',','&')
                                                               .replace('Nas_X','Nas X') #not the finest solution, butwe've got 
                                                               .split('&')])             #to control for the double meaning of 'X'
                                                               
            artist_count = len(artist_list)
            collab = True if artist_count > 1 else False
            artist_query = ' '.join(artist_list[:2]) #we will use this when we're querying spotify.
                                                     #Two artists has proven sufficient to accurately identify tracks
            entry_dict[i]={
                'Rank': rank,
                'Song_title': song_title,
                'Artist': artist,
                'Rank_change': rank_change,  #maybe eliminate this, it's only really useful in a timeseries,
                                             #in which case, we would just analyze week over week
                'Last_week': last_week,
                'Peak_rank': peak_rank,
                'Weeks_on_chart': weeks_on_chart,
                'Chart_week': chart_week,
                'Artist_list': artist_list,
                'Artist_count': artist_count,
                'Collab': collab,
                'Artist_query': artist_query,
                'Song_and_artist' : (song_title + ' ' + artist) #this acts as an identifying key to help weed out remixes or same-titled songs
            }
        return entry_dict
    else:
        return 'site error'
