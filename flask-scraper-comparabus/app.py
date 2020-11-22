from flask import Flask
from flask import render_template
from flask import request
from flask import send_from_directory
from scraper import *


app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def root():
    if request.method == 'GET':
        return render_template('home.html')
        
@app.route('/comparateur', methods=['POST'])
def comparateur():
    from_d = request.form['from']
    to_d = request.form['to']
    date_d = request.form['date']
    scraper = ProxyScraper(from_d,to_d)
    scraper.run()
    return render_template('comparateur.html', context=scraper.results)


@app.route('/download')
def download():
    return send_from_directory('', 'liste.csv', as_attachment=True)


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
