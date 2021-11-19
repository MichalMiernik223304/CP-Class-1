film_titles = ["Pitbull", "Listy do M", "James Bond", "Pilsudski", "Listy do M2"]

file = open("movies.txt", "a")
for i in range(0, len(film_titles)):
    file.write(film_titles[i] + "\n")
  
file.close()