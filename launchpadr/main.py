import json
from database import session, App, Item, Group, DBInfo, ImageCache, DownloadingApp, Category, AppSource


def dump(name, model):
	items = session.query(model).all()
	json.dump([i.as_dict() for i in items], open(f"dump/{name}.json", "w"), indent=4)


if __name__ == '__main__':
	dump("apps", App)
	dump("items", Item)
	dump("groups", Group)
	dump("dbinfo", DBInfo)
	dump("image_cache", ImageCache)
	dump("downloading_apps", DownloadingApp)
	dump("categories", Category)
	dump("app_sources", AppSource)
