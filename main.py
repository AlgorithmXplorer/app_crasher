
import os 
import pygetwindow
import time
import json
import random

path = "The path of the folder containing the permission JSON file and websites"

def main(repo_folder:str):
    os.chdir(repo_folder)#* The function switches to the received data folder

    def inner(path):
        try:
            active_windows = pygetwindow.getActiveWindowTitle()
            active_windows_list = active_windows.split(" - ")
            all_windows = pygetwindow.getAllTitles()
        except:
            all_windows = pygetwindow.getAllTitles()
            active_windows_list = []
        #* We used two different methods to receive all kinds of Windows data
        #! Since active windows are received as a string, we used split.

        if "app_name" in active_windows_list or "app_name" in all_windows :
            os.chdir(path+"/images")
            url_or_image = os.listdir()
            for i in range(3):
                image_url = random.choice(url_or_image)
                os.system(image_url) 
                time.sleep(0.50)
                #* Websites are displayed randomly so that they are not noticed
                #* The websites were set to 0.50 to prevent them from loading too fast.
                #! It completes a total of 3 cycles, meaning the websites are visible for 1.5 seconds in total. If you change the sleep duration here, the total time will also change.

            os.chdir("..")
            #* To open the websites, we directed the os module to their location
            #! At the end, we navigated back because the general folder contains the allow.json file besides the websites.


        
    def json_reader(path):
        json_file_path = path+"/is_it_allow.json"
        with open(json_file_path,"r",encoding="utf-8") as file:
            datas = json.load(file)
        #* A new path was written to read the JSON data, and data was fetched with the 'r' parameter for read permission.



        with open(json_file_path,"w",encoding="utf-8") as file:
            json.dump(datas,file,indent=4,sort_keys=False)
        allow = datas["key"].lower()
        if allow == "yes":
            return True
        else:
            return False
        #* If the user writes 'yes' in the key section, a 'True' value is sent for the application to function


    allow = json_reader(repo_folder)
    if allow:
        inner(repo_folder)

while True:
    time.sleep(1.80)
    main(path)
#* It checks every 1.80 seconds.

