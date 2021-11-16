"""Typing test implementation"""

from utils import *
from ucb import main, interact, trace
from datetime import datetime


###########
# Phase 1 #
###########


def choose(paragraphs, select, k):
    """Return the Kth paragraph from PARAGRAPHS for which SELECT called on the
    paragraph returns true. If there are fewer than K such paragraphs, return
    the empty string.
    """
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    i = 0  # counting how many paragraphs have be selected.
    for paragraph in paragraphs:
        if select(paragraph):
            i += 1
        if i - 1 == k:
            return paragraph
    return ''
    # END PROBLEM 1


def about(topic):
    """Return a select function that returns whether a paragraph contains one
    of the words in TOPIC.

    >>> about_dogs = about(['dog', 'dogs', 'pup', 'puppy'])
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup!'], about_dogs, 0)
    'Cute Dog!'
    >>> choose(['Cute Dog!', 'That is a cat.', 'Nice pup.'], about_dogs, 1)
    'Nice pup.'
    """
    assert all([lower(x) == x for x in topic]), 'topics should be lowercase.'
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    def is_include_topic(paragraph):
        standard_paragraph = remove_punctuation(lower(paragraph))
        words = standard_paragraph.split()
        for topic_word in topic:
            if topic_word in words:
                return True
        return False
    return is_include_topic
    # END PROBLEM 2


def accuracy(typed, reference):
    """Return the accuracy (percentage of words typed correctly) of TYPED
    when compared to the prefix of REFERENCE that was typed.

    >>> accuracy('Cute Dog!', 'Cute Dog.')
    50.0
    >>> accuracy('A Cute Dog!', 'Cute Dog.')
    0.0
    >>> accuracy('cute Dog.', 'Cute Dog.')
    50.0
    >>> accuracy('Cute Dog. I say!', 'Cute Dog.')
    50.0
    >>> accuracy('Cute', 'Cute Dog.')
    100.0
    >>> accuracy('', 'Cute Dog.')
    0.0
    """
    typed_words = split(typed)
    reference_words = split(reference)
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if len(typed_words) == 0:
        return 0.0
    else:
        i = 0  # iteration counter
        j = 0  # count the number of words that match
        while i < min(len(typed_words), len(reference_words)):
            if typed_words[i] == reference_words[i]:
                j += 1
            i += 1
        return j / len(typed_words) * 100.0


    # END PROBLEM 3


def wpm(typed, elapsed):
    """Return the words-per-minute (WPM) of the TYPED string."""
    assert elapsed > 0, 'Elapsed time must be positive'
    # BEGIN PROBLEM 4
    "*** YOUR CODE HERE ***"
    return len(typed) / 5 / elapsed * 60.0
    # END PROBLEM 4


def autocorrect(user_word, valid_words, diff_function, limit):
    """Returns the element of VALID_WORDS that has the smallest difference
    from USER_WORD. Instead returns USER_WORD if that difference is greater
    than LIMIT.
    """
    # BEGIN PROBLEM 5
    "*** YOUR CODE HERE ***"
    if user_word in valid_words:
        return user_word
    else:
        min_difference = min([diff_function(user_word, valid_word, limit) for valid_word in valid_words])
        if min_difference > limit:
            return user_word
        else:
            for valid_word in valid_words:
                if diff_function(user_word, valid_word, limit) == min_difference:
                    return valid_word

    # END PROBLEM 5


def shifty_shifts(start, goal, limit):
    """A diff function for autocorrect that determines how many letters
    in START need to be substituted to create GOAL, then adds the difference in
    their lengths.
    """
    # BEGIN PROBLEM 6
    """
    #  Did not mention the requirement of using recursion
    length_diff = abs(len(start) - len(goal))
    diff = length_diff
    for i in range(min(len(start), len(goal))):
        if diff > limit:
            return diff
        elif start[i] != goal:
            diff += 1
    return diff
    """
    if limit == -1:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))
    elif start[0] == goal[0]:
        return shifty_shifts(start[1:], goal[1:], limit)
    else:
        return shifty_shifts(start[1:], goal[1:], limit - 1) + 1
    # END PROBLEM 6


