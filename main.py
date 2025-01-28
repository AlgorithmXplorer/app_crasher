
import os 
import pygetwindow
import time
import json

path = "c:/Users/VICTUS/Masaüstü/abcd"

def main(repo_folder:str):
    def inner(path):
        windows = pygetwindow.getActiveWindowTitle()
        windows = windows.split(" - ")
        if "valo_crasher" in windows:
            os.chdir(path+"/images")
            url_or_image = os.listdir()
            for image_url in url_or_image:
                os.system(os.path.abspath(image_url)) 
    def json_reader(path):
        new_path = path+"/is_it_allow.json"
        with open(new_path,"r",encoding="utf-8") as file:
            datas = json.load(file)
            
        with open(new_path,"w",encoding="utf-8") as file:
            json.dump(datas,file,indent=4,sort_keys=False)
        allow = datas["key"].lower()
        if allow == "evet":
            return True
        else:
            return False
            
        
    print(json_reader(repo_folder))


main(path)


def controller():
    pass



