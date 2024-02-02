class QuizBrain:
    def __init__(self, q_list):
        self.q_no = 0
        self.q_list = q_list
        self.score = 0

    def still_has_questions(self):
        if self.q_no < len(self.q_list):
            return True
        else:
            return False

    def next_question(self):
        user_answer = input(f"Q{self.q_no+1}. {self.q_list[self.q_no].text} True/False?: ")
        self.check_answer(user_answer)
        self.q_no += 1

    def check_answer(self,user_answer):
        if user_answer == self.q_list[self.q_no].answer:
            print("You got it right")
            self.score += 1
        else:
            print("You got it wrong")
        print(f"The correct answer was {self.q_list[self.q_no].answer}")
        print(f"Your current score is {self.score}/{self.q_no+1}")
