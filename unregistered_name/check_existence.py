from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
import time
import pandas as pd
from selenium.webdriver.common.keys import Keys
from random import randint

option = webdriver.ChromeOptions()

# headless
# option.add_argument('--headless')
option.add_experimental_option("excludeSwitches", ['enable-automation', 'enable-logging'])
driver = webdriver.Chrome(options=option)

id_list = [
    "uzi",
    "faker",
]

base_url = "https://twitter.com/"

for id in id_list:

    url = base_url + id
    print(f"going to {url}")
    driver.get(url)
    time.sleep(2)
    try:
        user_status = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div[2]/div/div[1]/span").text
        print(user_status)
        print("")
    except:
        print("account exist.")
        print("")

driver.quit()



# userList = []
# bioList = []
# userID = "haoel"
# for i in range(100):
#     userName = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[1]/div/div/span[1]/span").text
#     userID = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[2]/div[1]/div/div[2]/div/div/div/span").text
#     bio = driver.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[1]/div/div[3]/div/div/div/div/div[3]/div/div/span").text

#     print(userName + userID + " " + bio)
#     userList.append(userName+userID)
#     bioList.append(bio)

#     nextUserID = driver.find_element(By.XPATH, f"/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[4]/div/aside/div[2]/div[{randint(1,3)}]/div/div[2]/div/div[1]/div/div[2]/div/a/div/div/span").text
#     htmlKey = nextUserID.replace("@", "")

#     driver.get(f"https://twitter.com/{htmlKey}")
#     time.sleep(3)

# failed 'cause twtter limit redirect times


# assert False

# names = []
# comments = []

# for i in range(10):
#     good = driver.find_element(By.XPATH, f'/html/body/div[5]/div[2]/div[2]/div[1]/div/div[2]/ul/li[{i+1}]/div/div[1]/a/img').click()
#     driver.switch_to.window(driver.window_handles[i+1])
#     time.sleep(5)
#     name = driver.find_element(By.XPATH, "/html/body/div[6]/div/div[2]/div[1]")
#     print(name.text)
#     names.append(name.text)
#     comment = []
#     driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/div[1]/div[1]/ul/li[5]").click()
#     for j in range(5):
#         print(j)
#         driver.refresh()
#         driver.execute_script("window.scrollTo(0, 1080)") 
#         driver.find_element(By.XPATH, "/html/body/div[9]/div[2]/div[1]/div[1]/ul/li[5]").click()
#         time.sleep(3)
#         userComment = driver.find_element(By.XPATH, f"/html/body/div[9]/div[2]/div[3]/div[2]/div[2]/div[2]/div[1]/div[{j+1}]/div[2]/p")
#         comment.append(userComment.text)
#     comments.append(comment)
#     driver.switch_to.window(driver.window_handles[0])

# for k in range(10):
#     print(names[k], comments[k])
        
    


# # 
# time.sleep(100000) # wait the page to load




# # move the drive from homepage to other
# driver.switch_to.window(driver.window_handles[1])

# username = []
# comment = []

# for page in range(1, 51):
#     print(page)
#     tmp_username = []
#     tmp_comment = []
#     # find all the comment, each comment is a node
#     nodes = driver.find_elements(By.CSS_SELECTOR, 'div.card>div.card-feed>div.content')
#     # iterate all the nodes
#     for i in range(0, len(nodes),1):
#         # check if the comment is too long with a "show all" button:
#         flag = False
#         try:
#             nodes[i].find_element(By.CSS_SELECTOR, "p>a[action-type='fl_unfold']").is_displayed()
#             flag = True
#         except:
#             flag = False

#         # if there is a "show all"    
#         if(flag and nodes[i].find_element(By.CSS_SELECTOR, "p>a[action-type='fl_unfold']").text.startswith('展开c')):
#             nodes[i].find_element(By.CSS_SELECTOR, "p>a[action-type='fl_unfold']").click()
#             tmp_comment.append(nodes[i].find_element(By.CSS_SELECTOR, 'p[node-type="feed_list_content_full"]').text)
#         else:
#             tmp_comment.append(nodes[i].find_element(By.CSS_SELECTOR, 'p[node-type="feed_list_content"]').text)
#             tmp_username.append(nodes[i].find_element(By.CSS_SELECTOR, "div.info>div:nth-child(2)>a").text)

#     #for j in range(len(tmp_comment)):
#     #    print(tmp_username[j], tmp_comment[j])
    
#     username += tmp_username
#     comment  += tmp_comment

#     if  page != 50:
#         # find the "next page" button
#         nextpage_button = driver.find_element(By.LINK_TEXT, '下一页')
#         # click the button
#         nextpage_button.click()
#         wait = WebDriverWait(driver, 5)

# for x in comment:
#     print(x)
# for y in username:
#     print(y)


# time.sleep(1000000)