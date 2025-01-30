
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

        if "app_name" in active_windows_list or "app_name" in all_windows :
            os.chdir(path+"/images")
            url_or_image = os.listdir()
            for i in range(3):
                image_url = random.choice(url_or_image)
                os.system(image_url) 
                time.sleep(0.50)
                #* websiteler random şekilde çıkarılıyor ki anlaşılmasın.
                #* websiteler çok hızlı yüklenmemesi için 0.50 olarak ayarlandı.
                #!toplam 3 tane tur atıyor. yani toplam 1.5 saniye websiteler gözüküyor. burdaki sleep kısmını değiştirirseno süre değişir

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
    time.sleep(1.80)
    main(path)
#* 1.80 sn de bir kontrol ediyor.

