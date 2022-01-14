class Question:
    def __init__(self, prompt):
        self.prompt = prompt['Q']
        self.options = f" (a) {prompt['A']}\n (b) {prompt['B']}\n (c) {prompt['C']}\n (d) {prompt['D']}\n"
        self.answer = prompt['R']