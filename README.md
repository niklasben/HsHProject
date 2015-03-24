# HsHProject
Files for a Student Project at the University of Applied Sciences and Arts Hannover

## Lemmatizer

In this folder are all Perl files for the German Lemmatizer

## Scripts

The perl scripts are divided by country and will retrieve the tweets using their keywords for the last week or so. The Twitter API is restricting calls made by a user in 15 minute windows. Due to this restriction, a waiting period is inserted after 175 calls.
Each script is expecting an (int) input, which represents the calls made by the script running prior to it after the last waiting period. This is needed so as to not waste possible calls.

## Output files

The Output files are formatted as such:

  'Running # of tweet' \t 'tweet_id' \t 'timestamp' \t 'message' \n
  
File names are formatted as

  "TweetFile_$country_".$date.".txt"
