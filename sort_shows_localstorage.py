import json
import datetime

# function to sort out the episodes
def sort_out(json):
    # loop through the json
    for show in json:
        # loop through the episodes(and their watches)
        for ep_id in json[show]['e']:
            ts = json[show]['e'][ep_id][0]
            # after 2022-11-07 only
            if(ts > 1667775600):
                print((7-len(ep_id)) * ' ' + str(ep_id) + ' at ' + str(datetime.datetime.fromtimestamp(ts)))

# open json file
data = open('trakt_orig_dates.json')

# load json file
json = json.load(data)

# call function
episodes = sort_out(json)
