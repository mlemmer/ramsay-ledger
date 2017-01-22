import csv

def database(csv_rows, object_map):
    """
    takes rows from csv_rows and imports the object database for the    
    Ramsay website
    """


class LedgerItem(object):
    def __init__(self, title, description, image, materials, dimensions, distance, collection, link, page, department, pounds, pounds2= None, dollars, license=None, artifact=None, date=None, origin=None, analytics=None, customer=None, ledger=None, author=None, book=None, publisher=None, Thumb1=None, Thumb2=None, Thumb3=None, Thumb4=None, Thumb5=None, Thumb6=None, Thumb7=None):
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
        self.pounds = pounds
        self.pounds2 = pounds2
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
        self.Thumb1 = Thumb1
        self.Thumb2 = Thumb2
        self.Thumb3 = Thumb3
        self.Thumb4 = Thumb4
        self.Thumb5 = Thumb5
        self.Thumb6 = Thumb6
        self.Thumb7 = Thumb7

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
                                "pounds2": row["pounds2"],
                                "dollars": row["dollars"],
                                "license": row["license"],
                                "artifact": row["artifact"],
                                "date": row["date"],
                                "origin": row["origin"],
                                "analytics": row["analytics"],
                                "customer": row["customer"],
                                "ledger": row["ledger"],
                                "author": row["author"],
                                "book": row["book"],
                                "publisher": row["publisher"],
                                "Thumb1": row["Thumb1"],
                                "Thumb2": row["Thumb2"],
                                "Thumb3": row["Thumb3"],
                                "Thumb4": row["Thumb4"],
                                "Thumb5": row["Thumb5"],
                                "Thumb6": row["Thumb6"],
                                "Thumb7": row["Thumb7"],}
