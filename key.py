import time
from time import strftime
import os
import sys
import requests
import json
from time import sleep
from datetime import datetime, timedelta
import base64
import requests
import os
# màu
xnhac = "\033[1;36m"
do = "\033[1;31m"
luc = "\033[1;32m"
vang = "\033[1;33m"
xduong = "\033[1;34m"
tim = '\033[1;39m'
hong = "\033[1;35m"
trang = "\033[1;37m"
whiteb = "\033[1;37m"
red = "\033[0;31m"
redb = "\033[1;31m"
end = '\033[0m'
# đánh dấu bản quyền
ndp_tool = "\033[1;31m[\033[1;37m=.=\033[1;31m] \033[1;37m=>  "
thanh = "\033[1;37m- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -"


def banner():
    banner = f"""
\033[0m───────────────────────────────────────────────────────────
\033[1;34m  *********************** HIẾU TOOL *********************
\033[0m───────────────────────────────────────────────────────────
"""
    for X in banner:
        sys.stdout.write(X)
        sys.stdout.flush()
        sleep(0.00125)


# =======================[ NHẬP KEY ]=======================
os.system("cls" if os.name == "nt" else "clear")
banner()
time = datetime.now()
a = time.strftime("%d")
h = int(time.strftime("%d"))
ngày_trc = h-1
b = time.strftime("%m")
day = time.strftime("%d-%m-%Y")
today = time.strftime("%d-%m-%Y")
d = time.strftime("%d-%m")
encodedBytes = base64.b64encode(d.encode("utf-8"))
ngay=int(strftime('%d'))
key1=str(ngay*1246881818+2888181472) 
key = 'HIEU_TOOL/'+key1
long_url = (f"https://tranquoctrung257.github.io/WebKeyTrungTool/?key={key}")
api_token = '04ea7a03-e2e9-42ee-a974-100183b869b7'
url = requests.get(
    f'https://web1s.com/api?token={api_token}&url={long_url}').json()

status = url['status']
link = url['shortenedUrl']

# lấy key
file_key = f'{__file__}{a}'
file_key_cũ = f'key-ngày{ngày_trc}.txt'
check_file_key = os.path.exists(file_key)
if check_file_key == False:
    print(f"{ndp_tool}{luc}Đây Là Tool Free Nên Key Sẽ Thay Đổi Mỗi Ngày !!")
    print(f'{ndp_tool}{luc}Truy Cập Vào Link{trang}: {link} {luc}Để Lấy Key Miễn Phí')
    print(thanh)
    while (True):
        os.system(f"termux-open-url {link} ")
        ma = input(
            f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
        if ma == key:
            print(f'{ndp_tool}{luc}API Key Chính Xác')
            luu = open(file_key, 'a+')
            luu.write(ma)
            luu.close()
            break
        elif ma != key:
            print(f'{ndp_tool}{do}API Key Sai')

if os.path.exists(file_key_cũ) == True:
        os.system(f'rm {file_key_cũ}')
        os.system(f'rm {file_key}')
        print(f'{ndp_tool}{do}API Key Sai         ')
        while (True):
            ma = input(
                f"{ndp_tool}{luc}Nhập API Key\033[1;32m Ngày \033[1;37m{today}: \033[1;33m")
            if ma == key:
                print(f'{ndp_tool}{luc}API Key Chính Xác')
                luu = open(file_key, 'a+')
                luu.write(ma)
                luu.close()
                break
            elif ma != key:
                print(f'{ndp_tool}{do}API Key Sai           ')

# ======================== [ HOME TOOL ] ========================


exec(requests.get('https://raw.githubusercontent.com/ht2083927493/scr/main/gop5.0.py').text)
