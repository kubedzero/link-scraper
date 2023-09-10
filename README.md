## Link Scraper

Background

* I'm creating an archive of a podcast I once listened to, whose files and metadata are currently available on an archive website
* I'm not sure how long that website will be live and it's suffered outages in the past, so I wanted to make a backup of the data found since the music from the podcast is not easily obtainable
* BeautifulSoup v4 seems to be a common HTML scraping/parsing option so I figured I would give it a shot for this



Challenges

* Formats vary wildly from post to post on the archive website, so grabbing all the relevant info was tricky. A combination of grabbing headings, paragraphs, and unordered lists appears to have retrieved all the information needed. 
* Output is still very unformatted, so I need to go through and manually separate stuff out into Markdown format



## 2023-09 Dedica Yoga Scraping

- Dea posts a full library of all the different yoga instruction videos, using Squarespace and Vimeo for the actual video hosting
- I'm using Requests to fetch the library page with a logged-in cookie and then using BeautifulSoup4 to parse the library page to get each of the video pages
- From each of the video pages, I then parse to find the Vimeo link to the actual class video
- Once I have a Vimeo link, I can pass it into yt-dlp to perform the download. This is out of scope for the project though, all I want is a repeatable way to fetch the library and Vimeo links (as I'll re-scrape in the future to get newly added videos)
- Goals:
  - Get a Python-readable list of all the class video pages, generated from the library pages (pagination at 200 items per page means I need to fetch multiple library pages to get everything)
  - Get a list of all the Vimeo links, perhaps associated with its class page (dict?)
- I sometimes got an error, but after 3 cycles I got 23 errors, 1 error, and then 0 errors and now have a complete set of Vimeo links
- I then used Sublime to get all the Vimeo URLs and put them in a separate text file, one URL per line. I could then run `yt-dlp --batch-file ~/GitHub/kubedzero/link-scraper/vimeos.txt` to fetch the videos. 
- There were some videos that needed the full URL, so not just `https://player.vimeo.com/video/723170274` but actually `https://player.vimeo.com/video/727178556?h=777871a737&app_id=122963`. Otherwise, `yt-dlp` would throw an error such as `ERROR: [vimeo] 721786316: Unable to download webpage: HTTP Error 404: Not Found` and sure enough I'd get a 404 in-browser when trying to navigate to that page

## Resources

- Create a HashSet in Python with `variable = set()` https://stackoverflow.com/questions/26724002/contains-of-hashsetinteger-in-python
- Or create a HashTable/Dict with https://www.askpython.com/python/examples/hashsets-and-hashtables-in-python `variable = dict()`
- IsInstance can say if something is of a certain class or not, which can eliminate None and get only Tag instances for example: `if isinstance(item, bs4.Tag):` https://www.w3schools.com/python/ref_func_isinstance.asp
- General official BeautifulSoup4 documentation https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- Pass in cookies to a request, either with the builtin `urllib` library or the `requests` library https://stackoverflow.com/questions/51682341/how-to-send-cookies-with-urllib https://requests.readthedocs.io/en/latest/user/quickstart/#cookiesd https://docs.python.org/3/library/http.cookiejar.html https://stackoverflow.com/questions/14742899/using-cookies-txt-file-with-python-requests
  - First define the cookie jar and point it to the Netscape-formatted cookies file `cookie_jar = http.cookiejar.MozillaCookieJar('cookies.txt')`
  - Then load it with `cookie_jar.load()`
  - Then fetch it with requests `requests.get(url, cookies=cookie_jar)`
  - Note that cookielib was renamed to cookiejar https://stackoverflow.com/questions/8405096/python-3-2-cookielib
- BeautifulSoup examples https://www.digitalocean.com/community/tutorials/how-to-work-with-web-data-using-requests-and-beautiful-soup-with-python-3 https://www.tutorialspoint.com/beautiful_soup/beautiful_soup_quick_guide.htm
- Change a key in a dict https://www.geeksforgeeks.org/python-ways-to-change-keys-in-dictionary/# `ini_dict['akash'] = ini_dict.pop('akshat')`
- YT-DLP configuration notes https://github.com/yt-dlp/yt-dlp#filesystem-options
- Print out exceptions and continue as if nothing happened https://www.freecodecamp.org/news/python-print-exception-how-to-try-except-print-an-error/ `except Exception as error:`
- Get a random number with https://elearning.wsldp.com/python3/python-random-number-between-1-10/ `random.randint(1, 10)`
- Sleep for a given number of seconds with https://www.digitalocean.com/community/tutorials/python-time-sleep `time.sleep(5)`
- Read and write objects to file in JSON format https://www.geeksforgeeks.org/write-a-dictionary-to-a-file-in-python/  https://www.geeksforgeeks.org/how-to-read-dictionary-from-file-in-python/
- The Homebrew utility `jq` can format json files with `jq . path/to/file` https://stackoverflow.com/questions/12943819/how-to-prettyprint-a-json-file https://unix.stackexchange.com/questions/244946/how-to-prettyprint-json-using-jq-standalone

 