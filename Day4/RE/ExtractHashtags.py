import re

def extract_hashtags(text):
    pattern = r'#[a-zA-Z0-9_]+'
    return re.findall(pattern, text)

tweet = "Learning #Python is fun! #coding #100DaysOfCode #Regex_Challenge"

# Extracting hashtags
hashtags = extract_hashtags(tweet)
print(hashtags)
