import json

# function to sort out the episodes
def sort_out(json):
    # create a list to store the episodes
    episodes = []
    titles = []
    times = []
    # loop through the json
    for i in json:
        # loop through the seasons
        for j in i['seasons']:
            # loop through the episodes
            for k in j['episodes']:
                # loop through the playDates
                for l in k['playDates']:
                    # check if the playDate is after 2022-11-07
                    if l > '2022-11-07':
                        # add the episode to the list
                        episodes.append(k['id'])

                        # append title to titles
                        titles.append(i['title'])

                        # append time to times
                        times.append(l)
    # return the list
    return episodes, titles, times

# open json file
data = open('app_data\McBaumwolle_watched_shows.json')

# load json file
json = json.load(data)

# call function
episodes = sort_out(json)

# sort by date
# episodes = sorted(episodes, key=lambda x: x[2])

# format time like this: 'yyyy-mm-dd at hh:mm:ss'
for i in range(len(episodes[2])):
    episodes[2][i] = episodes[2][i].replace('T', ' at ')
    episodes[2][i] = episodes[2][i].replace('.000Z', '')

# print each episode and title combination
for i in range(len(episodes[0])):
    # save in text file
    with open('watched_episodes.txt', 'a') as f:
        # save in colums with spacing 
        f.write(f'{episodes[0][i]:<10}{episodes[1][i]:<30}{episodes[2][i]:<30} \n')
