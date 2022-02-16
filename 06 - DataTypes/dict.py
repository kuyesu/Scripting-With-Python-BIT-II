"""Store user's favorite movies in a dictionary."""


def favorite_movies():
    """Store user's favorite movies in a dictionary."""
    movies = {}
    while True:
        movie = input("Enter a movie: ")
        if movie == "":
            break
        rating = input("Enter your rating: ")
        movies[movie] = rating
    return movies


def print_movies(movies):
    """Print out the movies and ratings."""
    for movie, rating in movies.items():
        print(f"{movie}: {rating}")


def main():
    """Run the program."""
    movies = favorite_movies()
    print_movies(movies)


if __name__ == "__main__":
    main()


    