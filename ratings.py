"""Restaurant rating lister."""


def print_ratings(rate_file):
    """Takes in a file, prints out restaurants and ratings.
    """

    rests = open(rate_file)
    new_dict = {}

    for pair in rests:
        ratings = pair.rstrip().split(':')
        new_dict[ratings[0]] = ratings[1]

    restaurants = sorted(new_dict)

    for place in restaurants:
        print place, 'is rated at', new_dict[place]


print_ratings('scores.txt')
