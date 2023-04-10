import get_userinfo
import get_followers



if __name__ == "__main__":
    userid_list = [
        "215939847",
    ]
    username_list = get_followers.get_followers(userid_list)
    user_list = get_userinfo.get_user_info(username_list)
    get_userinfo.write_to_database(user_list)
    print("done")