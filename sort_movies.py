import json

# function to sort out the episodes
def sort_out(json):
    # create a list to store the episodes
    films = []
    titles = []
    times = []
    # loop through the json
    for i in json:
        # loop through the seasons
        for j in i['playDates']:
            # only take data after 2022-11-07
            if j > '2022-11-11':
                # add the episode to the list
                films.append(i['id'])

                # append title to titles
                titles.append(i['title'])

                # append time to times
                times.append(j)

    return films, titles, times

# open json file
data = open('app_data\McBaumwolle_watched_movies.json')

# load json file
json = json.load(data)

# call function
films = sort_out(json)

# close
data.close()

# format time like this: 'yyyy-mm-dd at hh:mm:ss'
for i in range(len(films[2])):
    films[2][i] = films[2][i].replace('T', ' at ')
    films[2][i] = films[2][i].replace('.000Z', '')

# print each episode and title combination
for i in range(len(films[0])):
    # save in text file
    with open('watched_films.txt', 'a') as f:
        # save in colums with spacing 
        f.write(f'{films[0][i]:<10}{films[1][i]:<60}{films[2][i]:<30} \n')
