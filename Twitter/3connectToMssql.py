import pyodbc 
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=DESKTOP-BDR59P4;'
                      'Database=egitim;'
                      #'Trusted_Connection=yes;'
                      'uid=twitteruser;'
                      'pwd=123456;')

cursor = conn.cursor()
cursor.execute('SELECT * FROM [egitim].[dbo].[Tweets]')

for row in cursor:
    print(row)
