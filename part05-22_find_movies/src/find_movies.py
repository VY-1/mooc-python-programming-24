# Write your solution here

def find_movies(database: list, search_term: str) -> list:
    new_list = []
    for movie in database:

        if search_term.casefold() in movie["name"].casefold():
            new_list.append(movie)

    return new_list

if __name__ == "__main__":
    database = [{"name": "Gone with the Python", "director": "Victor Pything", "year": 2017, "runtime": 116},
                {"name": "Pythons on a Plane", "director": "Renny Pytholin", "year": 2001, "runtime": 94},
                {"name": "Dawn of the Dead Programmers", "director": "M. Night Python", "year": 2011, "runtime": 101}]

    my_movies = find_movies(database, "python")
    print(my_movies)