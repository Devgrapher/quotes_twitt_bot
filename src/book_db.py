# -*- coding:utf-8 -*-
import unittest
import json

class BookDB:
	def fromFile(path):
		'''make object from db file'''
		book_db = BookDB()
		f = open(path, 'r')
		db = f.read()
		book_db.parse(db)
		f.close()
		return book_db

	def formatTag(self, str):
		return str.replace(" ", "_")

	def parse(self, db):
		'''convert to string array by parsing format of json'''
		result = []
		books = json.loads(db)
		for book in books:
			try:
				name = self.formatTag(book["name"])
				author = self.formatTag(book["author"])
				for sentence in book["sentences"]:
					result += ["%s #%s #%s" % (sentence, name, author),]
			except KeyError as e:
				print("parse error %s %s %s" %(e, name, author))
				continue
		self.parsed = result


# test ##################################################

class TestDB(unittest.TestCase):
	def testParse(self):
		raw ='''
		[
		    {
		        "name": "stanford 2005",
		        "author": "steve jobs",
		        "sentences": [
		            "you can't connect the dots",
		            "looking forward"
		        ]
		    },
		    {
		        "name": "test"
		    }
		]
		'''
		bookdb = BookDB()
		bookdb.parse(raw)
		self.assertEqual(len(bookdb.parsed), 2)
		self.assertEqual(bookdb.parsed[0], '''you can't connect the dots #stanford_2005 #steve_jobs''')
		self.assertEqual(bookdb.parsed[1], '''looking forward #stanford_2005 #steve_jobs''')

	def testFromFile(self):
		bookdb = BookDB.fromFile("./test/test.json")
		self.assertEqual(len(bookdb.parsed), 2)
		self.assertEqual(bookdb.parsed[0], '''you can't connect the dots #stanford_2005 #steve_jobs''')
		self.assertEqual(bookdb.parsed[1], '''looking forward #stanford_2005 #steve_jobs''')

if __name__ == "__main__":
	unittest.main()