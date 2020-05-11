import os
import urllib.request

from bs4 import BeautifulSoup

urlList = [
    'https://techtronicsound.podzone.net/2005/08/27/01-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/09/03/02-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/09/10/03-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/09/20/04-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/09/23/05-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/10/04/06-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/10/12/07-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/10/16/08-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/10/25/9-the-best-of-techtronic-sound-part-1/',
    'https://techtronicsound.podzone.net/2005/10/29/10-the-best-of-techtronic-sound-part-2/ ',
    'https://techtronicsound.podzone.net/2005/11/08/11-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/11/15/12-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/11/22/13-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/11/28/14-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/12/07/15-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/12/15/16-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/12/21/17-techtronic-sound/',
    'https://techtronicsound.podzone.net/2005/12/28/18-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/01/05/19-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/01/15/20-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/01/21/21-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/01/30/22-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/02/06/23-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/02/14/24-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/02/24/25-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/03/03/26-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/03/14/27-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/03/22/28-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/03/31/29-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/04/08/30-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/04/19/31-the-best-of-techtronic-sound-part-1/ ',
    'https://techtronicsound.podzone.net/2006/04/30/32-the-best-of-techtronic-sound-part-2/ ',
    'https://techtronicsound.podzone.net/2006/05/06/33-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/05/17/34-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/06/03/35-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/06/11/36-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/06/21/37-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/07/02/38-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/07/11/39-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/07/20/40-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/08/01/41-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/08/05/late-nights-2006-08-05-pt1/',
    'https://techtronicsound.podzone.net/2006/08/05/late-nights-2006-08-05-pt2/',
    'https://techtronicsound.podzone.net/2006/08/05/late-nights-2006-08-05-pt2-2/',
    'https://techtronicsound.podzone.net/2006/08/05/late-nights-2006-08-05-pt4/',
    'https://techtronicsound.podzone.net/2006/08/09/42-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/08/11/late-nights-2006-08-11-pt1/',
    'https://techtronicsound.podzone.net/2006/08/11/late-nights-2006-08-11-pt2/',
    'https://techtronicsound.podzone.net/2006/08/11/late-nights-2006-08-11-pt3/',
    'https://techtronicsound.podzone.net/2006/08/11/late-nights-2006-08-11-pt4/',
    'https://techtronicsound.podzone.net/2006/08/12/late-nights-2006-08-12-pt1/',
    'https://techtronicsound.podzone.net/2006/08/12/late-nights-2006-08-12-pt2/',
    'https://techtronicsound.podzone.net/2006/08/12/late-nights-2006-08-12-pt3/',
    'https://techtronicsound.podzone.net/2006/08/12/late-nights-2006-08-12-pt4/',
    'https://techtronicsound.podzone.net/2006/08/18/43-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/08/24/44-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/09/07/45-anniversary-show/',
    'https://techtronicsound.podzone.net/2006/09/20/46-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/09/23/late-nights-2006-09-23-pt1/',
    'https://techtronicsound.podzone.net/2006/09/23/late-nights-2006-09-23-pt2/',
    'https://techtronicsound.podzone.net/2006/09/23/late-nights-2006-09-23-pt3/',
    'https://techtronicsound.podzone.net/2006/09/23/late-nights-2006-09-23-pt4/',
    'https://techtronicsound.podzone.net/2006/09/29/late-nights-2006-09-29/',
    'https://techtronicsound.podzone.net/2006/10/03/47-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/10/07/late-nights-2006-10-07/',
    'https://techtronicsound.podzone.net/2006/10/14/late-nights-2006-10-14-2/',
    'https://techtronicsound.podzone.net/2006/10/14/late-nights-2006-10-14/',
    'https://techtronicsound.podzone.net/2006/10/21/48-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/10/21/late-nights-2006-10-21/',
    'https://techtronicsound.podzone.net/2006/10/28/49-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/10/28/late-nights-2006-10-28-pt1/',
    'https://techtronicsound.podzone.net/2006/10/28/late-nights-2006-10-28-pt2/',
    'https://techtronicsound.podzone.net/2006/11/04/late-nights-2006-11-04-pt1/',
    'https://techtronicsound.podzone.net/2006/11/04/late-nights-2006-11-04-pt2/',
    'https://techtronicsound.podzone.net/2006/11/04/late-nights-2006-11-04-pt3/',
    'https://techtronicsound.podzone.net/2006/11/04/late-nights-2006-11-04-pt4/',
    'https://techtronicsound.podzone.net/2006/11/10/50-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/11/11/late-nights-2006-11-11-pt1/',
    'https://techtronicsound.podzone.net/2006/11/11/late-nights-2006-11-11-pt2/',
    'https://techtronicsound.podzone.net/2006/11/11/late-nights-2006-11-11-pt3/',
    'https://techtronicsound.podzone.net/2006/11/18/late-nights-2006-11-18-pt1/',
    'https://techtronicsound.podzone.net/2006/11/18/late-nights-2006-11-18-pt2/',
    'https://techtronicsound.podzone.net/2006/11/24/51-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/12/01/52-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/12/13/53-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/12/22/54-techtronic-sound/',
    'https://techtronicsound.podzone.net/2006/12/25/55-christmas-special/',
    'https://techtronicsound.podzone.net/2007/01/16/56-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/01/29/57-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/02/11/58-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/02/20/59-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/02/27/60-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/03/08/61-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/03/15/62-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/04/02/63-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/04/03/64-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/04/18/65-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/05/10/66-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/05/28/67-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/06/21/68-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/07/05/69-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/07/23/70-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/08/14/71-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/10/17/72-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/12/16/73-techtronic-sound/',
    'https://techtronicsound.podzone.net/2007/12/24/74-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/01/01/75-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/01/07/76-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/01/15/77-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/01/26/78-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/02/06/79-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/03/09/80-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/03/21/81-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/03/30/82-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/04/11/83-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/05/14/84-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/06/04/85-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/06/26/86-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/07/06/87-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/07/12/88-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/07/20/89-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/08/04/90-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/08/13/91-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/08/22/92-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/09/02/93-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/09/08/94-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/09/22/95-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/10/09/96-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/10/24/97-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/11/18/98-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/11/28/99-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/12/15/100-1-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/12/17/100-2-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/12/20/100-3-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/12/29/100-4-techtronic-sound/',
    'https://techtronicsound.podzone.net/2008/12/31/100-5-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/03/100-6-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/05/100-7-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/08/100-8-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/11/100-9-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/12/100-10-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/14/100-11-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/17/100-12-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/20/100-13-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/21/100-14-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/01/23/100-15-techtronic-sound/',
    'https://techtronicsound.podzone.net/2009/04/03/100-16-techtronic-sound/',
    'https://techtronicsound.podzone.net/2010/06/21/100-17-techtronic-sound/ ',
    'https://techtronicsound.podzone.net/2010/07/13/100-18-techtronic-sound/ ',
    'https://techtronicsound.podzone.net/2010/07/23/100-19-techtronic-sound/ ',
    'https://techtronicsound.podzone.net/2011/05/27/101-techtronic-sound/'
]


