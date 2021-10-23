# tmdb-scripts

Currently this repo contains only one script, but it may eventually grow.

## 1. Getting favorites from IMDB

Function `get_favorites()` produces a CSV file of titles you have rated 10 (customizable treshold) on *IMDB*, so you can import them as favorites to *TMDB*.

Why? IMDB doesn't have "favorites" as in TMDB, so when migrating you'd have to manually choose all favorites. Since you probably give 10 to your favorites only, this script should work quite well.

## Usage:

As the project currently contains only one function, the UI is quite minimalistic. The options are found at the start of the `main.py` file and running the file runs the function.

You can download your `ratings.csv` from [IMDB](https://www.imdb.com/list/ratings/) (three dots > Export).
