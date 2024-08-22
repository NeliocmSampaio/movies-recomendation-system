insert into tab_directors (name)
values( "James Cameron"),
		("Steven Spielberg"),
        ("Christopher Nolan"),
        ("Afonso Cuaron"),
        ("David Yates"),
        ("Mike Newell"),
        ("Chris Columbus");

insert into tab_movies (name, description, release_date, director_id, genre)
values ("Harry Potter I", "um filme muito legal.", "2001-01-01", 7, "Fantasy"),
		("Harry Potter II", "um filme muito legal.", "2001-01-01", 7, "Fantasy"),
        ("Harry Potter III", "um filme muito legal.", "2001-01-01", 4, "Fantasy"),
        ("Harry Potter IV", "um filme muito legal.", "2001-01-01", 6, "Fantasy"),
        ("Harry Potter V", "um filme muito legal.", "2001-01-01", 5, "Fantasy"),
        ("Harry Potter VI", "um filme muito legal.", "2001-01-01", 5, "Fantasy"),
        ("Harry Potter VII", "um filme muito legal.", "2001-01-01", 5, "Fantasy"),
        ("Harry Potter VIII", "um filme muito legal.", "2001-01-01", 5, "Fantasy"),
        ("Criaturas das Profundezas", "Nao conheco.", "2001-01-01", 1, "Horror"),
        ("Titanic", "oscar.", "2001-01-01", 1, "Romance"),
        ("Avatar", "Bonzinho", "2001-01-01", 1, "Sci-fi"),
        ("Avatar II", "Mais legal", "2001-01-01", 1, "Sci-fi"),
        ("A Origem", "Muito bom", "2001-01-01", 3, "Sci-fi"),
        ("Interestelar", "Melhor filme", "2001-01-01", 3, "Sci-fi"),
        ("Dunkirk", "Nao assisti.", "2001-01-01", 3, "War"),
        ("Tubarao", "...", "2001-01-01", 2, "Thriller"),
        ("E.T.", "Classico", "2001-01-01", 2, "Sci-fi");
        
insert into tab_artists (name)
values ("Daniel"),
		("Emma"),
        ("Ruppert"),
        ("Leonardo di Caprio");
        
insert into tab_users (uuid, name)
values 	("123", "Joao"),
		("124", "Maria"),
        ("125", "Carla"),
        ("126", "Joana"),
        ("127", "Tonho"),
        ("134", "Ana"),
        ("135", "Daniela"),
        ("136", "Eduardo"),
        ("137", "Barbara"),
        ("138", "Jota")
        ;
        
insert into tab_artist_movie (artist_id, movie_id)
values (1, 1),
		(1, 2),
        (1, 3),
        (1, 5),
        (2, 1),
        (2, 2),
        (2, 3),
        (4, 10),
        (4, 13);
        
insert into tab_user_movie (user_id, movie_id, rate)
values	(1, 1, 5),
		(1, 2, 2),
        (1, 3, 1),
        (1, 5, 5),
        (2, 1, 5),
        (2, 7, 5),
        (3, 7, 1),
        (3, 1, 2),
        (4, 17, 1),
        (4, 15, 2),
        (4, 10, 5),
        (5, 1, 5),
        (5, 5, 3),
        (5, 8, 4),
        (5, 9, 1),
        (5, 13, 5),
        (6, 4, 5),
        (7, 6, 3),
        (8, 5, 2),
        (9, 4, 1),
        (9, 8, 4),
        (10, 10, 3),
        (10, 14, 4)
        ;