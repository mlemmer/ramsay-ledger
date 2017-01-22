What can a 250 year old merchant’s ledger tell us about consumer
purchases? This site hopes to make a dusty ledger more familiar and
fun by presenting the book's historical evidence as it might be
encountered in a modern on-line store. The user can read about what
they are shopping for, see what similar items might look like, examine
a range of options, and see a modern cost comparison. They can also
see some of the range of other items purchased by a customer. Future
features will include more information on customers and more complex
diagnostic analysis of purchases.

A live version of this site is available at:
[https://ramsay.arthistory.wisc.edu](https://ramsay.arthistory.wisc.edu)


About this repository
=====================

This is the code used to generate the Ramsay interactive
"e-commerce"-like ledger website.  It evolved initially from a dynamic
site to a static site, so this project includes a Python web
application written in Flask, along with a static exporter which
generates the static site from a running version of the dynamic site.

The "database" generating the site contents is a simple CSV file
included in this repository, `LedgerDB.csv`.


License
=======

This project is licensed under the GNU General Public License, version
3 or (at your option) any later version of the GNU GPL as published by
the Free Software Foundation.

The images in static/ are under their own respective licenses.
See the LedgerDB.csv file which documents which license is used
for each file.
