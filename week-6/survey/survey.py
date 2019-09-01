# --- Instructions:
    # Must use OOP. You should build your program in a modular way, so that once you have the basic structure set up, it is easy to add additional questions and/or sections.
    # There must be at least 3 sections of the survey. Each section must have a title and description, and a minimum of 3 multichoice questions.
    # There must be a series of qualifying questions that the user is asked first. The users answers will decide which survey sections they will be asked to complete. (e.g. to answer the meerkat section of the survey, they must like meerkats).
    # Each question will consist of the question text followed by a minimum of 2 answers for the user to choose between. The user will select their answer by typing in the code that corresponds to the answer, as given by your program.
    # The user must be forgiven for any incorrect input (i.e. your program must handle incorrect user input).

#doing it all in one for simplicity 

class Answer(self):

    def __init__(self,answer_letter,answer_text):
        self.answer_letter = answer_letter 
        self.answer_text = answer_text

class Question(self):

    def __init__(self, question_letter, question_text):
        self.question_l = question_letter
        self.question_and_answers: {}

    def add_answer(self, answer):
        self.questions_and_answers.append(answer)
    
class Section(self):
    
    def __init__(self, qualifying_question, description):
        self.qualifying_question = qualifying_question
        self.description = description

    def section_setup(self):
        print(self.description)
        print(self.qualifying_question)


# Section 1 Setup
Section('Which type of respondent are you?',)