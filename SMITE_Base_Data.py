import sqlite3
import hirez_connect

sql_connect = sqlite3.connect('smite.sqlite')
sql_cursor = conn.cursor()

sql_cursor.execute('''
    CREATE TABLE IF NOT EXISTS MATCHES
    (id INTEGER NOT NULL UNIQUE PRIMARY KEY, date TEXT, queue INTEGER)
    ''')

# match_player table where many players can be associated with a single match_id and team_id
# this table will be the player records from each match, including most importantly each player's tier
# match_team table where we have at present 2 teams per match, as we see in the JSON/XML supplied by the api
# in match_team, the primary key is the values of team_num (0 or 1 unless we get a 3+ team ranked game mode)
# At present the only data that belongs in the match_team table is the boolean value winner

# sql_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS MATCH_TEAMS
#     (team_num INTEGER,
#      match_id INTEGER,
#      winner INTEGER,
#      PRIMARY KEY(team_num, match_id))
#      ''')
#
# sql_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS match_player
#     id INTEGER NOT NULL PRIMARY KEY UNIQUE,
#     match_id INTEGER,
#     team_num INTEGER,
#     player_id INTEGER,
#
#     ''')
#
# sql_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS PATCHES
#     (id TEXT PRIMARY KEY, start_date TEXT, end_date TEXT)
#     ''')
#
# # items needs to be finished
# sql_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS items
#     (id INTEGER NOT NULL UNIQUE PRIMARY KEY,
#     name TEXT,)
#     ''')
#
#
# sql_cursor.execute('''
#     CREATE TABLE IF NOT EXISTS gods
#     (id INTEGER NOT NULL UNIQUE PRIMARY KEY)
#
#     ''')
