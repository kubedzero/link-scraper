from http import cookiejar
from json import loads, dumps
from random import randint
from time import sleep

from bs4 import BeautifulSoup
from requests import get

# Configure portions of the code
# If set to False, the class list will be fetched from the live library pages
read_library_from_file = True
# Set the name of the JSON output file
dedica_class_filename = 'dedica_class_video_dict.json'
# Set the name of the Netscape-formatted Cookies file
cookies_file = 'dedica_cookies.txt'
# Define the library URLs to fetch. The page shows 200 classes at a time
library_urls = ['https://www.dedica.live/on-deamand-library',
                'https://www.dedica.live/on-deamand-library?offset=200']

# Create the cookie jar used to fulfill an authenticated request
# https://requests.readthedocs.io/en/latest/user/quickstart/#cookies
cookie_jar = cookiejar.MozillaCookieJar(cookies_file)
cookie_jar.load()


def get_class_urls_from_file():
    with open(dedica_class_filename) as file:
        data = file.read()
        return loads(data)


def get_class_urls_from_library_page():
    url_dict = dict()
    # Loop through the library URLs, parsing the class hrefs from each
    for url in library_urls:
        response = get(url, cookies=cookie_jar)
        soup = BeautifulSoup(response.text, features='html.parser')

        # The Library page has a few unordered lists, one of them contains all the classes
        # https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
        # https://stackoverflow.com/questions/8533673/beautifulsoup-get-tag-name-of-element-itself-not-its-children
        for unordered_list in soup.find_all('ul'):
            # Get the specific list where the class list has an element list-grid. This list contains the videos
            if unordered_list.get('class') is not None and 'list-grid' in unordered_list.get('class'):
                # Get all the A tags inside this set
                # NOTE: This includes the aria as well as normal tags so there are duplicates
                a_tags = unordered_list.find_all('a')
                for a_tag in a_tags:
                    # Add each of the hrefs to the dict as keys, leaving the not-yet-known Vimeo URL as None
                    # Since the href is a partial URL, prepend the domain for a full URL as the key
                    url_dict['https://www.dedica.live' + a_tag.get('href')] = None

    return url_dict


def add_vimeo_urls_to_dict(class_dict):
    for class_url in class_dict:
        # Skip fetching if the dict already had a value for the current URL
        if class_dict[class_url] is not None:
            print('URL {} already had a Vimeo link {}'.format(class_url, class_dict[class_url]))
            continue
        # Otherwise, fetch vimeo page URLs in a failsafe manner, so one failure doesn't block the whole process
        try:
            response = get(class_url, cookies=cookie_jar)
            soup = BeautifulSoup(response.text, features='html.parser')
            iframe = soup.find('iframe')
            class_dict[class_url] = iframe.get('src')
            print('URL {} had Vimeo link {}'.format(class_url, iframe.get('src')))
        except Exception as error:
            print('Something failed with the fetching of URL {}. Error {}'.format(class_url, error))

        # Add a 1-10s delay before the next loop to simulate human behavior
        sleep(randint(1, 10))
    return class_dict


def main():
    # Populate the dict with the class webpage URLs
    if read_library_from_file:
        class_dict = get_class_urls_from_file()
    else:
        class_dict = get_class_urls_from_library_page()

    # Get the Vimeo URLs from the individual class webpages
    class_dict = add_vimeo_urls_to_dict(class_dict)

    # Write the class webpage: Vimeo link map to a file
    with open(dedica_class_filename, 'w') as convert_file:
        convert_file.write(dumps(class_dict))


# https://stackoverflow.com/questions/419163/what-does-if-name-main-do
if __name__ == '__main__':
    main()
