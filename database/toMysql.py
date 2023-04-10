import mysql.connector
import json

example_data = [
   {
            "created_at": "2021-09-16T12:34:26.000Z",
            "description": "Yes, I am lazy..",
            "id": "1438481337569067008",
            "location": "United States",
            "name": "Fananshi\ud83c\udf7b",
            "profile_image_url": "https://pbs.twimg.com/profile_images/1630090968216260608/IUu5XsZh_normal.jpg",
            "protected": False,
            "public_metrics": {
                "followers_count": 14,
                "following_count": 846,
                "listed_count": 1,
                "tweet_count": 11
            },
            "username": "fananshi",
            "verified": False
        }
]

# create a connection to your MySQL database
db = mysql.connector.connect(
  host="your_host",
  user="your_username",
  password="your_password",
  database="twitter"
)

# create a cursor object to interact with the database
cursor = db.cursor()

# define the SQL statement to insert account info into the account_info table
sql = """INSERT INTO account_info (
         id, username, name, description, location, profile_image_url, protected, verified, created_at,
         followers_count, following_count, listed_count, tweet_count
       ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""

# loop through each JSON object in your data list
for account in example_data:

  # extract the relevant information from the JSON object
  id = account["id"]
  username = account["username"]
  name = account["name"]
  description = account["description"]
  location = account["location"]
  profile_image_url = account["profile_image_url"]
  protected = account["protected"]
  verified = account["verified"]
  created_at = account["created_at"]
  followers_count = account["public_metrics"]["followers_count"]
  following_count = account["public_metrics"]["following_count"]
  listed_count = account["public_metrics"]["listed_count"]
  tweet_count = account["public_metrics"]["tweet_count"]

  # insert the account info into the account_info table
  values = (id, username, name, description, location, profile_image_url, protected, verified, created_at,
            followers_count, following_count, listed_count, tweet_count)
  cursor.execute(sql, values)

# commit the changes to the database and close the connection
db.commit()
db.close()






"""
# create the table
CREATE TABLE  (
  id BIGINT PRIMARY KEY,
  username VARCHAR(255) NOT NULL,
  name VARCHAR(255) NOT NULL,
  description TEXT,
  location VARCHAR(255),
  profile_image_url TEXT,
  protected BOOLEAN,
  verified BOOLEAN,
  created_at DATETIME NOT NULL,
  followers_count INT NOT NULL,
  following_count INT NOT NULL,
  listed_count INT NOT NULL,
  tweet_count INT NOT NULL
);


"""
