import GetOldTweets3 as got
import sys

tweetCriteria = got.manager.TweetCriteria().setUsername(sys.argv[1]).setMaxTweets(2)

results = got.manager.TweetManager.getTweets(tweetCriteria)
print(results)
