import sqlite3
import matplotlib.pyplot as plt
from pypinyin import lazy_pinyin

def fetch_all_users(database):
    conn = sqlite3.connect(database)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM users;")
    users = cursor.fetchall()
    cursor.close()
    conn.close()
    return users


# check name and bio and location whether it contains chinese
def check_chinese_character(text):
    for ch in text:
        if u'\u4e00' <= ch <= u'\u9fff':
            return True
    return False
    
def check_japanese_character(text):
    # all katakana
    katakana = u'\u30A0-\u30FF'
    # all hiragana
    hiragana = u'\u3040-\u309F'
    for ch in text:
        if u"\u3040" <= ch <= u"\u30FF":
            return True
    return False

def check_korean_character(text):
    # all katakana
    katakana = u'\uAC00-\uD7AF'
    for ch in text:
        if u"\uAC00" <= ch <= u"\uD7AF":
            return True
    return False

# check location
def check_location(location):
    china_locations = ['guangzhou', 'jiangsu', 'hainan', 'guangdong', 'macau', 'henan', 'hunan', 'shanghai', 'ningxia', 'taiwan', 'hubei', 'hongkong', 'xinjiang', 'sichuan', 'china', 'gansu', 'guangxi', 'fujian', 'beijing', 'zhejiang', 'guizhou', 'yunnan', 'qinghai', 'shanxi', 'shandong', 'aomen', 'anhui', 'jilin', 'hainan', 'neimenggu', 'chongqing', 'tianjin', 'hebei', 'heilongjiang', 'xizang', 'xianggang', 'liaoning', 'jiangxi', 'tibet']
    china_locations_in_chinese_character = ['广州','江苏', '海南', '广东', '澳门', '河南', '湖南', '上海', '宁夏', '台湾', '湖北', '香港', '新疆', '四川', '中国', '甘肃', '广西', '福建', '北京', '浙江', '贵州', '云南', '青海', '山西', '山东', '澳门', '安徽', '吉林', '海南', '内蒙古', '重庆', '天津', '河北', '黑龙江', '西藏', '香港', '辽宁', '江西', '西藏']
    # split location by "," and "，"
    location0 = location.split(",")
    location1 = location.split(" ")
    for i in location0:
        if i.lower() in china_locations or i in china_locations_in_chinese_character:
            return True
    for j in location1:
        if j.lower() in china_locations or j in china_locations_in_chinese_character:
            return True
    if location is None:
        return False
    return False

def check_chinese(user):
    user["bio"] = user["bio"].replace("。", ".")
    user["bio"] = user["bio"].replace("、", ",")
    user["bio"] = user["bio"].replace("，", ",")
    user["bio"] = user["bio"].replace("；", ";")
    user["bio"] = user["bio"].replace("：", ":")
    user["bio"] = user["bio"].replace("？", "?")
    user["bio"] = user["bio"].replace("！", "!")
    user["bio"] = user["bio"].replace("（", "(")
    user["bio"] = user["bio"].replace("）", ")")
    user["bio"] = user["bio"].replace("【", "[")
    user["bio"] = user["bio"].replace("】", "]")
    user["bio"] = user["bio"].replace("《", "<")
    user["bio"] = user["bio"].replace("》", ">")
    user["bio"] = user["bio"].replace("“", "\"")
    user["bio"] = user["bio"].replace("”", "\"")
    user["bio"] = user["bio"].replace("‘", "\'")
    user["bio"] = user["bio"].replace("’", "\'")
    user["bio"] = user["bio"].replace("—", "-")
    user["bio"] = user["bio"].replace("～", "~")
    user["bio"] = user["bio"].replace("…", "...")
    user["bio"] = user["bio"].replace("￥", "$")
    user["bio"] = user["bio"].replace("＄", "$")
    user["bio"] = user["bio"].replace("％", "%")
    user["bio"] = user["bio"].replace("＆", "&")
    user["bio"] = user["bio"].replace("＊", "*")
    user["bio"] = user["bio"].replace("＋", "+")
    user["bio"] = user["bio"].replace("－", "-")
    user["bio"] = user["bio"].replace("／", "/")
    user["bio"] = user["bio"].replace("＝", "=")
    user["bio"] = user["bio"].replace("＠", "@")
    user["bio"] = user["bio"].replace("＃", "#")
    user["bio"] = user["bio"].replace("＜", "<")
    user["bio"] = user["bio"].replace("＞", ">")
    user["bio"] = user["bio"].replace("［", "[")
    user["bio"] = user["bio"].replace("］", "]")
    user["bio"] = user["bio"].replace("｛", "{")
    user["bio"] = user["bio"].replace("｝", "}")
    user["bio"] = user["bio"].replace("｜", "|")
    user["bio"] = user["bio"].replace("＼", "\\")
    user["bio"] = user["bio"].replace("＿", "_")
    user["bio"] = user["bio"].replace("｀", "`")
    

    # if location is true
    if check_location(user["location"]):
        return True
    elif not check_chinese_character(user["name"]) and not check_chinese_character(user['bio']):
        return False
    elif not check_japanese_character(user["name"]) and not check_korean_character(user["name"]) and not check_japanese_character(user['bio']) and not check_korean_character(user['bio']):
        return True
    else:
        return False

