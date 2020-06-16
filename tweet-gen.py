import GetOldTweets3 as got
import sys
from random import choice


def gettweets(username):
    tweetCriteria = got.manager.TweetCriteria().setUsername(username)\
                                               .setMaxTweets(500)

    results = got.manager.TweetManager.getTweets(tweetCriteria)
    tweets = []

    for tweet in results:
        text = tweet.text.split()
        tweets.extend(text)

    return tweets

    # with open('tweetcorpus.txt', 'w') as file:
    #     for tweet in results:
    #         file.write(tweet.text)
    #         file.write('\n')

def make_chains(words, n):
    # text = open(file_path).read()

    chains = {}

    # words = text.split()

    for i in range(len(words) - (n -1)):
        upper_bound = i + n
        ngram = tuple(words[i:upper_bound])
        chains[ngram] = chains.get(ngram, [])
        if upper_bound < len(words):
            chains[ngram].append(words[upper_bound])

    return chains

def make_text(chains):
    """Return text from chains."""

    words = []

    keys = list(chains.keys())
    link = choice(keys)
    n = len(link)
    words.extend(link)

    while chains[link] and len(words) < 30:
        words.append(choice(chains[link]))

        link = tuple(words[-n:])


    return " ".join(words)

username = sys.argv[1]

source = gettweets(username)

chains = make_chains(source, 5)

random_tweet = make_text(chains)

print(random_tweet)
