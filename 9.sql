SELECT people.name FROM people JOIN stars ON person_id= people.id JOIN movies ON movies.id = stars.movie_id WHERE movies.year=2004
GROUP BY people.name,person_id ORDER BY people.birth