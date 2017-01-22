from flask import Flask, url_for
from flask import render_template
app = Flask(__name__)
from fakeDB import FAKE_DB, extract_departments

@app.route('/title/')
@app.route('/title/<title>/')
def title(title=None):
    entry = FAKE_DB[title]

    return render_template('ItemEntries.html', entry=entry)

@app.route('/about/')
def about():
    return render_template('about.html')

@app.route('/departments/')
def departments():
    departments = extract_departments(FAKE_DB)
    return render_template('departments.html', departments=departments)

@app.route('/wishlists/')
def wishlists():
    return render_template('wishlists.html')

if __name__ == '__main__':
    app.run(debug=True)
