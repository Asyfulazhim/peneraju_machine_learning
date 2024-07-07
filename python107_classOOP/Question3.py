class MathProblemSolver:
    def __init__(self):
        pass

    def parse_problem(self, words):
        words = words.lower()
        words = words.replace(" ", "")
        words = words.replace("whatis", "")
        words = words.replace("?", "")
        words = words.replace("plus", "+")
        words = words.replace("minus", "-")
        words = words.replace("multipliedby", "*")
        words = words.replace("dividedby", "/")
        return words

    def evaluate_problem(self, words):
        result = words[0]
        for i in range(1, len(words), 2):
            operator = words[i]
            operand = words[i + 1]
            if operator == "+":
                result = str(int(result) + int(operand))
            elif operator == "-":
                result = str(int(result) - int(operand))
            elif operator == "*":
                result = str(int(result) * int(operand))
            elif operator == "/":
                result = str(int(result) / int(operand))
        return int(result)

solve = MathProblemSolver()
words = input()
words = solve.parse_problem(words)
result = solve.evaluate_problem(words)
print(result)