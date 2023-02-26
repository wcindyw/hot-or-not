# HOTorNOT
AthenaHacks 2023 submission

![HOTorNOT website design](https://github.com/wcindyw/hot-or-not/blob/main/1.png?raw=true)
![HOTorNOT website design](https://github.com/wcindyw/hot-or-not/blob/main/2.png?raw=true)

## Inspiration
HOTorNOT is a prototype web app inspired by our team’s varying spice tolerances for spicy foods. Websites like AllRecipes (allrecipes.com) will return tons of recipes when users search “chili”, “salsa”, and other similar keywords, but no option to filter by spice preference and/or tolerance. Enter HOTorNOT, the app that ranks recipes for a dish–based on spiciness.

## What it does
HOTorNOT is a prototype web app that ranks recipes for a dish–based on spiciness–by generating a composite heat index based on ingredient ratio and the Scoville scale. 

As it stands HOTorNOT can rank a dish’s spiciness by sorting recipes based on the number of Scoville heat units (SHU) of the ingredients. First, the user enters the name of a dish for which they desire a recipe. Then the app obtains the search results from AllRecipes and compares each ingredient to a comprehensive repertoire of ingredients with corresponding SHU. The results are sorted by SHU in ascending order and displayed to the user.

## How we built it
Our incredibly aesthetic mockup was created using Canva.

As for the current functionality: the script is written in Python. We scrape AllRecipes using the python-allrecipes library. The query results are compared to a dataset, Ultimate List of Peppers & their SHU, to obtain an ingredient’s associated SHU.

## Challenges we ran into 
We had trouble finding a recipe website that included an abundance of recipes for favorite dishes from our cultural backgrounds. We settled for AllRecipes due to its popularity, great number of recipes, and ease of web scraping.

For the functionality, processing the query results went smoothly for the most part. We hit a snag when it came to the ingredient quantities, notably with fractional amounts. The source website represents one-half with a symbol like “½” which didn’t parse correctly. After searching online we quickly found that it is simple to convert what is known as a “vulgar fraction” to a format suitable for our script.

## Accomplishments that we're proud of
We are proud of our idea and what we’ve created so far!

## What we learned
We learned how much fun it is to brainstorm wacky or light-hearted project ideas, and the value of building incrementally.

## What's next for HOTorNOT
- Use Flask web framework and deploy to a website
- Add features such as additional filter options and fun facts like dish origin history.

## Try it out
[HOTorNOT](wcindyw.github.io/hot-or-not/) **(coming soon)**
![data output](https://github.com/wcindyw/hot-or-not/blob/main/Screen%20Shot%202023-02-26%20at%201.34.53%20PM.png?raw=true)
