#!/usr/bin/python3

"""
A script that fetches info about an employee from an API
"""
import requests
from sys import argv


class Employee():
    """
    A class to encapsulate employee logic
    """
    __name = ""
    __id = None
    __tasks = []
    __completed = None

    def __init__(self, employee_id, user_dict, task_list):
        """constructor for the employee object"""
        self.id = employee_id
        self.name = user_dict
        self.tasks = task_list
        self.completed = self.tasks

    @property
    def id(self):
        """property getter"""
        return self.__id

    @property
    def name(self):
        """property getter"""
        return self.__name

    @property
    def tasks(self):
        """property getter"""
        return self.__tasks

    @property
    def completed(self):
        """property getter"""
        return self.__completed

    @completed.setter
    def completed(self, tasks):
        """property setter"""
        count = 0
        for task in tasks:
            if task.get('completed'):
                count += 1
        self.__completed = count

    @name.setter
    def name(self, dict=None):
        """A function to set the name of the employee"""
        self.__name = dict.get("name", None)

    @id.setter
    def id(self, value):
        """A function to set the id of the employee"""
        self.__id = value

    @tasks.setter
    def tasks(self, task_dict=None):
        """A function to set the tasks of a particular employee"""
        if task_dict:
            for task in task_dict:
                if task.get("userId", None) == int(self.id):
                    new_task = {}
                    new_task["title"] = task.get('title', None)
                    new_task["completed"] = task.get("completed", None)
                    self.__tasks.append(new_task)

    def __str__(self):
        """A function to print the object"""
        emp_string = f"Employee {self.name} is done "\
            f"with tasks({self.completed}/{len(self.tasks)}):"
        print(emp_string)
        for task in self.tasks:
            if task.get('completed'):
                f = f"\t {task.get('title')}"
                print(f)
        return ""


if __name__ == '__main__':
    employee_id = argv[1]
    task_url = "https://jsonplaceholder.typicode.com/todos"
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"

    with requests.get(user_url) as resp:
        if resp.status_code == 200:
            user_dict = resp.json()
    with requests.get(task_url) as resp:
        if resp.status_code == 200:
            task_list = resp.json()

    employee = Employee(employee_id, user_dict, task_list)
    print(employee, end="")
