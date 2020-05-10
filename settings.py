import envparse

envparse.env.read_envfile('.env')
dsn = envparse.env.str('dsn', default=None)


