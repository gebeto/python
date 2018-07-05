from peewee import *
import peewee


db = SqliteDatabase('courses.db')


class Course(Model):
	video_url = CharField()
	video_title = CharField()
	course_name = CharField()

	class Meta:
		database = db


def initialization():
	db.connect()
	db.create_tables([Course], safe=True)


if __name__ == "__main__":
	initialization()
	