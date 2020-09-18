# import psycopg2
# conn = psycopg2.connect('user=postgres host=localhost  password=2025 port=5432 dbname=Track_time.db')
# cur = conn.cursor()
#
# # mycursor.execute('DROP TABLE if exists additions')
# cur.execute("""SELECT * FROM Track_time""")
# res=cur.fetchall()
# print(res)