import snscrape.modules.twitter as sntwitter

maxTweets = 10
keyword = 'covid19'

for i,tweet in enumerate(sntwitter.TwitterSearchScraper(keyword + ' lang:tr since:2020-01-01 until:2020-10-30 -filter:links -filter:replies').get_items()):
        if i > maxTweets :
            break  
        print(tweet.username)
        print(tweet.date)
        print(tweet.content)
        print("\n")



