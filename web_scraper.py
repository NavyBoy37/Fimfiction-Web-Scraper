from bs4 import BeautifulSoup
import requests
import time
import random
from random_unicode_emoji import random_emoji
from selenium import webdriver
from selenium.webdriver.common.by import By

print("boop***********************************************************************************************************************************")
print("\n"+ random_emoji()[0])


class Story:
    def __init__(self,storynum):
        self.storyNumber = storynum
        self.page_details_list = []
    

    class PageDetails:
        def __init__(self, title, text, chapter,storynum):
            self.title = title #The title is both the title of the story and of the chapter
            self.text = text
            self.chapter = chapter
            self.storyNumber = storynum


    def add_page_details(self, title, text, chapter, storynum):
        page_details = self.PageDetails(title, text, chapter, storynum)
        self.page_details_list.append(page_details)


    def take(self, storynum):
        matching_page_details = []
        # Iterate through the list of PageDetails objects
        for page_details in self.page_details_list:
            # Check if the storynum matches
            if page_details.storyNumber == storynum:
                matching_page_details.append(page_details)  # Add matching PageDetails object to the list
        # If matching_page_details list is empty, return None or "Nothing Here"
        return matching_page_details  # Return the list of matching PageDetails objects
            
        
#Random Initialized Variables
y=0
x=0
page_array=[]
story_array=[]
soup=0

# driver=webdriver.Chrome()
# driver.get("https://www.fimfiction.net/manage/local-settings")
# checkbox = driver.find_element(By.NAME,"view_mature")
# checkbox.click()



#starting place for the webscraper/controlling variables
storynum=25199
chapnum=1
chapTotal=0
count_to_scrape = 500
my_story = Story(storynum=storynum) 
cookie = {'view_mature': "true"}

#the appropriate url for each story
while x<=count_to_scrape:
    chapter_code = 200
    story_code = 200 #potentially add selenium clicking portion right here with an if statement
    Story.storyNumber = storynum #Then if the thing pops up click and load the webpage like normal and it might recognize the mature access allowed
    chapnum=1
    time.sleep(random.randint(1,3))
    url="https://www.fimfiction.net/story/"+str(storynum)+"/"+str(chapnum)+"/"
    page_to_scrape=requests.get(url, cookies=cookie)
    story_code=page_to_scrape.status_code
    while chapter_code == 200:
        time.sleep(random.randint(1,3))
        
        chapter_code = page_to_scrape.status_code
        if chapter_code == 200:
            print(f"getting chapter {str(chapnum)} of story number {str(storynum)}")
            soup=BeautifulSoup(page_to_scrape.text, "html.parser")
            storytitles=soup.find("title")
            storytexts=soup.find("div",attrs={"class":"bbcode"}) 
            storytitles = storytitles.get_text()
            storytexts = storytexts.get_text()
            
            my_story.add_page_details(storytitles,storytexts,chapnum,storynum)
        chapnum = chapnum + 1      
        url="https://www.fimfiction.net/story/"+str(storynum)+"/"+str(chapnum)+"/"
        # The bulk of the code that extracts Title and Story Text
        # 200 is good status code, 404 means it doesn't exist
        page_to_scrape=requests.get(url, cookies=cookie)
          

    matching_details = my_story.take(storynum) # =list of page_details objects
    
    if story_code == 200:
        with open(f"C:\\Users\\joshu\\Desktop\\GitHub\\Stories\\{str(storynum)}.txt","w+", encoding="utf-8") as file:
            for obj in matching_details:
                single_story = "\n"+"\n"+"Title:    "+ obj.title +"\n Chapter:  "+ str(obj.chapter) + "\n" + obj.text
                file.writelines(single_story)

    x=x+1
    storynum=storynum+1

# driver.quit()

    









    



    

# base scraping code is below
""" 
    page_to_scrape=requests.get("https://www.fimfiction.net/story/552147/1/a-makeover-for-algernon-why-all-my-hamsters-are-goths/grownups-are-stupid")
    soup=BeautifulSoup(page_to_scrape.text, "html.parser")
    storytitles=soup.findAll("title")
    storytexts=soup.findAll("div",attrs={"class":"bbcode"})
"""

