from flask import Flask, render_template, request, redirect, url_for, jsonify
from data import queries
from dotenv import load_dotenv
from util import json_response

# import data_manager

load_dotenv()
app = Flask('codecool_series')


@app.route('/')
def index():
    shows = queries.get_shows()
    return render_template('index.html', shows=shows)


@app.route('/design')
def design():
    return render_template('design.html')


def main():
    app.run(debug=True)


@app.route('/shows/most-rated/<page>', methods=['GET', 'POST'])
# @json_response
def most_rated(page=1):
    if int(page) == 0:
        page = 0
    else:
        page = int(page) - 1

    data_received = request.get_json()
    print(data_received)
    if data_received is None:
        shows = queries.get_most_rated_shows(page * 15)
        for show in shows:
            genres_id = queries.get_show_genres(show['id'])
            genres_name = queries.get_genre_name(genres_id)
            show['genre'] = genres_name
        total_shows = queries.get_shows()
        return render_template('most-rated.html', shows=shows, total_shows=total_shows, page_nr=page)
    else:
        page = int(data_received[0])
        order_criteria = data_received[1]
        order_direction = data_received[2]
        shows = queries.get_most_rated_shows(page * 15, order_criteria, order_direction)
        for show in shows:
            genres_id = queries.get_show_genres(show['id'])
            genres_name = queries.get_genre_name(genres_id)
            show['genre'] = genres_name
        total_shows = queries.get_shows()
        return jsonify(shows)


@app.route('/shows/most-rated', methods=['GET', 'POST'])
def most_rated_default():
    return redirect(url_for('most_rated', page=0))


if __name__ == '__main__':
    main()
