from tsorm.conf.config import DB_CONFIG
import sys


def rewrite_db_config(params: list):
    tmp = DB_CONFIG
    tmp['user'] = params[1]
    tmp['password'] = params[2]
    tmp['database'] = params[3]
    tmp['host'] = params[4] if len(params) == 5 else '127.0.0.1'
    try:
        with open('config.py', 'w') as f:
            f.write(f"""DB_CONFIG = {str(tmp)}""")
        print('You got me!')
    except Exception as e:
        print(e)
        print('\nYou suck!\n')


def add_db_config(user, password, database, host='127.0.0.1'):
    tmp = DB_CONFIG
    tmp['user'] = user
    tmp['password'] = password
    tmp['database'] = database
    tmp['host'] = host
    try:
        with open('config.py', 'w') as f:
            f.write(f"""DB_CONFIG = {str(tmp)}""")
        print('You got me!')
    except Exception as e:
        print(e)
        print('\nYou suck!\n')


if __name__ == '__main__':
    if len(sys.argv) == 4 or len(sys.argv) == 5:
        rewrite_db_config(sys.argv)
    else:
        print(f"""If local database, use: {sys.argv[0]} [user] [password] [database]""")
        print(f"""If database server, use: {sys.argv[0]} [user] [password] [database] [server]""")