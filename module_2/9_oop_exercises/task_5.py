class Movie:
    def __init__(self, title, director, genre, release_year, duration, rating):
        self.title = title
        self._director = director
        self._genre = genre
        self._release_year = release_year
        self.__duration = duration
        self.__rating = rating

    def display_information(self):
        return f"Title: {self.title}\nDirector: {self._director}\nGenre: {self._genre}" \
               f"\nRelease year: {self._release_year}\nDuration: {self.__duration}\nRating: {self.__rating}\n"

    def upd_info(self, title, director, genre, release_year, duration, rating):
        self.title = title
        self._director = director
        self._genre = genre
        self._release_year = release_year
        self.__duration = duration
        self.__rating = rating
        return f"Title: {self.title}\nDirector: {self._director}\nGenre: {self._genre}" \
               f"\nRelease year: {self._release_year}\nDuration: {self.__duration}\nRating: {self.__rating}\n"

    def get_rate(self):
        return self.__rating


movie_1 = Movie("Great Gatsby", "Lurmann", "Drama", 2013, "2:32", 8)
movie_2 = Movie("Barbie", "Del Toro", "Comedy", 2023, "1:48", 7)


def calculate_average_rate(ratings_list: list):
    ratings = []
    for movie in ratings_list:
        ratings.append(movie.get_rate())
    return f"An average rate of movies is: {sum(ratings) / len(ratings)}\n"


print(movie_1.display_information())
print(movie_2.display_information())

print(movie_2.upd_info("Avatar", "James Cameron", "Science Fiction, Adventure, Action", 2009, "2:42", 7.8))
print(movie_2.display_information())

print(calculate_average_rate([movie_1, movie_2]))
