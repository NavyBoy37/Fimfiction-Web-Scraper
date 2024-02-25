from bs4 import BeautifulSoup
import requests
import time
import random

print("boop***********************************************************************************************************************************")
print("\n")


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
error_code = 200


#starting place for the webscraper/controlling variables
storynum=460011
chapnum=1
chapTotal=0
count_to_scrape = 1
my_story = Story(storynum=storynum) 


#the appropriate url for each story
while x<=count_to_scrape:
    Story.storyNumber = storynum
    chapnum=1
    while error_code == 200:
        
        url="https://www.fimfiction.net/story/"+str(storynum)+"/"+str(chapnum)+"/"
    #The bulk of the code that extracts Title and Story Text
    #200 is good status code, 404 means it doesn't exist
        page_to_scrape=requests.get(url)
        error_code = page_to_scrape.status_code
        if error_code == 200:
            time.sleep(random.randint(0,3))
            soup=BeautifulSoup(page_to_scrape.text, "html.parser")
            storytitles=soup.find("title")
            storytexts=soup.find("div",attrs={"class":"bbcode"}) 
            storytitles = storytitles.get_text()
            storytexts = storytexts.get_text()
            
            
            
            my_story.add_page_details(storytitles,storytexts,chapnum,storynum)
            

             #testing
        
        chapnum = chapnum + 1


    x=x+1
    storynum=storynum+1


page_details = my_story.take(460011)
File_object = open(r"C:\Users\joshu\Desktop\GitHub\Stories\Stories.txt","w+")
#for obj in page_details:
File_object.writelines(page_details.title,page_details.text,page_details.chapter,page_details.storyNumber)
    









    



    

#base scraping code is below
""" 
    page_to_scrape=requests.get("https://www.fimfiction.net/story/552147/1/a-makeover-for-algernon-why-all-my-hamsters-are-goths/grownups-are-stupid")
    soup=BeautifulSoup(page_to_scrape.text, "html.parser")
    storytitles=soup.findAll("title")
    storytexts=soup.findAll("div",attrs={"class":"bbcode"})
"""

