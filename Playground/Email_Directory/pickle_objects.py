# This program demonstrates object pickling.
import pickle

# main function


def pickle(email_dict, file_name):
    again = 'y'  # To control loop repetition

    # Open a file for binary writing.
    output_file = open(file_name, 'wb')

    # Get data until the user wants to stop.
    for entry in email_dict:
        # Get data about a person and save it.
        save_data(entry, output_file)

        # Does the user want to enter more data?
        again = input('Enter more data? (y/n): ')

    # Close the file.
    output_file.close()

# The save_data function gets data about a person,
# stores it in a dictionary, and then pickles the
# dictionary to the specified file.


def save_data(entry, output_file):
    # Create an empty dictionary.
    person = {}

    # Get data for a person and store
    # it in the dictionary.
    person['name'] = entry['name']
    person['email'] = entry['email']

    # Pickle the dictionary.
    pickle.dump(person, output_file)
