# trakt-data-restore
Simple python scripts to format any trakt data from the app-cache or browser-localstorage after the 07.11.2022 downtime of `trakt.tv`.  

## how to use
0. (setup Python)
1. Save the files locally. 
2. Replace the sample path with your path to the files (e.g. `user_watched_shows.json` and `user_watched_movies.json` for shows and movies respectively).
3. Run scripts.
4. View your data!

Keep in mind that the first column is the trakt_id. Copy the id into the trakt search and select "Trakt ID".

![image](https://user-images.githubusercontent.com/67203883/208303777-56f1d0d5-09c4-45fe-9068-5dd341d96586.png)


## how to get the app cache
![image](https://user-images.githubusercontent.com/67203883/208303634-363c8a3b-58c9-4e99-b88f-73992a8600b1.png)

## how to get the browser localstorage
1. Navigate to https://trakt.tv/
2. Right click > **Inspect**
3. Click on the **Console** tab
4. Enter this in the console: `compressedCache.get('watched_shows')` and `compressedCache.get('watched_movies')`
5. Right click on the output > **Copy object**
6. Create files for the data and paste the data into them, then follow the instructions under ***how to use*** above
