from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)
from DB import object_map, departmentize_db

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/title/')
@app.route('/title/<title>/')
def title(title=None):
    entry = object_map[title]

    return render_template('ItemEntries.html', entry=entry)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/departments/')
def departments():
    dept_db = departmentize_db(object_map.values())
    return render_template('departments.html', departments=dept_db)

@app.route('/wishlists/')
def wishlists():
    return render_template('wishlists.html')


if __name__ == '__main__':
    app.run(debug=True)
