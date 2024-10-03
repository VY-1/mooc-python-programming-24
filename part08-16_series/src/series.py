# Write your solution here:
class Series:
    def __init__(self, title: str, season: int, genres: list):
        self.title = title
        self.season = season
        self.genres = genres
        self.ratings = []

    def rate(self, rating: int):
        self.ratings.append(rating)

    def get_rating(self):
        if len(self.ratings) > 0:
            overall_rating = float(sum(self.ratings)/len(self.ratings))
            return overall_rating
        
    def __str__(self):
        genres_string = ", ".join(self.genres)
        rating_string = ""
        string_to_print = f"{self.title} ({self.season} seasons)\ngenres: {genres_string}\n"
        if self.get_rating():
            rating_string += f"{len(self.ratings)} ratings, average {self.get_rating():.1f} points"
        else:
            rating_string += "no ratings"
        string_to_print +=rating_string

        return string_to_print


def minimum_grade(rating: float, series_list: list)->list:
    series_found = []
    for series in series_list:
        if series.get_rating() >= rating:   #add to series_found if criteria met
            series_found.append(series)
    return series_found

def includes_genre(genre: str, series_list: list):
    series_found = []
    for series in series_list:
        if genre in series.genres:      #if criteria met, add to series_found
            series_found.append(series)
    return series_found


if __name__ == "__main__":
    dexter = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    dexter.rate(4)
    dexter.rate(5)
    dexter.rate(5)
    dexter.rate(3)
    dexter.rate(0)
    print(dexter)

    s1 = Series("Dexter", 8, ["Crime", "Drama", "Mystery", "Thriller"])
    s1.rate(5)
    s2 = Series("South Park", 24, ["Animation", "Comedy"])
    s2.rate(3)
    s3 = Series("Friends", 10, ["Romance", "Comedy"])
    s3.rate(2)
    series = [s1, s2, s3]
    list = minimum_grade(4.5, series)