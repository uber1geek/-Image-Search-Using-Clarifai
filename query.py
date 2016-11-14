import sqlite3
import urllib2
import sys

conn = sqlite3.connect('search.db')
c = conn.cursor()

def main(query):
	c.execute("SELECT * FROM imgTags WHERE tags LIKE '%"+query+"%'")
	print c.fetchone()
	c.close()


if __name__ == '__main__':
  main(sys.argv[1])