def meowstake_matches(start, goal, limit):
    """A diff function that computes the edit distance from START to GOAL.
    >>> big_limit = 10
    >>> meowstake_matches("speling", "spelling", big_limit)
    1
    """
    if limit == -1:
        return 0
    elif len(start) == 0 or len(goal) == 0:
        return max(len(start), len(goal))
    else:
        if start[0] == goal[0]:
            return meowstake_matches(start[1:], goal[1:], limit)
        else:
            add_diff = meowstake_matches(start, goal[1:], limit - 1)
            remove_diff = meowstake_matches(start[1:], goal, limit - 1)
            substitute_diff = meowstake_matches(start[1:], goal[1:], limit - 1)
            return min(add_diff, remove_diff, substitute_diff) + 1
    """
    # the template
    if __________: # Fill in the condition
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    elif ___________: # Feel free to remove or add additional cases
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END

    else:
        add_diff = ...  # Fill in these lines
        remove_diff = ... 
        substitute_diff = ... 
        # BEGIN
        "*** YOUR CODE HERE ***"
        # END
    """


def final_diff(start, goal, limit):
    """A diff function. If you implement this function, it will be used."""
    assert False, 'Remove this line to use your final_diff function'


###########
# Phase 3 #
###########


def report_progress(typed, prompt, id, send):
    """Send a report of your id and progress so far to the multiplayer server."""
    # BEGIN PROBLEM 8
    "*** YOUR CODE HERE ***"
    correct_number = 0
    for typed_word, prompt_word in zip(typed, prompt):
        if typed_word == prompt_word:
            correct_number += 1
        else:
            break
    ratio = correct_number / len(prompt)
    send({'id': id, 'progress': ratio})
    return ratio
    # END PROBLEM 8


def fastest_words_report(times_per_player, words):
    """Return a text description of the fastest words typed by each player."""
    game = time_per_word(times_per_player, words)
    fastest = fastest_words(game)
    report = ''
    for i in range(len(fastest)):
        words = ','.join(fastest[i])
        report += 'Player {} typed these fastest: {}\n'.format(i + 1, words)
    return report


def time_per_word(times_per_player, words):
    """Given timing data, return a game data abstraction, which contains a list
    of words and the amount of time each player took to type each word.

    Arguments:
        times_per_player: A list of lists of timestamps including the time
                          the player started typing, followed by the time
                          the player finished typing each word.
        words: a list of words, in the order they are typed.
    """
    # BEGIN PROBLEM 9
    "*** YOUR CODE HERE ***"
    game = [words, []]
    for i in range(len(times_per_player)):
        game[1].append([])
        for j in range(len(words)):
            interval = times_per_player[i][j + 1] - times_per_player[i][j]
            game[1][i].append(interval)
    return game
    # END PROBLEM 9


def fastest_words(game):
    """Return a list of lists of which words each player typed fastest.

    Arguments:
        game: a game data abstraction as returned by time_per_word.
    Returns:
        a list of lists containing which words each player typed fastest
    >>> p0 = [2, 2, 3]
    >>> p1 = [6, 1, 2]
    >>> fastest_words(game(['What', 'great', 'luck'], [p0, p1]))
    [['What'], ['great', 'luck']]
    """
    players = range(len(all_times(game)))  # An index for each player
    words = range(len(all_words(game)))    # An index for each word
    # BEGIN PROBLEM 10
    "*** YOUR CODE HERE ***"
    def create_fastest_structure(players):
        fastest = []
        for _ in players:
            fastest.append([])
        return fastest


    def find_fastest_player(game, word_index):
        """
        find the fastest player for one the word in
        specific index.

        """
        nonlocal players
        min_time = float('inf')
        for player in players:
            if time(game, player, word_index) < min_time:
                min_time = time(game, player, word_index)
                min_player = player
        return min_player


    fastest = create_fastest_structure(players)
    for word_index in words:
        fastest[find_fastest_player(game, word_index)].append(word_at(game, word_index))
    return fastest



    # END PROBLEM 10


