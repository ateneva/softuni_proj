
# Admission exam 2019-04-07 Movie Ratings **************************************

movies = int(input())
max_rating = 1
min_rating = 10
total_rating = 0
highest = ''
lowest = ''

for movie in range(movies):
    movie_title = input()
    rating = float(input())
    total_rating += rating

    if rating > max_rating:
        max_rating = rating
        highest = movie_title

    if rating < min_rating:
        min_rating = rating
        lowest = movie_title

    avg_rating = total_rating / movies

print(f"{highest} is with highest rating: {max_rating:.1f}")
print(f"{lowest} is with lowest rating: {min_rating:.1f}")
print(f"Average rating: {avg_rating:.1f}")
