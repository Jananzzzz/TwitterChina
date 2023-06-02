### Roadmap

1. find the tweeters with the most followers, attach labels on them
2. crawl the followings of these tweeters and their information
	1. with high priority because their following almost certainly valuable tweeter.
	2. construct the celebrity-following-following network, which is the core circle of twitter-of-china
	3. crawl the user info of the core network: followers count, following count, type
		- decide whether chinese account (most of the core network will be chinese)
			1. on name
			2. on bio
			3. on location
			4. on tweets (high cost)
		- decide account type: porn, tech, taiwannese, hongkonger, politic, entertainment, life sharing, etc.
3. use twitter api or crawler, fetch the core users' tweets, analyze them get to get the latest hotspot in ToC.