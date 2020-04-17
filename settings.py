import envparse

envparse.env.read_envfile('.env')
PASSWORD = envparse.env.str('PASSWORD', default=None)