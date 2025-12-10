class Question:
    def __init__(self, text, points):
        self.text = text
        self.points = points

    def check(self, answer):
        raise NotImplementedError("Subclasses must implement check().")

    def __str__(self):
        return f"{self.text} ({self.points} pts)"


class SingleChoiceQuestion(Question):
    def __init__(self, text, points, options, correct_answer):
        super().__init__(text, points)
        self.options = options
        self.correct_answer = correct_answer

    def check(self, answer):
        a = str(answer).strip().lower()
        c = str(self.correct_answer).strip().lower()
        return a == c

    def __str__(self):
        opts = "\n".join(f"  {opt}" for opt in self.options)
        return f"{super().__str__()}\n{opts}"


class MultipleChoiceQuestion(Question):
    def __init__(self, text, points, options, correct_answers):
        super().__init__(text, points)
        self.options = options
        self.correct_answers = correct_answers

    def check(self, answer):
        if not isinstance(answer, (list, tuple)):
            return False
        norm = lambda s: str(s).strip().lower()
        correct_set = {norm(x) for x in self.correct_answers}
        answer_set = {norm(x) for x in answer}
        return answer_set == correct_set  # exact match, order irrelevant

    def __str__(self):
        opts = "\n".join(f"  {opt}" for opt in self.options)
        return f"{super().__str__()}\n{opts}"


class OpenQuestion(Question):
    def __init__(self, text, points, correct_answer):
        super().__init__(text, points)
        self.correct_answer = correct_answer

    def check(self, answer):
        return str(answer).strip().lower() == str(self.correct_answer).strip().lower()


class Quiz:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def evaluate(self, answers):
        total_points = sum(q.points for q in self.questions)
        score = 0
        # If fewer answers are provided, treat missing as wrong; if extra, ignore.
        for q, ans in zip(self.questions, answers):
            if q.check(ans):
                score += q.points
        return score, total_points


if __name__ == "__main__":
    quiz = Quiz("Sample Quiz")

    q1 = SingleChoiceQuestion(
        text="Capital of France?",
        points=5,
        options=["A) Paris", "B) Rome", "C) Berlin", "D) Madrid"],
        correct_answer="A"
    )
    q2 = MultipleChoiceQuestion(
        text="Select prime numbers:",
        points=10,
        options=["A) 2", "B) 4", "C) 5", "D) 9"],
        correct_answers=["A", "C"]
    )
    q3 = OpenQuestion(
        text="Who wrote '1984'?",
        points=5,
        correct_answer="George Orwell"
    )
    q4 = SingleChoiceQuestion(
        text="Cine e fratele lui Lamine Yamal?",
        points=10,
        options=["A) Dumil Ankur", "B) Ceszlo Boz", "C) Catalin Dicu", "D) Soyeyan Masele", "E) Yamil Angura"],
        correct_answer="Yamil Angura"
    )


    quiz.add_question(q1)
    quiz.add_question(q2)
    quiz.add_question(q3)
    quiz.add_question(q4)

    answers = ["A", ["A", "C"], "george orwell", "Catalin Dicu"] # ultima e gresita
    score, total = quiz.evaluate(answers)
    print(f"Score: {score}/{total}")
