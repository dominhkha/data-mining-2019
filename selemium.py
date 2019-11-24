from selenium import webdriver 
from time import sleep 
import sys
import requests
from bs4 import BeautifulSoup
import re
from collections import defaultdict
import pandas as pd
import facebook;

cate_dict = {
    "music": [" hát ","âm thanh", "hat", "bolero","karaoke", "nhạc", "cải lương", "song ca","thơ ca","yêu thơ","điệp khúc","phượt","tình thơ"],
    "sport and travel": ["football","golf","bóng chuyền", "volleyball", "thể thao", "bóng đá", "du lịch", "travel",'karate', "MU", "chelsea", "ronaldo","gải trí","trip"," ảnh ","real madrid"],
    "comic and film": ["diễn viên","conan", "doreamon", "truyện", "batman", "superman", "phim", "ant man", "spider man", "truyen", "siêu nhân","du ký"],
    "jobs": ["job","lương","làm thêm",'ship tìm người',"part-time",'full-time',"fresher", "việc", "viec", " tuyen", "tuyển", "lao động", "lao dong", "thiết kế", "thực tập","freelancer","nghề","dọn nhà"],
    "social learning": ["tốt nghiệp","ielts","toeic","vật lý","học tập","tài liệu","academy","english","course","sách","giải tích","luật","hướng dẫn","giải đáp","toán","gia sư" , "tuyển sinh", "ôn thi", "luyện thi", "learning","tiếng anh","dạy","công nghệ",'hack'],
    "love": ["hip hop","tâm sự",'young','teen',"theanh28","làm quen","tìm bạn","bạn đời","tình cảm", "ngôn tình","trái tim", "hạnh phúc", "hanh phuc", "girl", "hot boy", "sexy","oppa","buồn vui","thẩm mỹ","spa","adam","eva","hẹn hò","love","thư giãn","gái đẹp","trai đẹp","troll","gái xinh","gay ","nỗi buồn","beatvn"],
    "suport": ["nhân ái","nhan ai","thiện nguyện", "tình nguyện", "tình thương", "hỗ trợ","giúp đỡ","thiện tâm","từ thiện","mồ côi","khuyết tật"],
    "health and family": ["dòng họ","bếp","đồng hương","lễ","trẻ em","đông y","khỏe", "chăm sóc", "dưỡng", "cận thị", "lão", "gia đình","tổ quốc", "quê hương","phật","chúa","khổ nạn","maria","công giáo","a di","đạo","tín ngưỡng","cầu nguyện","bồ tát","nam mô","quan âm","miền tây","tâm linh","con cháu","thuốc","ung thư","quê","cụ","chùa","làm đẹp","phẫu thuật","ơn nghĩa","món ăn","món ngon","ẩm thực","y học","công giáo","giáo lý","xem bói","mẹ",'tử vi'],
    "new": ["tin xã hội","tin tức", "new", "vietnamnet", "vnexpress", "tạp chí", "báo", "thời tiết","thông tin","tin mới","cười","hài","fun","giải trí","tin nóng","hóng hớt","hóng biến"],
    "gaming": ["league of kings","lol", "moba", "survival", "liên minh", "liên quân", "pubg", "dota", "game", "kiếm vương","pewpew","mixi","mộng tam quốc","casino","fifa"],
    "buy and sell": ["thời trang","uy tín","rao vặt","điện thoại","chính hãng","mỹ phẩm","tiki","lazada","tạp hóa","nhà trọ","lẻ","sỉ","giảm giá","xiaomi","iphone","market","cho thuê","bất động sản","giao thương","quần"," áo ","giày","sale","hàng", "chợ", "mua ", "bán", "shop", "thời trang", "rao vặt", "dịch vụ", "thanh lý","nhà đất","giao dịch","kinh doanh",'cũ','đại lý',"siêu thị",'sieuthi',' rẻ','đấu giá','free'],
    "school and class": ["giáo viên","9","12","school","university","lớp", "lop", "khoá",  "trường","THPT","thpt","12b1","10b1","trung học","sinh viên","học sinh"],    
    "club": ["kết bạn","team","community","chia sẻ","clb", "cộng đồng","fc","fan", "hội", "friends", "nhóm", "fc", "bạn bè","group","tình bạn","việt nam","hà nội","vietnam","club","nhậu","bạn hữu","kết nối","confession","anh em"],
}
usr='0334962631'
pwd='man050699'

# 01262706021
# qsn21793@zasod.com
driver_exe=r'C:\Users\Dell\Downloads\chromedriver_win32\chromedriver.exe'
driver = webdriver.Chrome(driver_exe) 

base_url= r'https://www.facebook.com/'
driver.get('https://www.facebook.com/') 


  
username_box = driver.find_element_by_name('email') 
username_box.send_keys(usr)

  
password_box = driver.find_element_by_name('pass') 
password_box.send_keys(pwd) 
  
login_box = driver.find_element_by_css_selector('[type="submit"]') 
login_box.click()

dict__ = {'__label__18-24': {'sport and travel': 0, 'buy and sell': 0, 'health and family': 0, 'jobs': 0, 'love': 0,
                            'social learning': 0, 'suport': 0, 'new': 0, 'comic and film': 0, 'music': 0, 'gaming': 0, 'school and class': 0,"club":0,"general":0}}

f = open("test.txt")
contents=f.readlines()
first_line=int(sys.argv[1])
last_line=int(sys.argv[2])

def checkInside(category, name):
    return any(x in name for x in category)
df = pd.DataFrame.from_dict(dict__, orient='index')
try:
    for index,line in enumerate(contents[first_line: last_line]):
        line=line.strip().split(" ")
        dict_ = defaultdict(dict)
        label=index+first_line
        index=index+first_line
        for i in cate_dict.keys():
            dict_[label][i] = 0
        dict_[label]["general"] = 0
        if(len(line)>30): line=line[:30]
        for i in line:
            print(i)
            url = base_url+"groups/"+i
            driver.get(url)
            sleep(1)
            try: 
                a=driver.find_element_by_css_selector("#seo_h1_tag a")
                name = a.text.strip().lower()
                flag=False
                for j in cate_dict.keys():
                    if(checkInside(cate_dict[j],name)):
                        dict_[label][j] += 1
                        flag=True
                        print(str(index)+" - "+name+" -> "+j)
                        break
                if flag==False:
                    dict_[label]["general"] += 1
                    print(name+" - general")
            except:
                print("not Found")
                
        
        df1 = pd.DataFrame.from_dict(dict_, orient='index')
        df = pd.concat([df, df1],sort=False)
    df=df.iloc[1:]
    name="data_"+str(first_line)+"_"+str(last_line)+".csv"
    df.to_csv(name,encoding='utf-8-sig')
except :
    df=df.iloc[1:]
    name="data_"+str(first_line)+"_"+str(last_line)+"err.csv"
    df.to_csv(name,encoding='utf-8-sig')
