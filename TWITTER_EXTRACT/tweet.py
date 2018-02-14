
import tweepy 
import csv

#twitter api credentials
consumer_key = "xxxxxxxxxxxxxxxxxxxxxxxx"
consumer_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_key = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
access_secret = "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"


def get_all_tweets(screen_name):
	auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
	auth.set_access_token(access_key, access_secret)
	api = tweepy.API(auth)
	alltweets = []  
	new_tweets = api.user_timeline(screen_name = screen_name,count=13)
	
	#[print(tweets) for tweets in new_tweets]
	
	alltweets.extend(new_tweets)
	oldest = alltweets[-1].id - 1
	
	while len(new_tweets) > 0:
		print( "getting tweets before %s" % (oldest))
		new_tweets = api.user_timeline(screen_name = screen_name,count=2,max_id=2)
		alltweets.extend(new_tweets)
		print ("...%s tweets downloaded so far" % (len(alltweets)))
		
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in alltweets]

	 
	with open('%s_tweets.csv' % screen_name, 'w') as f:
		writer = csv.writer(f)
		writer.writerow(("id_str","created_at","text"))
		writer.writerows(outtweets)

	pass


if __name__ == '__main__':
	get_all_tweets("verge")