def game(words, times):
    """A data abstraction containing all words typed and their times."""
    assert all([type(w) == str for w in words]), 'words should be a list of strings'
    assert all([type(t) == list for t in times]), 'times should be a list of lists'
    assert all([isinstance(i, (int, float)) for t in times for i in t]), 'times lists should contain numbers'
    assert all([len(t) == len(words) for t in times]), 'There should be one word per time.'
    return [words, times]


def word_at(game, word_index):
    """A selector function that gets the word with index word_index"""
    assert 0 <= word_index < len(game[0]), "word_index out of range of words"
    return game[0][word_index]


def all_words(game):
    """A selector function for all the words in the game"""
    return game[0]


def all_times(game):
    """A selector function for all typing times for all players"""
    return game[1]


def time(game, player_num, word_index):
    """A selector function for the time it took player_num to type the word at word_index"""
    assert word_index < len(game[0]), "word_index out of range of words"
    assert player_num < len(game[1]), "player_num out of range of players"
    return game[1][player_num][word_index]


def game_string(game):
    """A helper function that takes in a game object and returns a string representation of it"""
    return "game(%s, %s)" % (game[0], game[1])

enable_multiplayer = False  # Change to True when you

##########################
# Extra Credit #
##########################

key_distance = get_key_distances()
def key_distance_diff(start, goal, limit):
    """ A diff function that takes into account the distances between keys when
    computing the difference score.
    >>>
    1.650081475501692
    """

    start = start.lower()  # converts the string to lowercase
    goal = goal.lower()  # converts the string to lowercase
    if limit < 0:
        return float('inf')
    elif len(start) == 0 or len(goal) == 0:
        if max(len(start), len(goal)) <= limit:
            return max(len(start), len(goal))
        else:
            return float('inf')
    else:
        if start[0] == goal[0]:
            return key_distance_diff(start[1:], goal[1:], limit)
        else:
            add_diff = key_distance_diff(start, goal[1:], limit - 1) + 1
            remove_diff = key_distance_diff(start[1:], goal, limit - 1) + 1
            key_dis = key_distance[(start[0], goal[0])]
            substitute_diff = key_distance_diff(start[1:], goal[1:], limit - key_dis) + key_dis
            return min(add_diff, remove_diff, substitute_diff)
    # END PROBLEM EC1

def memo(f):
    """A memoization function as seen in John Denero's lecture on Growth"""

    cache = {}
    def memoized(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return memoized


key_distance_diff = count(key_distance_diff)


def faster_autocorrect(user_word, valid_words, diff_function, limit):
    """A memoized version of the autocorrect function implemented above."""

    # BEGIN PROBLEM EC2
    "*** YOUR CODE HERE ***"

    # END PROBLEM EC2


##########################
# Command Line Interface #
##########################


def run_typing_test(topics):
    """Measure typing speed and accuracy on the command line."""
    paragraphs = lines_from_file('data/sample_paragraphs.txt')
    select = lambda p: True
    if topics:
        select = about(topics)
    i = 0
    while True:
        reference = choose(paragraphs, select, i)
        if not reference:
            print('No more paragraphs about', topics, 'are available.')
            return
        print('Type the following paragraph and then press enter/return.')
        print('If you only type part of it, you will be scored only on that part.\n')
        print(reference)
        print()

        start = datetime.now()
        typed = input()
        if not typed:
            print('Goodbye.')
            return
        print()

        elapsed = (datetime.now() - start).total_seconds()
        print("Nice work!")
        print('Words per minute:', wpm(typed, elapsed))
        print('Accuracy:        ', accuracy(typed, reference))

        print('\nPress enter/return for the next paragraph or type q to quit.')
        if input().strip() == 'q':
            return
        i += 1


@main
def run(*args):
    """Read in the command-line argument and calls corresponding functions."""
    import argparse
    parser = argparse.ArgumentParser(description="Typing Test")
    parser.add_argument('topic', help="Topic word", nargs='*')
    parser.add_argument('-t', help="Run typing test", action='store_true')

    args = parser.parse_args()
    if args.t:
        run_typing_test(args.topic)