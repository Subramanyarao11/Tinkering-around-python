cur_movies = {
  'Batman': '11:00am',
  'Rudolph': '1:00pm',
  'Ted': '3:00pm',
  'Ted-2': '5:00pm'
}

print("We're Cuurently Showing the following Movies")

for key in cur_movies:
  print(key)

movie = input("What movie would you like to get the showtime for?\n")

showtime = cur_movies.get(movie)
if showtime == None:
  print("Requested showtime isn't playing")
else:
  print(movie, "is playing at", showtime)
