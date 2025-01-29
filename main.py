
import os 
import pygetwindow
import time
import json
import datetime
import random

path = "C:/Users/VICTUS/Masaüstü/abcd"
# path = "izin json dosyasını ve websiteleri içeren klasörün yolu"

def main(repo_folder:str):
    os.chdir(repo_folder)#* fonksiyon aldığı data klasörüne geçiş yapıyor.

    def inner(path):
        active_windows = pygetwindow.getActiveWindowTitle()
        active_windows_list = active_windows.split(" - ")
        all_windows = pygetwindow.getAllTitles()
        #* elimize her türlü windows verisi gelmesi için iki türlü metot kullandık
        #! aktif pencereler str verisi halinde geldiği için split kullandık

        if "valo_crasher" in active_windows_list or "valo_crasher" in all_windows :
            os.chdir(path+"/images")
            url_or_image = os.listdir()
            now = datetime.datetime.now()
            finish_run_time = now + datetime.timedelta(seconds=3)
            #* websiteler toplam 3 saniye boyunca gözükücek.

            while True:
                now_2 = datetime.datetime.now()
                if now_2.second == finish_run_time.second:
                    break
                else:
                    image_url = random.choice(url_or_image)
                    os.system(image_url) 
                    time.sleep(1.25)
                    #* websiteler random şekilde çıkarılıyor ki anlaşılmasın.
                    #* websiteler çok hızlı yüklenmemesi için 1.25 sn alındı

            os.chdir("..")
            #* websitelerinin açılabilmesi için os modülünü websitelerinin olduğu konuma götürdük.
            #! en sonda geri çıktık çünkü genel klasörde websitesi dışında allow.json dosyası var
        
    def json_reader(path):
        json_file_path = path+"/is_it_allow.json"
        with open(json_file_path,"r",encoding="utf-8") as file:
            datas = json.load(file)
        #*json verisini okumak için yeni bir path yazıldı ve izin verme durumu için "r" parametresi ile data alındı

        with open(json_file_path,"w",encoding="utf-8") as file:
            json.dump(datas,file,indent=4,sort_keys=False)
        allow = datas["key"].lower()
        if allow == "yes":
            return True
        else:
            return False
        #* kullanıcı key kısmına yes yazarsa uygulamanın çalışması için bir "True" verisi gödneriliyor

    allow = json_reader(repo_folder)
    if allow:
        inner(repo_folder)

while True:
    time.sleep(1.50)
    main(path)
#* 1.50 sn de bir kontrol ediyor.

