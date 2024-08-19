insert into tab_movies (name, description)
values ("Harry Potter I", "um filme muito legal."),
		("Harry Potter II", "um filme muito legal."),
        ("Harry Potter III", "um filme muito legal."),
        ("Harry Potter IV", "um filme muito legal."),
        ("Harry Potter V", "um filme muito legal."),
        ("Harry Potter VI", "um filme muito legal."),
        ("Harry Potter VII", "um filme muito legal."),
        ("Harry Potter VIII", "um filme muito legal."),
        ("Criaturas das Profundezas", "Nao conheco."),
        ("Titanic", "oscar."),
        ("Avatar", "Bonzinho"),
        ("Avatar II", "Mais legal"),
        ("A Origem", "Muito bom"),
        ("Interestelar", "Melhor filme"),
        ("Dunkirk", "Nao assisti."),
        ("Tubarao", "..."),
        ("E.T.", "Classico");
        
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
        
insert into director_movie (director_id, movie_id)
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
        
insert into artist_movie (artist_id, movie_id)
values (1, 1),
		(1, 2),
        (1, 3),
        (1, 5),
        (2, 1),
        (2, 2),
        (2, 3),
        (4, 10),
        (4, 13);