def is_valid_element(tag):
    # https://stackoverflow.com/questions/9573244/how-to-check-if-the-string-is-empty
    # remove empty (falsy) tags
    if len(tag.get_text(strip=True)) == 0:
        return False
    # https://stackoverflow.com/questions/2612548/extracting-an-attribute-value-with-beautifulsoup
    # remove elements if they have a class attribute mentioning powerpress, using an inner filter
    if tag.get("class") is not None:
        powerpressClassItems = [classVal for classVal in tag.get("class") if "powerpress" in classVal]
        if len(powerpressClassItems) > 0:
            return False
    return True


fileName = "linkInfo.md"

# https://www.w3schools.com/python/python_file_remove.asp
# first clean up the existing file so we can start fresh
if os.path.exists(fileName):
    os.remove(fileName)

# https://www.geeksforgeeks.org/iterate-over-a-list-in-python/
# iterate over each item in the input URL list
for url in urlList:
    # https://docs.python.org/3/library/urllib.request.html#module-urllib.request
    # Fetch the data
    # Using the requests library. requests.get(url).text() would also work
    content = urllib.request.urlopen(url)

    # read into BeautifulSoup. print(soup.prettify()) would print it
    soup = BeautifulSoup(content, features="html.parser")

    # https://stackoverflow.com/questions/5041008/how-to-find-elements-by-class
    # get the the first div with a particular class
    entryDivContents = soup.find("div", {"class": "entry-content"})

    # https://stackoverflow.com/questions/8533673/beautifulsoup-get-tag-name-of-element-itself-not-its-children
    # get all items of type paragraph, heading3, or unordered list in that div
    paragraphResultSet = entryDivContents.find_all(['p', 'h3', 'ul'])

    # https://stackoverflow.com/questions/12451997/beautifulsoup-gettext-from-between-p-not-picking-up-subsequent-paragraphs
    # convert from BeautifulSoup ResultSet to normal List and save only the plaintext (no <> tags) from each result.
    # Also do filtering to save only the elements we consider valid
    paragraphTextList = [k.get_text() for k in paragraphResultSet if is_valid_element(k)]

    # get the name of the page
    urlSplit = url.split("/")
    pageName = urlSplit[len(urlSplit) - 2]

    # https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python
    # write the output to a file in markdown format with the pagename as the top level list and contents as a subitem
    # https://stackoverflow.com/questions/27092833/unicodeencodeerror-charmap-codec-cant-encode-characters
    # make sure we are using the correct encoding so we don't get parsing errors
    with open(fileName, "a", encoding="utf-8") as outputFile:
        # print the page name and URL in Markdown hyperlink format
        outputFile.write("* [" + pageName + "](" + url + ')\n')

        # write all paragraphs we've extracted from the div as items in a Markdown list
        for paragraph in paragraphTextList:
            outputFile.write("  * " + paragraph + '\n')

    print("finished processing " + url + "\n")
