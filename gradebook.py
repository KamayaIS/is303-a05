"""
Kevin Amaya
IS 303 - A05

Inputs: 
- Ask for assignment name
- Ask for assignment score
- ask for max score possible

Processes:
- Calculate letter grade based on assignment score
- Calculate average score for the course
- Find the highest and lowest score for the course

Outputs:
- Display letter grade for the assignment
- Display average score for the course
- Display highest and lowest score for the course
"""

class assignment:
    def __init__(self, name, score, max_score):
        self.name = name.title()
        self.score = score
        self.max_score = max_score

    def calculate_letter_grade(self):
        percentage = (self.score / self.max_score) * 100
        if percentage >= 90:
            return 'A'
        elif percentage >= 80:
            return 'B'
        elif percentage >= 70:
            return 'C'
        elif percentage >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        return f"{self.name}: {self.score}/{self.max_score} ({self.calculate_letter_grade()})"
    
class gradebook:
    def __init__(self):
        self.assignments = []

    def add_assignment(self, assignment):
        self.assignments.append(assignment)

    def calculate_average_score(self):
        total_score = sum(assignment.score for assignment in self.assignments)
        return total_score / len(self.assignments) if self.assignments else 0

    def find_highest_score(self):
        return max(assignment.score for assignment in self.assignments) if self.assignments else 0

    def find_lowest_score(self):
        return min(assignment.score for assignment in self.assignments) if self.assignments else 0

    def calculate_course_grade(self):
        avg = self.calculate_average_score()
        if avg >= 90:
            return 'A'
        elif avg >= 80:
            return 'B'
        elif avg >= 70:
            return 'C'
        elif avg >= 60:
            return 'D'
        else:
            return 'F'
    
    def __str__(self):
        result = ""
        for a in self.assignments:
            result += str(a) + "\n"
        result += f"\nGradebook Summary:\n"
        result += f"Average Score: {self.calculate_average_score():.2f} ({self.calculate_course_grade()})\n"
        result += f"Highest Score: {self.find_highest_score()}\n"
        result += f"Lowest Score: {self.find_lowest_score()}"
        return result

if __name__ == "__main__":
    main = gradebook()

    while True:
        print()
        name = input("Enter assignment name (or 'done' to finish): ")
        if name.lower() == "done":
            break
        while True:
            score = float(input("Enter score earned: "))
            if 0 <= score <= 100:
                break
            print("Score must be between 0 and 100.")

        while True:
            max_score = float(input("Enter max score possible: "))
            if 0 <= max_score <= 100:
                break
            print("Max score must be between 0 and 100.")
        main.add_assignment(assignment(name, score, max_score))

    print()
    print(main)