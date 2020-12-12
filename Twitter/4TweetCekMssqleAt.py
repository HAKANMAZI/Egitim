import pyodbc 
import snscrape.modules.twitter as sntwitter

conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BDR59P4;'
                      'Database=egitim;'
                      #'Trusted_Connection=yes;'
                      'uid=twitteruser;'
                      'pwd=123456;')
cursor = conn.cursor()

for i,tweet in enumerate(sntwitter.TwitterSearchScraper('covid19 istanbul lang:tr since:2000-01-01 until:2020-12-12').get_items()):
    if i>20: 
        break 
    print(tweet.content)
    print(tweet.username)
    print(tweet.date)
    print(i)
    print("\n")

    command = ('insert into [egitim].[dbo].[tweet](content, username, date) values (?,?,?) ')
    values = [tweet.content, tweet.username, tweet.date]
    
    cursor.execute(command, values)
    cursor.commit()

cursor.close()



    
