from bs4 import BeautifulSoup
from random import randint
from random_unicode_emoji import random_emoji
from requests import get
from time import sleep


print(
    "\n"
    + random_emoji()[0]
    + "**********************************************************************************************************"
)


class Story:
    def __init__(self, storynum):
        self.storyNumber = storynum
        self.page_details_list = []

    """storynum connects every chapter of a story with its page details."""

    class PageDetails:
        def __init__(self, title, text, chapter, storynum):
            self.title = title
            self.text = text
            self.chapter = chapter
            self.storyNumber = storynum

    def add_page_details(self, title, text, chapter, storynum):
        page_details = self.PageDetails(title, text, chapter, storynum)
        self.page_details_list.append(page_details)

    """Matches storynum to each story chapter in page_details list, then returns matching_page_details list."""

    def take(self, storynum):
        matching_page_details = []
        for page_details in self.page_details_list:
            if page_details.storyNumber == storynum:
                matching_page_details.append(page_details)
        return matching_page_details


"""Initialized Variables"""
y = 0
x = 0
page_array = []
story_array = []
soup = 0
cookie = {"view_mature": "true"}

"""Starting place for the webscraper/controlling variables"""
storynum = 1
chapnum = 1
count_to_scrape = 25200
my_story = Story(storynum=storynum)


while x <= count_to_scrape:
    chapter_code = 200
    story_code = 200
    Story.storyNumber = storynum
    chapnum = 1
    sleep(randint(1, 3))
    url = f"https://www.fimfiction.net/story/{storynum}/{chapnum}/"
    page_to_scrape = get(url, cookies=cookie)
    story_code = page_to_scrape.status_code
    while chapter_code == 200:
        sleep(randint(1, 3))

        chapter_code = page_to_scrape.status_code
        if chapter_code == 200:
            print(f"getting chapter {str(chapnum)} of story number {str(storynum)}")
            soup = BeautifulSoup(page_to_scrape.text, "html.parser")
            storytitles = soup.find("title")
            storytexts = soup.find("div", attrs={"class": "bbcode"})
            storytitles = storytitles.get_text()
            storytexts = storytexts.get_text()

            my_story.add_page_details(storytitles, storytexts, chapnum, storynum)
        chapnum = chapnum + 1
        url = f"https://www.fimfiction.net/story/{str(storynum)}/{str(chapnum)}/"
        page_to_scrape = get(url, cookies=cookie)

    # list of page details objects
    matching_details = my_story.take(storynum)

    if story_code == 200:
        with open(
            f"C:\\Users\\joshu\\Desktop\\GitHub\\Stories\\{str(storynum)}.txt",
            "w+",
            encoding="utf-8",
        ) as file:
            for obj in matching_details:
                single_story = (
                    f"\n\nTitle:\t{obj.title}\nChapter:\t{str(obj.chapter)}\n{obj.text}"
                )
                file.writelines(single_story)

    x = x + 1
    storynum = storynum + 1
