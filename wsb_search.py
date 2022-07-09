from psaw import PushshiftAPI
import datetime as datetime
    
api = PushshiftAPI()



start_time=int(datetime.datetime(2021, 5, 16).timestamp())

submissions = api.search_submissions(after=start_time,
                            subreddit='investing',
                            filter=['url','author', 'title', 'subreddit'])
                           

for submission in submissions:
    
    

    words = submission.title.split()
    cashtags = list(set(filter(lambda word: word.lower().startswith('$'), words)))

    if len(cashtags) > 0:
        print(cashtags)
        #print(submission.created_utc)
        print(submission.title)
        print(submission.url)

