# We have provided you with two lists, letters and points.
# We would like to combine these two into a dictionary
# that would map a letter to its point value.

letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
           "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3,
          4, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10]

# Using a list comprehension and zip, create a dictionary called
# letter_to_points that has the elements of letters as the keys and
# the elements of points as the values.
letter_to_points = {key: value for key, value in zip(letters, points)}

# Our letters list did not take into account blank tiles.
# Add an element to the letter_to_points dictionary that has a key of " "
# and a point value of 0.
letter_to_points[" "] = 0

# We want to create a function that will take in a word and
# return how many points that word is worth.


def score_word(word):
    total_points = 0
    for letter in word:
        total_points += letter_to_points.get(letter, 0)
    return total_points


# Let’s test this function!
brownie_points = score_word("BROWNIE")
print(brownie_points)

# Create a dictionary called player_to_words that
# maps players to a listof the words they have played.
player_to_words = {"player1": ["BLUE", "TENNIS", "EXIT"],
                   "wordNerd": ["EARTH", "EYES", "MACHINE"],
                   "Lexi Con": ["ERASER", "BELLY", "HUSKY"],
                   "Prof Reader": ["ZAP", "COMA", "PERIOD"]}

# Create an empty dictionary called player_to_points.
player_to_points = {}


def play_word(player, word):  # Add a word a player played to player_to_words
    player_to_words[player].append(word)


def update_points_total():  # Update the total of points in player_to_points
    # Iterate through the items in player_to_words.
    for player, words in player_to_words.items():
        player_points = 0
        # Iterate through each word in words and add the score
        for word in words:
            player_points += score_word(word)
        player_to_points[player] = player_points


update_points_total()  # Update the total of points in player_to_points
print(player_to_points)  # The winner is wordNerd

# Add a new word "ZEBRA" to Prof Reader's played words list
play_word("Prof Reader", "ZEBRA")
update_points_total()  # Re update the total of points
print(player_to_points)  # Now the winner is Prof Reader
