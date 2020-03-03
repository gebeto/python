from sqlalchemy import Column, Integer, String, create_engine, REAL, BLOB
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import os

url_root = os.popen("getconf DARWIN_USER_DIR").read().strip()
url = os.path.join(url_root, "com.apple.dock.launchpad", "db", "db")
print(" >>>", url)
# exit()
engine = create_engine(f"sqlite:///{url}")
# engine = create_engine(url)
factory = sessionmaker()
factory.configure(bind=engine)
session = factory()

print(session)

Base = declarative_base()

class Apps(Base):
	__tablename__ = 'apps'
	item_id = Column(Integer, primary_key=True)
	title = Column(String())
	bundleid = Column(String())
	storeid = Column(String())
	category_id = Column(Integer)
	moddate = Column(REAL)
	bookmark = Column(BLOB)

	def __repr__(app):
		return f"App({app.item_id}, '{app.title}', '{app.bundleid}')"

class DBInfo(Base):
	__tablename__ = 'dbinfo'
	key = Column(String())
	value = Column(String())

# class ImageCache(Base):
# 	__tablename__ = 'image_cache'
# 	item_id = Column(Integer)
# 	size_big = Column(Integer)
# 	size_mini = Column(Integer)
# 	image_data = Column(BLOB)
# 	image_data_mini = Column(BLOB)


# CREATE TABLE dbinfo (key VARCHAR, value VARCHAR);
# CREATE TABLE items (rowid INTEGER PRIMARY KEY ASC, uuid VARCHAR, flags INTEGER, type INTEGER, parent_id INTEGER NOT NULL, ordering INTEGER);
# CREATE TABLE groups (item_id INTEGER PRIMARY KEY, category_id INTEGER, title VARCHAR);
# CREATE TABLE downloading_apps (item_id INTEGER PRIMARY KEY, title VARCHAR, bundleid VARCHAR, storeid VARCHAR, category_id INTEGER, install_path VARCHAR);
# CREATE TABLE categories (rowid INTEGER PRIMARY KEY ASC, uti VARCHAR);
# CREATE TABLE app_sources (rowid INTEGER PRIMARY KEY ASC, uuid VARCHAR, flags INTEGER, bookmark BLOB, last_fsevent_id INTEGER, fsevent_uuid VARCHAR);
# CREATE TABLE image_cache (item_id INTEGER, size_big INTEGER, size_mini INTEGER, image_data BLOB, image_data_mini BLOB);


# apps = session.query(Apps).all()
# print(apps)
# print(apps[0].bookmark)

# images = session.query(ImageCache).all()
# print(images)
