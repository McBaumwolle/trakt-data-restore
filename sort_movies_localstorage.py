import json
import datetime

# function to sort out the episodes
def sort_out(json):
    # loop through the json
    for movie_id in json:
        ts = json[movie_id][0]
        # after 2022-11-07 only
        if(ts > 1667775600):
            print((7-len(movie_id)) * ' ' + str(movie_id) + ' at ' + str(datetime.datetime.fromtimestamp(ts)))

# open json file
data = open('watched_movies.json')

# load json file
json = json.load(data)

# call function
episodes = sort_out(json)
