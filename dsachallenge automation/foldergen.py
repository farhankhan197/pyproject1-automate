import os

def foldergen(directory):
    for day in range(1, 101):
        foldername = f"Day {day}"
        folderpath = os.path.join(directory, foldername)
        os.makedirs(folderpath)

directory = r"C:\Users\Lenovo\Desktop\Code\Python\Projects\DSAwithedSlash\github"
foldergen(directory)
