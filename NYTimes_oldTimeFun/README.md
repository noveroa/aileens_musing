![ScreenShot](/screenshots/home.png)

# NyTimes_searchAPI
- To run use npm .. or just run using npx
- - ```npx http-server -p 8000```

## Per Request 
- A search query text box 
- A button labeled “Search” that executes the search when clicked 
- A results display that includes the following for each result: 
- - Publication date 
- - Document type 
- - Headline (as a live link to the article) 
- - The web page must be accessed with the http: protocol (not file:) 


## Further Features:
-  Columns can be reordered; several columns are hidden
- - Display thumbnail image associated with each article (Too nested to understand best way to implement'
- - Paging of large result sets was not implemented; the api returns 10 at a time.  Currently the moer button will tell user how many hits have been found; user can change the offset for field to execute another search.
- - User specified date range
- - Snippet displayed in popup when mouse hovers over headline
 
