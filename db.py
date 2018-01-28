import psycopg2

class Database:
	def __init__(self):
		self.conn = psycopg2.connect("dbname=robot_info user=postgres password=JensenRobot321")
		self.cur = self.conn.cursor()


	def update_field(field, val):
		self.cur.execute("UPDATE real_time SET {0}={1} WHERE info_id=1".format(field, val))






## For testing ##
if __name__ == '__main__':
	db = Database()
	print db.conn
	print db.cur