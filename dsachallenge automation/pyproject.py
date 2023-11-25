
import pandas as pd
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
import pyautogui
import pandas as pd
import requests
from bs4 import BeautifulSoup
import webbrowser
import os
import getpass
import shutil



sourcefolder = r"C:\Users\Lenovo\Desktop"
userdirectory = r'C:\Users\Lenovo\Desktop\Code\Python\Projects\DSAwithedSlash\github'

searchText = input("Enter Day of DSAwithedSlash Challenge: ")
def move_images(sourcefolder, userdirectory):
    if not os.path.exists(sourcefolder):
        print(f"Source folder '{sourcefolder}' does not exist.")
        return

    if not os.path.exists(userdirectory):
        os.makedirs(userdirectory)

    files = os.listdir(sourcefolder)

    for file in files:
        source_path = os.path.join(sourcefolder, file)

        if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif')):
            destination_path = os.path.join(f'{userdirectory}\\Day {searchText}', file)

            shutil.move(source_path, destination_path)
            print(f"Moved '{file}' to '{destination_path}'")
            

url = "https://edslash.com/dsa-with-edslash-leetcode-100-days/"
response = requests.get(url)
htmlContent = response.content
soup = BeautifulSoup(htmlContent, 'html.parser')

h2Tags = soup.find_all('h2')



for i in h2Tags:
    if searchText.lower() in i.get_text().lower():
        print(f"Match for '{searchText}' found : {i.get_text()}\n")
        element_container = i.find_next(class_="elementor-widget-container")
        if element_container:
            print(f"Problem Name:{element_container.get_text()}\n")
            probname = element_container.get_text()
            anchortag = element_container.find('a')
            if anchortag:
                anchorUrl = anchortag.get('href')
                print(f"Leetcode URL: {anchorUrl}\n")
            else:
                print("No matching anchor tag found.\n")
        else:
            print("No match found for this h2 tag.\n")

df = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\Code\\Python\\Projects\\DSAwithedSlash\\table_1_1.csv')
inputTitle = probname
df['Title'] = df['Title'].str.strip().str.replace(" ", "")
inputTitle = inputTitle.strip().replace(" ", "")
df['Title'] = df['Title'].str.lower()
inputTitle = inputTitle.lower()
fildf = df[df['Title'].str.contains(inputTitle, na=False)]

if not fildf.empty:
    resultId = fildf['ID'].values[0]
    print(f"Leetcode Problem Number for {element_container.get_text()}is : {resultId}\n")
else:
    print(f"No entry found for the title '{element_container.get_text()}'.")

search_text = searchText.replace('/n','')
probname = probname.replace('\n','')



def delete_file(filename):
    try:
        os.remove(filename)
        print(f"{filename} has been deleted.")
    except FileNotFoundError:
        print(f"File {filename} not found.")
    except PermissionError:
        print(f"Permission denied: Unable to delete {filename}.")

pathjava = f'{userdirectory}\\Day {searchText}\\Day {search_text} {probname}.java'

a = f"""Day {search_text}/100 of the edSlash DSA Challenge on LeetCode!
Solved a problem on {probname}. (LeetCode {resultId}).
#DSAwithedSlash 
#CodingThinker
#DSASuccess 
#DSAChallenge
#CodingMilestone 
#Datastructures
#Algorithms"""
while True:
    user_input = input(f"""---------------------------------------ENTER A COMMAND------------------------------------------------
                       'new javasol'  : Enter a new Java Solution for Day {search_text}.
                       'test javasol' : Try Leetcode Test Cases for Day {search_text} Java Solution.
                       'solution'    : Open edSlash Solution for {probname}.
                       'move ss'     : Move Screenshots from Desktop to Designated Folder.
                       'caption'     : Print Caption for Day {search_text} Linkedin Post.
                       'done' to finish.
                       :""")

    if user_input.lower() == "done":
        print("Exiting...")
        break

    elif user_input.lower() == "solution":
            pstring = '-'.join(probname.lower().strip().split())
            url = f"https://edslash.com/leetcode-problem-{resultId}-{pstring}/"
            print(url)
            webbrowser.open(url)

    elif user_input=='move ss':    
            move_images(sourcefolder, userdirectory)

    elif user_input.lower() == "new javasol":
        delete_file(f'{userdirectory}\\Day {searchText}\\Day {search_text} {probname}.java')
        print("Enter Java Solution (press Enter twice to finish):")
        javaSol = ""
        while True:
            line = input()
            if line == "":
                break
            javaSol += line + "\n"
        with open(pathjava, 'w') as file:
            file.write(javaSol)
        print(f'-----------Day {search_text} Java Solution Created----------')   

    elif user_input.lower() == "test javasol":
        driver = webdriver.Chrome()
        driver.get(anchorUrl)
        time.sleep(1)
        time.sleep(6)
        svg_element = driver.find_element(By.XPATH,r"/html/body/div[1]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/button/div/div")
        svg_element.click()
        time.sleep(2)
        java_option = driver.find_element(By.XPATH,r'/html/body/div[1]/div[2]/div/div/div/div/div[3]/div/div[1]/div/div/div/div[2]/div[1]/div[1]/div/ul/li[2]/div/div')
        java_option.click()
        time.sleep(4)
        textarea = driver.find_element(By.TAG_NAME,'textarea')
        textarea.click()
        pyautogui.hotkey('ctrl', 'a')
        time.sleep(1)
        pyautogui.press('backspace')
        filejava = f'{userdirectory}\\Day {searchText}\\Day {search_text} {probname}.java'
        with open(filejava, 'r') as file:
             filecontentjava = file.read()        
        textarea.send_keys(filecontentjava)
        waitbhai = getpass.getpass("PRESS ENTER TO FINISH")
        driver.quit()

    elif user_input.lower()=='caption':
         print(a)
    else:
            print("""Invalid command. Please enter one of the following:
                  'new javasol'
                  'test javasol'
                  'move ss'
                  'solution'
                  'caption'
                  or 'done'.""")



