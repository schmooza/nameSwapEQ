#https://pythonguides.com/python-screen-capture/
#pip install webdriver-manager
#screen shot websites
from PIL import Image
from twill.commands import *
import pytesseract #ocr
from time import sleep
from selenium import webdriver #screenshot
from webdriver_manager.chrome import ChromeDriverManager # open web page
import pandas as pd

# driver = webdriver.Chrome(ChromeDriverManager().install())

# siteToScreenShot = "https://brisbanesde-qld.compass.education"
# website = siteToScreenShot
#
# driver.get(website)
# sleep(5) # lets it load


#
# driver.get_screenshot_as_file("images/role.png") # saves as an image


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'
ocrData = pytesseract.image_to_string(r'images/img.png')

ocrDataConverted = str(ocrData)


#converts to a text file
with open('outputCSV/outputStudentNames.txt', 'w') as f:
    f.write(ocrDataConverted)
read_file = pd.read_csv(r'outputCSV/outputStudentNames.txt')
read_file.to_csv(r'outputCSV/convertedToCSV/outputStudentNames.csv', index=None)
# converts to a csv file

df = pd.read_csv('outputCSV/convertedToCSV/outputStudentNames.csv')
# puts data into pandas data frame
nameListA = []


for n in df['Student']:
    x = n.split()
    x.reverse()
    print(x,"debug")
    nameListA.append(x)

print(nameListA)