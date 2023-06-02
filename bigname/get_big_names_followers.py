import twint
import multiprocessing


def crawl(user):
    c = twint.Config()
    c.Username = user
    c.Database = "/home/janan/TwitterChina/bigname/data/big_name_followers/" + user + ".db"
    twint.run.Followers(c)

if __name__=="__main__":

    big_names = [
    ]

    processes = []
    for user in big_names:
        p = multiprocessing.Process(target=crawl, args=(user,))
        processes.append(p)
        p.start()

    for process in processes:
        process.join()