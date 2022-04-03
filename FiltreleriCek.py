
import xlsxwriter
from bs4 import BeautifulSoup
from selenium import webdriver
import os
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

ilanlist=[]
konutlist=[]
illist=[]





#Webdriver settings for selenium

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "normal"  #  Waits for full page load
#caps["pageLoadStrategy"] = "none"   # Do not wait for full page load
chromeOptions= webdriver.ChromeOptions()
#chromeOptions.add_argument("--headless")
chromeOptions.add_argument("--no-sandbox")
chromeOptions.add_argument("start-maximized")
chromeOptions.add_argument("disable-infobars")
chromeOptions.add_argument("--disable-extensions")
current_path=os.path.dirname(os.path.abspath(__file__))+"\chromedriver.exe"
current_path=current_path.replace("\\","\\\\")
chrome=webdriver.Chrome(executable_path=str(current_path),options=chromeOptions,desired_capabilities=caps)
link=("https://www.sahibinden.com/kategori/emlak-konut")


chrome.get(link)
r=chrome.page_source
soup=BeautifulSoup(r,"lxml")

# İlan tipleri

ilantip=soup.find("div",attrs={"class":"sahibindenSelect closed categoryArea"})
ilantipler=ilantip.find_all("li")
for i in ilantipler:
    ilanlist.append(i.text)


# Konut Tipleri


konutlar=soup.find("select",attrs={"name":"category","id":"category","class":"selectedOption"})
for i in konutlar:
    konutlist.append(i.text)

# İller

iller= soup.find("select",attrs={"class":"city selectedOption","name":"address_city","id":"address_city"})
count=1
for i in iller:
    a=i.text
    a=a.replace("\n","")
    a=a.replace("\t","")
    a=a.replace(" ","")
    if count%2==0:
        illist.append(a)
    count+=1


chrome.quit()

workbook = xlsxwriter.Workbook("main.xlsx")
worksheet = workbook.add_worksheet()

worksheet.write("A1","Satılık")
worksheet.write("B1","Konut")
worksheet.write("C1","İl")
worksheet.write_column('CA10', illist)

worksheet.data_validation('A1',{'validate':'list','source':ilanlist})
worksheet.data_validation('B1',{'validate':'list','source':konutlist})
worksheet.data_validation("C1",{'validate': 'list', 'source': '=$CA$10:$CA$91'})
workbook.close()

