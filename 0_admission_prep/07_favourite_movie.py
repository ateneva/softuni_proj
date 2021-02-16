
# **************06.favourtite movie (nested loop) *****************************

movie = input()
movies = 0
most_points = 0
best_movie = ''

while not movie == 'STOP':
   movies += 1
   points = 0   # needs to start over for every movie

   for char in movie:
       p = ord(char)
       points += p

       if p >= 97 and p <= 122:
           points -= 2*len(movie)

       elif p >= 65 and p <= 90:
           points -= len(movie)

   if points >= most_points:
       most_points = points
       best_movie = movie

   if movies >= 7:
       print("The limit is reached.")
       print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")
       break

   movie = input()

else:
   print(f"The best movie for you is {best_movie} with {most_points} ASCII sum.")
