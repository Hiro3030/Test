import bs4
import requests
import time
import urllib.request

Target_URL_ikkodate = 'https://www.fudousan.or.jp/system/?act=l&type=14&pref=24&stype=l&city%5B%5D=24201&city%5B%5D=24202&city%5B%5D=24205&city%5B%5D=24207&city%5B%5D=24214&city%5B%5D=24303&city%5B%5D=24324&city%5B%5D=24341&city%5B%5D=24343&city%5B%5D=24344&pl=l&ph=1&pu=1&acl=l&ach=h&atl=l&ath=h&n=20&p=1&v=on&s=n'
Target_URL_tochi = 'https://www.fudousan.or.jp/system/?act=l&type=16&pref=24&stype=l&city%5B%5D=24201&city%5B%5D=24202&city%5B%5D=24205&city%5B%5D=24207&city%5B%5D=24214&city%5B%5D=24303&city%5B%5D=24324&city%5B%5D=24341&city%5B%5D=24343&city%5B%5D=24344&pl=l&ph=1&pu=1&acl=l&ach=h&n=20&p=1&v=on&s=n'
Target_URL_jigyou = 'https://www.fudousan.or.jp/system/?act=l&type=17&pref=24&stype=l&city%5B%5D=24201&city%5B%5D=24202&city%5B%5D=24205&city%5B%5D=24207&city%5B%5D=24214&city%5B%5D=24303&city%5B%5D=24324&city%5B%5D=24341&city%5B%5D=24343&city%5B%5D=24344&pl=l&ph=h&pu=1&aul=l&auh=h&n=20&p=1&v=on&s=n'
headers = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.122 Safari/537.36"}
        
columns_ikkodate = ["url", "price", "place", "access", "unit", "age", "imageurl"]
columns_tochi = ["url", "price", "place", "access", "square", "imageurl"]
columns_jigyou = ["url", "price", "place", "access", "type", "age", "imageurl"]


resp = requests.get(Target_URL_ikkodate, headers=headers)
time.sleep(5)
resp.raise_for_status()

soup = bs4.BeautifulSoup(resp.text, "html.parser")
entry = soup.find(class_="result_all_part")
first_site = entry.find("a")
url_row = first_site.get("href")
url_com = url_row.lstrip(".")
url = "https://www.fudousan.or.jp/system" + url_com

price = entry.find_all("td")[2].text
place = entry.find_all("td")[3].text
access = entry.find_all("td")[4].text
unit = entry.find_all("td")[7].text
age = entry.find_all("td")[8].text
imgurl = entry.find("img")['src']

datapath = "./Data/"

try:
    with urllib.request.urlopen(imgurl) as web_file, open(datapath, 'wb') as local_file:
        time.sleep(1)
        local_file.write(web_file.read())
except urllib.error.URLError as e:
    print(e)





# first_read = "https://www.mercari.com" + first_site
# info = requests.get(first_read, headers=headers)
# time.sleep(1)
# info.raise_for_status()
# parse = bs4.BeautifulSoup(info.text, "html.parser")
# result = parse.find(class_ = "item-box-container l-single-container")



# token = "JMG8yIXiIG6TcyZdDKqQrAlnKXbJusnP7fmnHnG1SjB"
# url = "https://notify-api.line.me/api/notify"
# headers = {"Authorization": "Bearer " + token}
# payload = {"message": "テストメッセージだよ"}
# requests.post(url, headers=headers, data=payload)
