'''
The Task class should receive a name (string) and a due_date (str) upon initialization. A task also has two attributes: comments (empty list) and completed set to False by default.
The Task class should also have five additional methods:
-	change_name(new_name: str)
o	Changes the name of the task and returns the new name.
o	If the new name is the same as the current name, returns "Name cannot be the same."

-	change_due_date(new_date: str)
o	Changes the due date of the task and returns the new date.
o	If the new date is the same as the current date, returns "Date cannot be the same."

-	add_comment(comment: str)
o	Adds a comment to the task.

'''

from typing import List


class Task:
    def __init__(self, name: str, due_date: str):
        self.name = name
        self.due_date = due_date
        self.comments: List[str] = []
        self.completed = False

    # don't forget to access the class
    def change_name(self, new_name: str):
        if self.name == new_name:
            return "Name cannot be the same."
        self.name = new_name
        return self.name

    def change_due_date(self, new_date: str):
        if self.due_date == new_date:
            return "Date cannot be the same."
        self.due_date = new_date
        return self.due_date

    def add_comment(self, comment: str):
        self.comments.append(comment)

    def edit_comment(self, comment_number: int, new_comment: str):
        if 0 <= comment_number <= len(self.comments) - 1:
            self.comments[comment_number] = new_comment
            return ", ".join(self.comments)
        return "Cannot find comment."

    def details(self):
        return f"Name: {self.name} - Due Date: {self.due_date}"