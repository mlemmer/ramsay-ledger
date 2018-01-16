# >>> def static_save_page(page_name):
# ...   page_url = "http://127.0.0.1:5000/" + page_name
# ...   # This is where we'd do the request.get type thing
# ...   # and get back a response, saving it to disk.
# ...   print("Getting page: " + page_url)
# ...   output_location = "/home/mlemmer/save_this_stuff/"
# ...   page_directory = output_location + page_name
# ...   # Here we're making the directories, if they don't yet exist.
# ...   print("Making directories if necessary: " + page_directory)
# ...   page_file = page_directory + "index.html"
# ...   # Here we take the response.text (or whatever) and save
# ...   # it to a file in the subdirectory we've just ensured exists.
# ...   print("Writing response to disk: " + page_file)
# ...   # Now close the file, and you're done!

import requests
import os
import csv
import subprocess

OUTPUT_LOCATION = "/home/mlemmer/Desktop/Documents/Database/flaskproject/export/"
STATIC_LOCATION = "/home/mlemmer/Desktop/Documents/Database/flaskproject/static"
STATIC_OUTPUT_LOCATION = "/home/mlemmer/Desktop/Documents/Database/flaskproject/export/"

def static_save_page(page_name):
    page_url = "http://127.0.0.1:5000/" + page_name
    r = requests.get(page_url)
    page_directory = OUTPUT_LOCATION + page_name
    page_filename = page_directory + "index.html"
    if not os.path.exists(page_directory):
        os.makedirs(page_directory)
    with open(page_filename, mode="w", encoding="utf-8") as page_file:
        page_file.write(r.text)

FIXED_PAGES = ["", "about/", "wishlists/", "departments/"]

for page in FIXED_PAGES:
    static_save_page(page)

with open("LedgerDB.csv") as object_map_file:
    reader = csv.DictReader(object_map_file)
    for row in reader:
        page_name = "title/" + row["self"] + "/"

        static_save_page(page_name)

subprocess.Popen([
    "rsync", "--archive", "--verbose", "--recursive",
    STATIC_LOCATION, STATIC_OUTPUT_LOCATION])

print("\nDone!")

