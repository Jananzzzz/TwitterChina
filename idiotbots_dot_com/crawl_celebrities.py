# don't keep using i as the variable name, it's not a good habit.

import requests
from lxml import etree
from lxml.etree import tostring
import json

base_url = "https://www.idiotbots.com"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36"
}

type_list = [
    "Overall_Ranking",
    "Media",
    "Editorials",
    "Finance",
    "Gossip",
    "Anime",
    "Girls",
    "Run",
    "Porn",
    "Uncategorized",
]

popularity_ranking_site = "https://www.idiotbots.com/twiranks?lg=zh&category=999&ranksort=flw"
activity_ranking_site = "https://www.idiotbots.com/twiranks?lg=zh&ranksort=stt"

response1 = requests.get(popularity_ranking_site, headers=header)
html1 = etree.HTML(response1.text)
response2 = requests.get(activity_ranking_site, headers=header)
html2 = etree.HTML(response2.text)

activity_ranking_url_list = []
popularity_ranking_url_list = []

for i in range(2):
    for j in range(5):
        popularity_ranking_url_list.append(base_url + html1.xpath(f'/html/body/main/div/div/div/div/div/div[2]/table/tr[{i+1}]/td[{j+1}]/a')[0].attrib['href'])
        activity_ranking_url_list.append(base_url + html2.xpath(f'/html/body/main/div/div/div/div/div/div[2]/table/tr[{i+1}]/td[{j+1}]/a')[0].attrib['href'])

for i in range(10):
    file_name = "C:/Users/16591/Desktop/Github/TwitterChina/idiotbots_dot_com/data/popularity/" + type_list[i] + ".json"
    with open(file_name, "w") as f:
        response = requests.get(popularity_ranking_url_list[i], headers=header)
        html = etree.HTML(response.text)
        dict = {}
        for j in range(1,52):
            if j != 6:
                try:
                    name = html.xpath(f"/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[{j+1}]/td[2]/a")[0].text
                    sub_url = html.xpath(f'/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[{j+1}]/td[2]/a')[0].attrib['href']
                    url = base_url + sub_url

                    response1 = requests.get(url, headers=header)    
                    html1 = etree.HTML(response1.text)
                    link = html1.xpath("/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/th[2]/a")[0].attrib['href']
                    print(name)
                    print(link)
                    dict[name] = link
                except:
                    pass
        # dict to json, write to file, indent=4, encoding="utf-8"
        json.dump(dict, f, indent=4, ensure_ascii=False)
        print(f"create popularity{type_list[i]} file successfully. {i+1}/10")
        f.close()

for i in range(10):
    file_name = "C:/Users/16591/Desktop/Github/TwitterChina/idiotbots_dot_com/data/activity/" + type_list[i] + ".json"
    with open(file_name, "w") as f:
        response = requests.get(activity_ranking_url_list[i], headers=header)
        html = etree.HTML(response.text)
        dict = {}
        for j in range(1,52):
            if j != 6:
                try:
                    name = html.xpath(f"/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[{j+1}]/td[2]/a")[0].text
                    sub_url = html.xpath(f'/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[{j+1}]/td[2]/a')[0].attrib['href']
                    url = base_url + sub_url
                
                    response1 = requests.get(url, headers=header)    
                    html1 = etree.HTML(response1.text)
                    link = html1.xpath("/html/body/main/div/div/div/div/div/div[2]/div[1]/table/tbody/tr[1]/th[2]/a")[0].attrib['href']
                    print(name)
                    print(link)
                    dict[name] = link
                except:
                    pass
        # dict to json, write to file, indent=4, encoding="utf-8"
        json.dump(dict, f, indent=4, ensure_ascii=False)
        print(f"create activity_{type_list[i]} file successfully. {i+1}/10")
        f.close()








