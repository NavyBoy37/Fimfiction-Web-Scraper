

https://www.fimfiction.net/story/482117/3/

- The first set of numbers represents the story
- The second set of numbers represents the chapter of the story
- Both of these must be present to give useful information even if it is chapter 1

1. Make text and title extractor (potentially author later)
2. Make it search through each chapter of a story and cancel when it can't find useful information on the chapter after the last that was written
3. Once done with story, bump up the number of the story and repeat the chapter search loop.

Next up https://www.fimfiction.net/story/25148/2/all-american-girl/chapter-one-equine-american
with kimi no sain  
:D

error:  

  File "C:\Users\joshu\Desktop\GitHub\Fimfiction Web Scraper\web_scraper.py", line 94, in <module>
    file.writelines(single_story)
  File "C:\Users\joshu\AppData\Local\Programs\Python\Python311\Lib\encodings\cp1252.py", line 19, in encode
    return codecs.charmap_encode(input,self.errors,encoding_table)[0]
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
UnicodeEncodeError: 'charmap' codec can't encode character '\u014d' in position 0: character maps to <undefined>