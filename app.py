# TODO:
'''
    - Remove/edit entries
    - back to index page
'''

from flask import Flask, session, render_template, request, g
from db_handler import DatabaseHandler
import json

app = Flask(__name__)
dbh = DatabaseHandler()

@app.route("/", methods=['get', 'post'])
def index():
    '''Main page'''
    submited_text = request.form.get('journal_text')
    if submited_text:
        dbh.add_journal(submited_text)

    return render_template("index.html")

@app.route("/edit_text", methods=['get', 'post'])
def edit_text():
    '''Main page but from having edited text'''
    submited_text = request.form.get('journal_text')
    date = request.form.get('date')
    dbh.add_journal(submited_text, purge_old=True, date=date)

    return render_template("index.html")


@app.route("/show_journals")
def show_journals():
    all_journals = dbh.get_all_journals()
    all_journals = {k: v.replace('\r\n', '\\r\\n') for k, v in all_journals.items()}
    return render_template("show_journals.html", data=all_journals)

@app.teardown_appcontext
def print_exeption(exception):
    pass

if __name__ == '__main__':
    # app.run(debug=True)
    app.run(host="0.0.0.0", port=1902, debug=True)
