import tweepy
import config
import time
import multiprocessing
# from datetime import datetime, timedelta

myList = ['minitofu_de', 'sunhaokk', 'growthcapreport', 'KatharineSieck', 'nagatokoi', 'MitsubishiMid', 'IBCpradeeprawat', 'RavenRaymier3', 'thanatos_hp', 'artistholbein', 'SlimpenniesNFT', 'pd_xen', 'veronicamenglu', 'keonuu__', 'SPGlobalPMI', 'damoshushu', 'kyou_eth', 'ChauJastin', 'DeepthiPrimali', 'CTestFunny', '1bgmsuocySD05Qk', 'tianxingjian111', 'meedy_baby', 'MeowrPurrfect', 'sakananoike', 'ginzatobu', 'o3o_mandol', 'rezabloomer', 'LVlastuin', 'michaelldm', 'icooktw', 'ElaineFR', 'Shibaa27', 'scttdvln', 'linux_deepin', 'pedrinhodacruz_', 'Harious_Joe', 'el_lumpen', 'vetinari0714', 'Trshz0156', 'jentaub', '600689', 'majia1988', 'Ebz_Tin', 'magaly_aliantec', 'ayaforjm1013', 'Aughr', 'scottmcgeejr', 'noxvrenne', 'AgendaFreeTV', 'Yokohama_amachi', 'ifweburn1', 'Kotoba_kun', 'strutter777', 'hatami_izumo', 'TANGDOG2', 'llll040305', 'Kishu_Mate', 'SloodlesNFT', 'ROI_Analytics', 'Loku', 'CousinMatt_', 'chechelee', 'asigami9', 'Mammie_Sorbo', 'R6ghzU7nmpPTt5j', 'LukeSekuterski', 'badeduc', 'wuheqilin', 'M19nares1', 'JoyZcz', 'Ren_leilei', 'itsMedicine0', 'wapwap90', '200468QQ', 'Sonia3488', 'berry838', 'DannyQu8', 'geyao', 'chenhua59721848', 'Mrzzy888', '_Zuleikat', 'XooshAbdirahman', 'DonBraid', 'ActLittleMan', 'bong8242co', 'FayeCreative', 'tvstarr', '7wV2i0a0FOg7Xwm', 'transportdsn', 'Comrade_Hoxha', 'Miku_lzayoi0119', 'bananalove1069', 'CharlieLi_Cloud', 'willchan86755', 'laozheng2020', 'vG3oj7h0IkKuUx9', 'Ceezwer2', 'EmbajadaChinaEc', 'spaceswapdefi']

# today_time = datetime.now()
# today = str(today_time)[:10]
# yesterday = str(today_time-timedelta(days=1))[:10]

client = tweepy.Client(bearer_token=config.bear_token)
query = "covid -is:retweet"
query0 = "covid OR covid19 is:retweet"
query1 = "covid OR covid19 -is:retweet"
query2 = "xijinping -is:retweet"
query3 = "(from:bboczeng) until:2022-03-04 since:2022-01-01" # need elevated api access.
query4 = "(from:bboczeng)"

start_time = time.time()

def search_tweets(thread_id):
    for i in range(myList[i*10], myList[(i+1)*10]):
        query = f"(from:{myList[i]})"
        response = client.search_recent_tweets(query=query, 
        max_results=10)
        if response.data:
            print(i , response.data[0].text)
    

# create 10 processes, each process search 10 users
for i in range(10):
    p = multiprocessing.Process(target=client.search_recent_tweets, args=(query4, 10))
    p.start()
    p.join()


end_time = time.time()
print(f"total time cost: {end_time - start_time}")

# for _, tweetor in enumerate(myList):
#     query = f"(from:{tweetor})" 
#     response = client.search_recent_tweets(query=query, 
#     max_results=10)
#     if response.data:
#         print(_, response.data[0].text)

# for tweetor in myList:
#     print(f"tweets from {tweetor}:\n")
#     query = f"(from:{tweetor})" 
#     response = client.search_recent_tweets(query=query, 
#     max_results=100)
    
#     counter = 0

#     for tweet in response.data:
#         counter += 1
#         print(tweet.text)
#         print(f"########################--------------------------------------------{counter}")


# client = tweepy.Client(bearer_token=config.bear_token)
# query = "openai -is:retweet"

# response = client.search_recent_tweets(query=query,
#                                        max_results=10,
#                                        tweet_fields=['created_at', 'lang'],
#                                        user_fields=['profile_image_url'],
#                                        expansions=['author_id'])

# users = {u['id']: u for u in response.includes['users']}
                                        
# counter = 0
# for tweet in response.data:
#     if users[tweet.author_id]:
#         user = users[tweet.author_id]
#         counter += 1
#         print(tweet.id, tweet.created_at, tweet.lang)
#         print(user.profile_image_url)
#         print(f"----------------------------------------------------{counter}")
