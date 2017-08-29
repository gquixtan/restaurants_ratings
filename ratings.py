"""Restaurant rating lister."""

def make_rating_dict(rate_file):
    """Takes in a file, returns a dict.
    """

    rests = open(rate_file)
    new_dict = {}

    for pair in rests:
        ratings = pair.rstrip().split(':')
        new_dict[ratings[0]] = ratings[1]

    return new_dict


new_dict = make_rating_dict('scores.txt')





def print_ratings(new_dict):
    """Takes in a file, prints out restaurants and ratings.
    """

    restaurant_list = sorted(new_dict)

    for place in restaurant_list:
        print place, 'is rated at', new_dict[place]


def new_ratings(new_dict):
    """Allows new input for restaurants/ratings to dict from print_ratings.
    """

    restaurants = new_dict

    new_rest = raw_input('What restaurant do you want to add?: ')
    new_rate = raw_input('What is your rating for {}?: '.format(new_rest))

    restaurants[new_rest] = new_rate

    new_dict = restaurants

    return new_dict



print_ratings(new_dict)
new_ratings(new_dict)
print_ratings(new_dict)
