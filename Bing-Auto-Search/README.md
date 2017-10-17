# Overview:
this is an auto-searcher for bing used on Microsoft Edge on Windows 10

## Setup:

### 1: Install python
If you do not have python installed follow instuructions to download and install python on your desktop  
`https://www.python.org/downloads/release/python-361/`

### 2: install python selenium
run this in command line   
`pip install -U selenium`

### 3: install MicrosoftWebDriver
download and install Microsoft web driver
`https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/`

### 4: Create new folder
create a new folder on desktop and add `words.txt` and `bingEngine.py` to file  
Add Microsoft web Driver to same file. 

---

# Execution:

Open 'bingEngine.py' and edit Edge to have correct file location of webDriver  
e.g.  
 `Edge = webdriver.Edge("C:/Users/usana/Desktop/Extra C/python/MicrosoftWebDriver.exe")`  
 //line 14

Save and run

