insert into tab_movies (name, description, release_date)
values ("Harry Potter I", "um filme muito legal.", "2001-01-01"),
		("Harry Potter II", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter III", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter IV", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter V", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter VI", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter VII", "um filme muito legal.", "2001-01-01"),
        ("Harry Potter VIII", "um filme muito legal.", "2001-01-01"),
        ("Criaturas das Profundezas", "Nao conheco.", "2001-01-01"),
        ("Titanic", "oscar.", "2001-01-01"),
        ("Avatar", "Bonzinho", "2001-01-01"),
        ("Avatar II", "Mais legal", "2001-01-01"),
        ("A Origem", "Muito bom", "2001-01-01"),
        ("Interestelar", "Melhor filme", "2001-01-01"),
        ("Dunkirk", "Nao assisti.", "2001-01-01"),
        ("Tubarao", "...", "2001-01-01"),
        ("E.T.", "Classico", "2001-01-01");
        
insert into tab_artists (name)
values ("Daniel"),
		("Emma"),
        ("Ruppert"),
        ("Leonardo di Caprio");
        
insert into tab_directors (name)
values( "James Cameron"),
		("Steven Spielberg"),
        ("Christopher Nolan"),
        ("Afonso Cuaron"),
        ("David Yates"),
        ("Mike Newell"),
        ("Chris Columbus");
        
insert into tab_users (uuid, name)
values 	("123", "Joao"),
		("124", "Maria"),
        ("125", "Carla"),
        ("126", "Joana"),
        ("127", "Tonho");
        
insert into tab_director_movie (director_id, movie_id)
values (7, 1),
		(7, 2),
        (4, 3),
        (6, 4),
        (5, 5),
        (5, 6),
        (5, 7),
        (5, 8),
        (1, 9),
        (1, 10),
        (1, 11),
        (1, 12),
        (3, 13),
        (3, 14),
        (3, 15),
        (2, 16),
        (2, 17);
        
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
        (3, 1, 2);