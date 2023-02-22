"""
The following are the steps to solve this problem:

1. the program needs to read a pipe-delimited text file containing name and date of birth values, calculate the age
of each person, sort the data by date of birth, and display the sorted data along with the average age of all people
in the file.

2.  we need a function to calculate age from a date of birth, a function to read data from a file, a function to sort
the data, and a function to display the results.

Here is how it works:

The calculate_age() function takes a datetime.date object representing the date of birth and returns the age in
years.

The read_data() function reads the pipe-delimited file and returns a list of tuples containing the name and
date of birth for each person in the file. It handles file errors using a try-except block and returns an empty list
if an error occurs.

The sort_data() function sorts the data by date of birth using the sorted() function and a lambda
function to extract the date of birth from each tuple.

The display_data() function prints the sorted data to the console, including the name, date of birth, and age of each
person.

The calculate_average_age() function calculates the average age of the people in the file. It checks if the data is
empty before calculating the average to avoid division by zero. Finally, the program prompts the user for the
filename, reads the data from the file, sorts it by date of birth, displays it, and prints the average age to the
console.

"""
import datetime
import csv
import os


def calculate_age(born: datetime.date) -> int:
    today = datetime.date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))


def read_data(filename: str) -> list:
    """
    Reads data from a CSV file and returns a list of tuples containing
    the name and date of birth of each person in the file.

    Args:
        filename (str): The name of the file to read.

    Returns:
        A list of tuples in the form (name, date_of_birth).
    """
    try:
        # Open the file for reading with specified options
        with open(filename, 'r', newline='', encoding='utf-8') as file:
            # Use CSV reader to read data from file and split on the '|' character
            data = csv.reader(file, delimiter='|')
            name_dob = []
            # Loop over the rows of the CSV file
            for name, dob in data:
                # Remove leading and trailing whitespace from name and dob fields
                name = name.strip()
                dob = datetime.datetime.strptime(dob.strip(), '%Y-%m-%d').date()
                # Get the current date
                today = datetime.datetime.now().date()
                # Check if dob is not in the future

                if today < dob:
                    raise Exception("The date supplied is in the future")
                # Append the name and dob to the list
                name_dob.append((name, dob))
            # Return the list of name and dob tuples
            return name_dob

    except FileNotFoundError:
        # Handle the case where the file does not exist
        print(f"Error: file '{filename}' not found.")
    except PermissionError:
        # Handle the case where the user does not have permission to access the file
        print(f"Error: permission denied for file '{filename}'.")
    except UnicodeDecodeError:
        # Handle the case where the file contains invalid characters
        print(f"Error: file '{filename}' contains invalid characters.")
    except ValueError:
        # Handle the case where the file contains invalid data format
        print(f"Error: invalid data format in file '{filename}'.")
    except Exception as e:
        # Handle any other exceptions that may occur
        print(f"Error reading data from file: {e}")
    # If there was an error, return an empty list
    return []


def sort_data(data: list) -> list:
    """
    Sorts a list of tuples containing name and date of birth
    by date of birth.

    Args:
        data (list): A list of tuples in the form (name, date_of_birth).

    Returns:
        A sorted list of tuples in the form (name, date_of_birth).
    """

    def get_date_of_birth(person):
        return person[1]

    return sorted(data, key=get_date_of_birth)


def display_data(data: list) -> None:
    """
    Prints a formatted table of data showing name, date of birth,
    and age for each person in a list of tuples.

    Args:
        data (list): A list of tuples in the form (name, date_of_birth).
    """
    print("Name\t\tDate of Birth\tAge")
    for name, dob in data:
        age = calculate_age(dob)
        print(f"{name}\t{dob.strftime('%d-%m-%Y')}\t{age}")


def calculate_average_age(data: list) -> float:
    """
    Calculates the average age of a list of tuples containing
    name and date of birth.

    Args:
        data (list): A list of tuples in the form (name, date_of_birth).

    Returns:
        The average age as a float.
    """
    if not data:
        return 0
    total_age = sum([calculate_age(dob) for _, dob in data])
    return total_age / len(data)


if __name__ == '__main__':
    filename = input("Enter the filename to read: ")
    if not os.path.isfile(filename):
        print(f"Error: file '{filename}' not found.")
    else:
        data = read_data(filename)
        sorted_data = sort_data(data)
        display_data(sorted_data)
        avg_age = calculate_average_age(data)
        print(f"Average age: {avg_age:.2f}")
