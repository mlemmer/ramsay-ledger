import csv

def database(csv_rows, object_map):
    """
    takes rows from csv_rows and imports the object database for the    
    Ramsay website
    """


class LedgerItem(object):
    def __init__(self, title, description, image, materials, dimensions, distance, collection, link, page, department, pounds, dollars, license=None, artifact=None, date=None, origin=None, analytics=None, customer=None, ledger=None, Unit=None, author=None, book=None, publisher=None, author2=None, book2=None, publisher2=None, origin2=None, link2=None):
        self.title = title
        self.description = description
        self.image = image
        self.materials = materials
        self.dimensions = dimensions
        self.distance = distance
        self.collection = collection
        self.link = link
        self.page = page
        self.department = department
        self.unit = unit
        self.pounds = pounds
        self.dollars = dollars
        self.license = license
        self.artifact = artifact
        self.date = date
        self.origin = origin
        self.analytics = analytics
        self.customer = customer
        self.ledger = ledger
        self.author = author
        self.book = book
        self.publisher = publisher
        self.author2 = author2
        self.book2 = book2
        self.publisher2 = publisher2
        self.origin2 = origin2
        self.link2 = link2

with open("LedgerDB.csv") as object_map_file:
    reader = csv.DictReader(object_map_file)
    object_map = {}
    for row in reader:
        object = row["self"]
        object_map[object] =    {"title": row["title"],
                                "description": row["description"],
                                "image": row["image"],
                                "materials": row["materials"],
                                "dimensions": row["dimensions"],
                                "distance": row["distance"],
                                "collection": row["collection"],
                                "link": row["link"],
                                "page": row["page"],
                                "department": row["department"],
                                "pounds": row["pounds"],
                                "dollars": row["dollars"],
                                "license": row["license"],
                                "artifact": row["artifact"],
                                "date": row["date"],
                                "origin": row["origin"],
                                "analytics": row["analytics"],
                                "customer": row["customer"],
                                "ledger": row["ledger"],
                                "unit": row["unit"],
                                "author": row["author"],
                                "book": row["book"],
                                "publisher": row["publisher"],
                                "author2": row["author2"],
                                "book2": row["book2"],
                                "publisher2": row["publisher2"],
                                "origin2": row["origin2"],
                                "link2": row["link2"],
                                "self": row["self"],
                                "thumbnail": row["thumbnail"],
                                "Thumb1": row["Thumb1"],
                                "Thumb2": row["Thumb2"],
                                "Thumb3": row["Thumb3"],
                                "Thumb4": row["Thumb4"],
                                "Thumb5": row["Thumb5"],
                                "Thumb6": row["Thumb6"],
                                "Thumb7": row["Thumb7"]}

def departmentize_db(db):
    departments = {}
    for row in db:
        dept = row["department"]
        if not dept in departments:
            departments[dept] = []
        departments[dept].append(row)
    return departments
