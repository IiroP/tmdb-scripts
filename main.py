import csv

# Options
inputFile = "ratings.csv" # Ratings will be read from this file
outputFile = "favorites.csv" # Favorites will be written to this file
minRating = 10 # Titles with this rating (or higher) are counted as favorites

def get_favorites():
	favorites = []
	with open(inputFile) as file:
		reader = csv.DictReader(file)
		for row in reader:
			# Ignore individual episodes etc.
			if row["Title Type"] != "tvSeries" and row["Title Type"] != "movie":
				continue
			if int(row["Your Rating"]) >= minRating:
				favorites.append(row)

	# Throw error if no favorites			
	if len(favorites) == 0:
		raise ValueError("No titles with rating 10")

	with open(outputFile, "w", newline="") as output:
		# Get field names from first favorite
		fields = favorites[0].keys()

		writer = csv.DictWriter(output, fieldnames=fields)
		writer.writeheader()
		writer.writerows(favorites)

# Currently the function is automatically run, there is no UI
get_favorites()