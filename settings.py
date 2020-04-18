import envparse

envparse.env.read_envfile('.env')
PASSWORD = envparse.env.str('PASSWORD', default=None)

config = {'user': 'postgres',
          'password': PASSWORD,
          'host': 'localhost',
          'database': 'my_database'}

dsn = 'postgres://{}:{}@{}/{}'.format(config['user'], config['password'],
                                      config['host'], config['database'])
