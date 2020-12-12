import snscrape.modules.twitter as sntwitter

# from:Projects_007 kullanıcısına ait tweet'leri çek
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:Projects_007  lang:tr since:2020-01-01 until:2020-12-30').get_items()):
        if i > 1 : break  
        print(tweet.username)
        print(tweet.date)
        print(tweet.content)
        print("\n")


# from:Projects_007 kullanıcısından  to:@mertcobanov kullanıcısına atilan tweetleri çek
for i,tweet in enumerate(sntwitter.TwitterSearchScraper('from:Projects_007  to:@mertcobanov lang:tr since:2020-01-01 until:2020-12-30').get_items()):
        if i > 1 : break  
        print(tweet.username)
        print(tweet.date)
        print(tweet.content)
        print("\n")

# geocode:37.7764685,-122.4172004,10km 
for i,tweet in enumerate(sntwitter.TwitterSearchScraper(' geocode:37.7764685,-122.4172004,10km since:2020-01-01 until:2020-12-30').get_items()):
        if i > 20 : break  
        print(tweet.username)
        print(tweet.date)
        print(tweet.content)
        print("\n")
