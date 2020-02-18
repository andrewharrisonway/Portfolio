# Project 2 - Billboard Hot 100/Spotify Regression

Project 2 required us to scrape data from the web and answer a question about it using regression.  As a musician, I chose to examine Billboard's Hot 100.  Using BeautifulSoup, I scraped the Hot 100 for every week in 2019.  After filtering for tracks released in 2019, I used SpotiPy to interact with Spotify's API to grab their 'Audio Feature' information for each track.  I then used LASSO and Ridge techniques to explore whether or not there is a relationship between audio features and how long a track stays on the Hot 100.

[Presentation Deck](../Hot100_Spotify/AndrewWMusicByFeatureSubmission.pdf)

[Hot 100 Scraper](../Hot100_Spotify/hot100scraper.py)

[Scraping Code](../Hot100_Spotify/Hot100ParserV2.ipynb)

[Regression Analysis Code](../Hot100_Spotify/Hot100Regression.ipynb)

[Blog](https://www.andrewharrisonway.com/journal/regression-progression-or-how-i-learned-to-stop-worrying-and-love-machine-learning)
