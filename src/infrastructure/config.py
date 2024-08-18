# mysql+<drivername>://<username>:<password>@<server>:<port>/dbname

class Config:
    def __init__(self, db):
        self.db = db


class DBConfig:
    def __init__(self, username, password, server, port, name) -> None:
        self.username = username
        self.password = password
        self.server = server
        self.port = port
        self.name = name


db_config = DBConfig(
    "admin",
    "admin",
    "127.0.0.1",
    3306,
    "movie_recomendation_system"
)
cfg = Config(db=db_config)
