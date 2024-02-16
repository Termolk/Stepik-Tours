import random

from flask import Flask, render_template, abort  # сперва подключим модуль

import data

app = Flask(__name__)  # объявим экземпляр фласка


@app.route('/')
def render_main():
    keys = list(data.tours.keys())
    random_keys = random.sample(keys, 6)
    random_tours = {key: data.tours[key] for key in random_keys}
    return render_template('index.html', data=data, tours=random_tours)


@app.route('/departures/<departure>')
def render_departures(departure):
    if departure not in data.departures:
        abort(404)
    filtered_tours = {k: v for k, v in data.tours.items() if v['departure'] == departure}
    return render_template('departure.html', tours=filtered_tours, departure=data.departures[departure], data=data.tours)


@app.route('/tours/<int:id>')
def render_about(id):
    if id not in data.tours:
        abort(404)
    return render_template('tour.html', tour=data.tours[id], departures=data.departures, data=data)


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', data=data), 404


if __name__ == '__main__':
    app.run()