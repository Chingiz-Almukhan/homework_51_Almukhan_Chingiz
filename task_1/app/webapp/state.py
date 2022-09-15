import random

from webapp.db import data, links


def change_state(post):
    if post.get('state') == 'play':
        if data.get('is_active') == 'yes':
            random_num = random.randint(1, 100)
            if random_num > 33:
                data.update({'happiness': data.get('happiness') + 15})
                data.update({'satiety': data.get('satiety') - 10})
                data.update(({'image': links[1]}))
            else:
                data.update({'happiness': 0})
                data.update(({'image': links[2]}))
        else:
            data.update({'happiness': data.get('happiness') - 5})
            data.update(({'satiety': data.get('satiety') - 10}))
            data.update(({'image': links[3]}))
            data.update({'is_active': 'yes'})
    elif post.get('state') == 'feed':
        if data.get('is_active') == 'yes':
            data.update({'satiety': data.get('satiety') + 15})
            data.update({'happiness': data.get('happiness') + 5})
            data.update(({'image': links[4]}))
            if data.get('satiety') >= 100:
                data.update({'satiety': 100})
                data.update({'happiness': data.get('happiness') - 30})
                data.update(({'image': links[5]}))
        else:
            data.update({'is_active': 'yes'})
            data.update(({'image': links[0]}))
    elif post.get('state') == 'sleep':
        data.update({'is_active': 'no'})
        data.update(({'image': links[6]}))


def check_data(some_data):
    if some_data.get('satiety') < 0:
        some_data.update({'satiety': 0})
    elif some_data.get('happiness') < 0:
        some_data.update({'happiness': 0})
