# --- Instructions:
    # Must use OOP. You should build your program in a modular way, so that once you have the basic structure set up, it is easy to add additional questions and/or sections.
    # There must be at least 3 sections of the survey. Each section must have a title and description, and a minimum of 3 multichoice questions.
    # There must be a series of qualifying questions that the user is asked first. The users answers will decide which survey sections they will be asked to complete. (e.g. to answer the meerkat section of the survey, they must like meerkats).
    # Each question will consist of the question text followed by a minimum of 2 answers for the user to choose between. The user will select their answer by typing in the code that corresponds to the answer, as given by your program.
    # The user must be forgiven for any incorrect input (i.e. your program must handle incorrect user input).

#doing it all in one for simplicity 

class Answer:

    def __init__(self, code, answer_text):
        self.code = code 
        self.answer_text = answer_text
        # self.next_question = Question()
        # self.action = action

class Question:

    def __init__(self, question_text):
        self.question_text = question_text
        self.answers = []
        self.next_question: Question()

    def add_answer(self, answer):
        self.answers.append(answer)

    def get_answer_by_code(self,answer):
        pass

class Section(Question):
    
    def __init__(self, qualifying_question, first_question, description):
        self.qualifying_question = Question()
        self.first_question = Question()
        self.description = description

    def section_setup(self):
        print(self.description)
        print(self.qualifying_question)


# Qualifying Questions
html_qualifying = Question('Would you say you have a good understanding of HTML & CSS?')
html_qualifying.add_answer(Answer(code='A', answer_text='Yes'))
html_qualifying.add_answer(Answer(code='B', answer_text='No'))

python_qualifying = Question('Would you say you have a good understanding of Python & Django?')
python_qualifying.add_answer(Answer(code='A', answer_text='Yes'))
python_qualifying.add_answer(Answer(code='B', answer_text='No'))

