## Link Scraper

Background

* I'm creating an archive of a podcast I once listened to, whose files and metadata are currently available on an archive website
* I'm not sure how long that website will be live and it's suffered outages in the past, so I wanted to make a backup of the data found since the music from the podcast is not easily obtainable
* BeautifulSoup v4 seems to be a common HTML scraping/parsing option so I figured I would give it a shot for this



Challenges

* Formats vary wildly from post to post on the archive website, so grabbing all the relevant info was tricky. A combination of grabbing headings, paragraphs, and unordered lists appears to have retrieved all the information needed. 
* Output is still very unformatted, so I need to go through and manually separate stuff out into Markdown format