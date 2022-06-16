# Custom Search Services

This service facilitates adding websites to Chrome's "Site Search" feature that would otherwise not be possible because the websites do not offer a query URL. This is done by reverse engineering their "internal" search API's.

Chrome has a feature called "Site Search" that allows users to search websites from the URL bar (without having to visit the website first). This allows users to enter a search query and see the query results on the website without having to go to the website home page first.

For example, you know you want to purchase something on Amazon.com, you can type "Amazon.com" in the Chrome browser followed by hitting the ```SPACE``` key (instead of ```ENTER```). This will trigger Chrome to recognize you want to do a "Site Search". You can read [more about this feature here](https://www.thewindowsclub.com/search-any-website-directly-from-the-chrome-or-edge-address-bar).

This feature works with all websites that support for search query parameters.
Keeping with the Amazon example:
- I know Amazon's URL query format is: https://www.amazon.com/s?k={query_string}
- So if I wanted to searrch Amazon for "baseball", the URL query would look like this: [https://www.amazon.com/s?k=baseball](https://www.amazon.com/s?k=baseball)

**Not all websites provide a query URL that is as easily accessible. That is the purpose this service attempts to solve.**
