from sqlalchemy import Column, create_engine, REAL, BLOB, VARCHAR, INTEGER
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import json
import os

url_root = os.popen("getconf DARWIN_USER_DIR").read().strip()
url = os.path.join(url_root, "com.apple.dock.launchpad", "db", "db")
print(" >>>", url)
engine = create_engine(f"sqlite:///{url}")
factory = sessionmaker()
factory.configure(bind=engine)
session = factory()

Base = declarative_base()


def as_dict(item):
	return {k: v for k, v in item.__dict__.items() if k[0].isalpha() and type(v) != bytes}


setattr(Base, "as_dict", as_dict)

# class Base(Baseb):
# 	def as_dict(item):
# 		print(item)


class App(Base):
	__tablename__ = 'apps'
	item_id = Column(INTEGER, primary_key=True)
	title = Column(VARCHAR)
	bundleid = Column(VARCHAR)
	storeid = Column(VARCHAR)
	category_id = Column(INTEGER)
	moddate = Column(REAL)
	bookmark = Column(BLOB)

	def __repr__(app):
		return f"App({app.item_id}, '{app.title}', '{app.bundleid}')"


class Item(Base):
	__tablename__ = 'items'
	rowid = Column(INTEGER, primary_key=True)
	uuid = Column(VARCHAR)
	flags = Column(INTEGER)
	type = Column(INTEGER)
	parent_id = Column(INTEGER, nullable=False)
	ordering = Column(INTEGER)

	def __repr__(item):
		return f"Item({item.rowid}, '{item.uuid}', '{item.parent_id}')"


class Group(Base):
	__tablename__ = 'groups'
	item_id = Column(INTEGER, primary_key=True)
	category_id = Column(INTEGER)
	title = Column(VARCHAR)

	def __repr__(group):
		return f"Group({group.item_id}, '{group.category_id}', '{group.title}')"


class DBInfo(Base):
	__tablename__ = 'dbinfo'
	key = Column(VARCHAR, primary_key=True)
	value = Column(VARCHAR)

	def __repr__(info):
		return f"DBInfo('{info.key}', '{info.value}')"


class ImageCache(Base):
	__tablename__ = 'image_cache'
	item_id = Column(INTEGER, primary_key=True)
	size_big = Column(INTEGER)
	size_mini = Column(INTEGER)
	image_data = Column(BLOB)
	image_data_mini = Column(BLOB)

	def __repr__(img_cache):
		return f"ImageCache({img_cache.item_id}, {img_cache.size_big}, {img_cache.size_mini}, ...)"


class DownloadingApp(Base):
	__tablename__ = 'downloading_apps'
	item_id = Column(INTEGER, primary_key=True)
	title = Column(VARCHAR)
	bundleid = Column(VARCHAR)
	storeid = Column(VARCHAR)
	category_id = Column(INTEGER)
	install_path = Column(VARCHAR)

	def __repr__(app):
		return f"DownloadingApp({app.item_id}, '{app.title}', '{app.bundleid}', '{app.storeid}', ...)"


class Category(Base):
	__tablename__ = 'categories'
	rowid = Column(INTEGER, primary_key=True)
	uti = Column(VARCHAR)

	def __repr__(category):
		return f"Category({category.rowid}, '{category.uti}')"


class AppSource(Base):
	__tablename__ = 'app_sources'
	rowid = Column(INTEGER, primary_key=True)
	uuid = Column(VARCHAR)
	flags = Column(INTEGER)
	bookmark = Column(BLOB)
	last_fsevent_id = Column(INTEGER)
	fsevent_uuid = Column(VARCHAR)

	def __repr__(source):
		return f"AppSource({source.rowid}, '{source.uuid}', ...)"

