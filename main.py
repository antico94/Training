from flask import Flask, render_template
from data import queries
from dotenv import load_dotenv

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
    app.run(debug=False)


@app.route('/shows/most-rated')
def most_rated():
    shows = queries.get_most_rated_shows()

    for show in shows:
        genres_id = queries.get_show_genres(show['id'])
        genres_name = queries.get_genre_name(genres_id)
        show['genre'] = genres_name
        print(genres_name)

    return render_template('most-rated.html', shows=shows)


if __name__ == '__main__':
    main()


most_rated()