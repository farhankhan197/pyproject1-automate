
# Automating DSAwithedSlash Challenge with Python

While its a delight to have 100 expert handpicked questions and Daily video solutions for the #DSAwithedSlash Challenge, Having to repeat the whole task of posting and organizing everything everyday can become a bit tedious after a while.

That's why this project aims to Automate tasks related to the DSAwithedSlash challenge. This tool simplifies the process, allowing you to focus on solving problems rather than managing files.



Contributions:
Contributions are welcome! If you have ideas for improvement or additional features, feel free to open an issue or submit a pull request.

Disclaimer:
This project is not affiliated with the official "DSAwithedSlash" challenge. It's an independent tool created to simplify the process of managing solution files.

License:

This project is licensed under the MIT License.


Instructions on Using the automator, Commands and more can be found below.

Happy coding, and may your solutions be as efficient as this automator! 🚀








## Features

- Day-based Input: Input the day on which you are attempting the solution, and the automator will organize files accordingly. Stay organized and track your progress effortlessly.

- Terminal Efficiency: Perform all tasks seamlessly from the terminal. No need to switch windows; stay focused on your coding workflow without interruptions.
- Effortless Setup: Quickly set up your workflow with a single input. Say goodbye to manual file creation and organization.
- Save solutions Locally : Automatically generate solution files for each challenge problem. No more creating and manually naming solution files.
- Web Scraping: Fetch the problem name, LeetCode URL, and LeetCode number based on the input day. Access relevant information directly without manual searches.
- Customization: Modify the directories to specify where to save automatically generated solution files. Also organize screenshots into separate folders. (more in detail in the Customization section)
- Time-saving: Boost your productivity by eliminating the repetitive task of creating files for each challenge. Spend more time solving problems and honing your skills.

## Running Locally

- Clone the project

- Install Necessary Libraries / Skip if you have them already installed. 
- Selenium
```powershell
pip install selenium
```
- Pandas
```powershell
pip install pandas
```
- BeautifulSoup
```powershell
pip install beautifulsoup4
```
- Requests
```powershell
pip install requests
```
- PyAutoGUI
```powershell
pip install pyautogui
```

- if you had pre installed version of a module that is not working with this code, try updating it first.
command to update selenium for example -
```powershell
pip install selenium --upgrade
```

## Setting up the Environment

Modify the directories to specify where to save automatically generated solution files. Also organize screenshots into separate folders. 

- foldergen.py

  1) Open the foldergen.py script and in userdirectory copy and paste the path of the folder where you want to save your solutions and screenshots.

   2) Set your default screenshot saving location to desktop to avoid transferring extra images.

  3) Run the foldergen.py script. It will create 100 folders named Day 1-Day 100.

- pyproject.py
 
  1) Open the pyproject.py in an IDE and in line 17 in the sourcefolder variable, copy and paste the directory where your screenshots are saved (ideally set it to desktop).

  2) In line 18 in the userdirectory variable, copy and paste the path of the directory you created a 100 folders in using foldergen.py
   (or you can just copy paste the path you defined in the directory variable of the foldergen.py script).

   3) Done


## Using the Script
- After setting up the environment, run the pyproject.py file.
- It will ask you for an input for the Day of the Challenge on which you want to operate.
- Input value in integer and in range(1 to 100).
- It will scrape relevant data and present it to you so that you can read the problem and know what problem you are going to be working with.

## Commands
- 'new javasol' :
 
  creates a new java solution with the code that you input in the terminal after executing the command. Pressing Enter twice means you have finished writing code and it will save that file locally in the folder on which day you were solving the problem.
  
  (for ex: if you were operating on day 1 problem, the solution will be stored in "{directory specified in foldergen.py}/Day 1)

  Overwrites any pre-existing solutions too.

- 'test javasol' :

   opens leetcode website, selects java as the language and pastes your solution so that you can either test or submit your solution.

- 'solution' : 

     opens edSlash's Solution Website for the problem in question.

- 'move ss' :

     Moves screenshots from sourcefolder to the folder of the day on which you are operating.   


- 'caption' :

     Prints out a postable caption with all the necessary tags and variable string entries.

     The string can be found and modified at line 96 of the pyproject.py file.

- 'done' :

    Exit the Script.     
