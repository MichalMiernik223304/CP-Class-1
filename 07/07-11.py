film_titles = ["Pitbull\n", "Listy do M\n", "James Bond\n", "Pilsudski\n", "Listy do M2\n"]

file = open("movies.txt", "a")
for i in range(0, len(film_titles)):
    file.write(film_titles[i])
  
file.close()