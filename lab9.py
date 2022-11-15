# Jacob Jung, Nathaniel Battad, Quan Nguyen
# CS 2520 Lab 9

import random


class Students:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.cur_score = 0
        self.high_score = 0

    def update_score(self, cur_score):
        self.cur_score = cur_score

        if self.cur_score > self.high_score:
            self.high_score = self.cur_score

    def display_scores(self):
        print("Current score: ", self.cur_score, "High score: ", self.high_score)


class Quiz:
    def __init__(self, student):
        self.quiz_taking_student = student

    question_bank = [
        {
            "question": "Which animal can be seen on the Porsche logo?",
            "choices": {"a": "Bull", "b": "Horse", "c": "Cat", "d": "Goat"},
            "answer": "b"
        },
        {
            "question": "How many strand of hair do we usually lose a day?",
            "choices": {"a": "between 10-25", "b": "between 25-50", "c": "between 50-100", "d": "more than 100"},
            "answer": "c"
        },
        {
            "question": "Who is depicted on the US hundred dollar bill?",
            "choices": {"a": "Benjamin Franklin", "b": "George Washington", "c": "Alexander Hamilton",
                        "d": "Abraham Lincoln"},
            "answer": "a"
        },
        {
            "question": "What color is the Fed in the FedEx logo?",
            "choices": {"a": "green", "b": "orange", "c": "yellow", "d": "purple"},
            "answer": "d"
        },
        {
            "question": "___ percent of human body is water.",
            "choices": {"a": "30", "b": "40", "c": "60", "d": "80"},
            "answer": "c"
        },
        {
            "question": "What is the largest internal organ in your body?",
            "choices": {"a": "liver", "b": "stomach", "c": "heart", "d": "lungs"},
            "answer": "a"
        },
        {
            "question": "How many seconds are in a day?",
            "choices": {"a": "72,000", "b": "86,400", "c": "82,800", "d": "79,200"},
            "answer": "b"
        },
        {
            "question": "In what year was McDonald's founded?",
            "choices": {"a": "1940", "b": "1945", "c": "1950", "d": "1955"},
            "answer": "d"
        },
        {
            "question": "In what year was Facebook founded?",
            "choices": {"a": "2004", "b": "2008", "c": "2010", "d": "2012"},
            "answer": "a"
        },
        {
            "question": "What currency does Poland use?",
            "choices": {"a": "kip", "b": "euro", "c": "zloty", "d": "peso"},
            "answer": "c"
        },
        {
            "question": "Where did the 2000 Summer Olympics take place?",
            "choices": {"a": "Sydney, Australia", "b": "Tokyo, Japan", "c": "Paris, France", "d": "Seoul, South Korea"},
            "answer": "a"
        },
        {
            "question": "Which state does NOT share a border with California?",
            "choices": {"a": "Arizona", "b": "Nevada", "c": "Oregon", "d": "Washington"},
            "answer": "d"
        },
        {
            "question": "Approximately how many pounds are in a ton?",
            "choices": {"a": "1000", "b": "1500", "c": "2000", "d": "2500"},
            "answer": "c"
        },
        {
            "question": "What is a nine-sided polygon called?",
            "choices": {"a": "septagon", "b": "nonagon", "c": "octagon", "d": "hexagon"},
            "answer": "b"
        },
        {
            "question": "What number does every Major League Baseball player wear on April 15?",
            "choices": {"a": "2", "b": "16", "c": "42", "d": "3"},
            "answer": "c"
        },
        {
            "question": "What is the diameter of the average basketball hoop?",
            "choices": {"a": "12 inches", "b": "16 inches", "c": "18 inches", "d": "20 inches"},
            "answer": "c"
        },
        {
            "question": "What percentage of the Earth's wildlife is found in the ocean?",
            "choices": {"a": "72", "b": "56", "c": "94", "d": "80"},
            "answer": "c"
        },
        {
            "question": "In American football, how many points is a touchdown worth?",
            "choices": {"a": "6", "b": "7", "c": "8", "d": "9"},
            "answer": "a"
        },
        {
            "question": "Where is the world's largest Starbucks located?",
            "choices": {"a": "Chicago", "b": "Seattle", "c": "New York", "d": "Los Angeles"},
            "answer": "a"
        },
        {
            "question": "In what year was the first iPod released?",
            "choices": {"a": "2005", "b": "2003", "c": "2001", "d": "2004"},
            "answer": "c"
        },
    ]

    def question(self, quiz_taking_student):
        self.quiz_taking_student = quiz_taking_student
        correct_answer = 0

        for q in random.sample(self.question_bank, 5):
            print("\nQuestion:", q.get('question', 'choices'))

            answer = input("{} \ntype your answer: ".format(q.get('choices')).lower())

            if answer == q.get('answer'):
                print("Correct!")
                correct_answer += 1

            else:
                print("Wrong!")

        print("\nYou got {} / 5 questions right ".format(correct_answer))
        quiz_taking_student.update_score(correct_answer)


student1 = Students("Jacob Jung", 1234567890)
quiz = Quiz(student1)
quiz.question(student1)
student1.display_scores()
