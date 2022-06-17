# Custom Search Services

This service facilitates adding websites to Chrome's "Site Search" feature that would otherwise not be possible because the websites do not offer a query URL. This is done by reverse engineering their "internal" search API's.

Chrome has a feature called "Site Search" that allows users to search websites from the URL bar (without having to visit the website first). This allows users to enter a search query and see the query results on the website without having to go to the website home page first.

For example, you know you want to purchase something on Amazon.com, you can type "Amazon.com" in the Chrome browser followed by hitting the ```SPACE``` key (instead of ```ENTER```). This will trigger Chrome to recognize you want to do a "Site Search". You can read [more about this feature here](https://www.thewindowsclub.com/search-any-website-directly-from-the-chrome-or-edge-address-bar).

This feature works with all websites that support search query parameters.
Keeping with the Amazon example:
- I know Amazon's URL query format is: https://www.amazon.com/s?k={query_string}
- So if I wanted to search Amazon for "baseball", the URL query would look like this: [https://www.amazon.com/s?k=baseball](https://www.amazon.com/s?k=baseball)

**Not all websites provide a query URL that is as easily accessible. That is the purpose this service attempts to solve.**

## Baseball Savant
I am currently using this with [Baseball Savant](https://baseballsavant.mlb.com/). This website allows you to search for baseball players and view various stats. Normally, you would need to go to the the [Baseball Savant homepage](https://baseballsavant.mlb.com/) and search the players name on the top right search box.

### How does this work?
Each player has a URL with the following pattern:
- https://baseballsavant.mlb.com/savant-player/**{Player Name}**-**{PlayerID}**
For example, if I were to search for "Aaron Judge", I would get the following URL:
- https://baseballsavant.mlb.com/savant-player/**ronald-acuna-jr**-**660670**

To create a URL for each player, we need:

1. Player Name
- I noticed the Baseball Savant search doesn't work with accented letters. Accents are very common in players from Latin American countries. This means that if you search for "Ronald Acuña Jr.", no results will be found. However, if the accents are removed (ñ becomes n), "Ronald Acuna Jr." returns the desired result. This problem can be solved by using [unicodedata.normalize](https://docs.python.org/3/library/unicodedata.html#unicodedata.normalize) in Python to replace the accented letters with non-accented letters.

2. Player ID
By using the Chrome network inspection tool, I was able to find the backend search service that is used for the website. Searches can be done by using the following URL: https://baseballsavant.mlb.com/player/search-all?search=**Ronald%20Acuna%20Jr.**
This returns a list of players that match the search query. This list contains the ID that is used in the URL.

Putting pieces 1 and 2 allows us to create the correct URL for each player:
[https://baseballsavant.mlb.com/savant-player/ronald-acuna-jr-660670](https://baseballsavant.mlb.com/savant-player/ronald-acuna-jr-660670)

### How is this used?
Add this URL to Chromes site search settings (along with a search shortcut, I use "cssbs")
- https://custom-search-services-sokb3tjtoa-uc.a.run.app/baseball-savant/%s
"%s" represents the search term that will be used.

Example:
- https://custom-search-services-sokb3tjtoa-uc.a.run.app/baseball-savant/clayton%20kershaw

### Demo
https://user-images.githubusercontent.com/1068345/174200126-68bebbbd-8e36-42ec-ac4e-e401094b01a5.mp4

