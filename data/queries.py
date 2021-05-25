import os
import json

from data import data_manager


def get_shows():
    return data_manager.execute_select('SELECT id, title FROM shows;')


def get_most_rated_shows(offset=0, order_criteria=None, order_direction=None):
    if not order_direction and not order_criteria:
        return data_manager.execute_select('SELECT * FROM shows ORDER  BY rating DESC LIMIT 15 OFFSET %(offset)s',
                                           {'offset': offset})
    else:
        x = f'SELECT * FROM shows ORDER  BY {order_criteria} {order_direction} LIMIT 15 OFFSET {offset}'
        print(x)
        return data_manager.execute_select(
            f'SELECT * FROM shows ORDER  BY {order_criteria} {order_direction} LIMIT 15 OFFSET {offset}')


def get_show_genres(show_id):
    ceva = data_manager.execute_select('SELECT genre_id FROM show_genres WHERE show_id = %(show_id)s',
                                       {'show_id': show_id})
    return [x['genre_id'] for x in ceva]


def get_genre_name(genres):
    list_to_return = []
    for genre in genres:
        list = data_manager.execute_select('SELECT name FROM genres where id= %(genre)s', {'genre': genre})
        list_to_return.append(list[0]['name'])
    return list_to_return
