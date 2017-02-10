# twit
Just a basic Twitter event loop reader
# It will check the event loop for variations of the given keyword, i.e. "panda" searches for ['panda','pandas','Panda','Pandas']

# Usage: 
#  Starting a feed stream with full text
>./twit.py -k panda 
# Start a shell session stream with random keywords from the feed
>./twit.py -k panda --stream
# Get a summary from wikipedia regarding the keyword chosen and post it back as a tweet
>./twit.py -k panda --stream --wiki
