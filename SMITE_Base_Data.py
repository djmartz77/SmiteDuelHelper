import sqlite3
import hirez_connect

sql_connect = sqlite3.connect('smite.sqlite')
sql_cursor = conn.cursor()

sql_cursor.execute('''
    CREATE TABLE IF NOT EXISTS MATCHES
    (
     id INTEGER NOT NULL UNIQUE PRIMARY KEY, 
     datetime TEXT, 
     queue INTEGER, 
     p1_duel_tier INTEGER,
     p1_win_status TEXT,
     p1_god_id INTEGER,
     p1_active_id_1,
     p1_active_id_2,
     p1_item_id_1,
     p1_item_id_2,
     p1_item_id_3,
     p1_item_id_4,
     p1_item_id_5,
     p1_item_id_6,
     p2_duel_tier INTEGER,
     p2_win_status TEXT,
     p2_god_id INTEGER,
     p2_active_id_1,
     p2_active_id_2,
     p2_item_id_1,
     p2_item_id_2,
     p2_item_id_3,
     p2_item_id_4,
     p2_item_id_5,
     p2_item_id_6,
    )
    ''')

sql_cursor.execute('''
     CREATE TABLE IF NOT EXISTS items
     (
      id INTEGER NOT NULL UNIQUE PRIMARY KEY,
      name TEXT,
      icon_url TEXT,
     )
     ''')


sql_cursor.execute('''
    CREATE TABLE IF NOT EXISTS gods
    (
     id INTEGER NOT NULL UNIQUE PRIMARY KEY,
     name TEXT,
     icon_url TEXT,
    )
     ''')
