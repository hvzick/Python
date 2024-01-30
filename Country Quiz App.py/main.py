import random
from datetime import date
import os
import sys

# Use datetime module for todays date
date = date.today()

# Delete all previous files
def delete_previously_created_files():

    # Check files in the current directory
    for file_name in os.listdir():

        # Check if the file is text file but not Country Data file
        if file_name.endswith('.txt') and not(file_name.startswith('Country Data')):

            # Delete those files
            os.unlink(file_name)

    # Return to main function        
    return

def take_user_input():
    try:
        # Ask for maximum roll of the class
        max_roll = int(input('Enter maximum roll of the class: '))

        # Ask for number of questions from user
        questions_no = int(input('How many questions will be for each quiz: '))

        # Ask for number participants from user
        students_no = int(input('How many students will participate in quiz: '))

        # Throw Value Error if students_no is > max_roll
        if students_no > max_roll:
            sys.exit("Participants can't be more than the roll of class")

    # Catch Value Error
    except ValueError:
        print('Input can only be positive integers')
    
    # Return to main function
    return questions_no, students_no

def parse_country_data_file():
        
    # Create a dictionary to store Countries and Capitals
    countries_dict = {}

    # Parse the Country Data file to extract Countries and Capitals
    with open('Country Data.txt', 'r',  encoding='utf-8') as parsed_country_data_file:

        # Skip the header line
        parsed_country_data_file.readline()

        # iterate through each Country in the file
        for country in parsed_country_data_file:

            # Remove the spaces and make each line into a list
            country_info = country.strip().split(';')

            # In Country Data file the Country name is at 1 index so we store it in country_name variable
            country_name = country_info[1]

            # In Country Data file the Capital name is at 1 index so we store it in country_capital variable
            country_capital = country_info[2]

            # Here we add the Country name and capital to the dictionary
            countries_dict[country_name] = country_capital

            # in each iteration the Country name and capital will be added to the dictionary until the file is empty
    
    # Return countries to main function
    return countries_dict


# Generate Question and Answer files
def generate_qna(questions_l, students_l, countries_l):

    # Iterate through the number of students
    for quiz_number in range(students_l):
        try:
            # create new file name = quiz_number+1 beacuse quiz_number = 0 at first
            with open(f'Questions{quiz_number+1}.txt', 'w', encoding='utf-8') as question_file:
                
                # Write Name and Date on the Question file
                question_file.write(f'Name: \nDate: {date} \n')

                # Write Form number on the question file
                question_file.write(f"{' ' * 30} Country Capitals Quiz Form {quiz_number+1}\n\n")

                # Iterate throught the number of question for 1 student
                for question_number in range(questions_l):

                    # Turn Keys of dictionary to a list
                    country_list = list(countries_l.keys())

                    # Choose a Country from the above created list
                    question_country = random.choice(country_list)

                    # Select the Correct Capital answer of the above chosen Country
                    correct_answer = countries_l[question_country]

                    # Turn Values of dictionary to a list
                    capital_list = list(countries_l.values())

                    # Create new list which contains the correct answer and 3 wrong answers
                    answer_list = [correct_answer] + random.sample(capital_list, 3)

                    # Schuffle the answer list
                    random.shuffle(answer_list)

                    # Write question on Form
                    question_file.write(f'{question_number+1}. Capital of {question_country} is:\n')

                    # Create l variable
                    l = 0

                    # Create letters list for the answer options
                    letters = ['A', 'B', 'C', 'D']

                    # Iterate through the answer list to write on the Form after the Question
                    for i in answer_list:
                        question_file.write(f'      {letters[l]}. {i}\n')

                    # Leave a line after every question
                    question_file.write('\n')

                    # Create an Answer file to write correct answers t0
                    with open(f'Answers{quiz_number+1}.txt', 'a', encoding='utf-8') as   answer_file:
                        answer_file.write(f"{question_number+1}. {correct_answer}\n")

        # Catch exceptions
        except Exception as e:
            print(f'Failed to create the File Questions{quiz_number+1}.txt')
            


def main():

    # Call the functions to delete previous quiz files
    delete_previously_created_files()

    # Call user input file
    questions_main, students_main = take_user_input()

    # Call parsing data function 
    countries_main = parse_country_data_file()

    # Call function to create file of QnA
    generate_qna(questions_main, students_main, countries_main)



if __name__ == '__main__':
    main()