# whether it followed the most popular chinese accounts
# check tweets

# check existence of a user
def check_existence(username):
    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile_test.db")
    usernamelist = []
    for row in users:
        usernamelist.append(row[3].lower())
    if username.lower() in usernamelist:
        print(f"{username} exists!")
    else:
        print(f"{username} does not exist!")


def distribution(users):
    follower_list = []
    for row in users:
        follower_list.append(row[11])
    # x_labels: 0-500, 500-1000, 1000-2000, 2000-5000, 5000-10000, 10000-20000, 20000-50000, 50000-100000, 100000-200000, 200000-500000, 500000-inf
    y = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for follower in follower_list:
        if follower < 500:
            y[0] += 1
        elif follower < 1000:
            y[1] += 1
        elif follower < 2000:
            y[2] += 1
        elif follower < 5000:
            y[3] += 1
        elif follower < 10000:
            y[4] += 1
        elif follower < 20000:
            y[5] += 1
        elif follower < 50000:
            y[6] += 1
        elif follower < 100000:
            y[7] += 1
        elif follower < 200000:
            y[8] += 1
        elif follower < 500000:
            y[9] += 1
        else:
            y[10] += 1
    x = ["0-0.5k", "0.5k-1k", "1k-2k", "2k-5k", "5k-10k", "10k-20k", "20k-50k", "50k-100k", "100k-200k", "200k-500k", "500k-inf"]
    # plt to plot
    plt.bar(x, y)
    # plt.xticks(rotation=45)
    plt.yticks(range(0, 300000, 10000))
    plt.xlabel("followers")
    plt.ylabel("number of users")
    plt.title("followers distribution")
    # add y value upon each bar
    for a, b in zip(x, y):
        plt.text(a, b+0.05, '%.0f' % b, ha='center', va= 'bottom',fontsize=11)
    plt.show()

if __name__=="__main__":
    not_exist = [
    ]
    for user in not_exist:
        check_existence(user)

    users = fetch_all_users("idiotbots_dot_com/data/profiles/profile_test.db")

    # distribution(users)
    
    chinese_users = []
    for row in users:
        user = {
            "name": row[2],
            "username": row[3],
            "bio": row[4],
            "location": row[5],
            "tweet": row[9],
            "following": row[10],
            "followers": row[11],
        } 
        if check_chinese(user):
            chinese_users.append(row)
        
    # distribution(chinese_users)

    chinese_users.sort(key=lambda x: x[11], reverse=True)
    for i in range(200):
        print(i, chinese_users[i][2], chinese_users[i][3], chinese_users[i][11])
    print(f"chinese users:{len(chinese_users)}")

