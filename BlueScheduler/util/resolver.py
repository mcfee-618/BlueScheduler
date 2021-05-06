import os
import re

from BlueScheduler.models.project import *
from BlueScheduler.models.task import *


class Resolver:

    def __init__(self):
        self.__projects = None
        self.__current_project = None

    def resolve(self, path):
        self.__projects = dict()
        if not os.path.exists(path):
            raise Exception("path {} not found".format(path))
        if not os.path.isdir(path):
            raise Exception("path {} not dir".format(path))
        self.resolve_file(path)
        return self.__projects

    def resolve_file(self, path):
        if os.path.isfile(path):
            with open(path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                self.resolve_contents(lines)

        for _, directories, files in os.walk(path):
            for directory in directories:
                self.resolve_file(os.path.join(path, directory))
            for file in files:
                if re.match(".*todo$", file) is not None:
                    self.resolve_file(os.path.join(path, file))
            break

    def resolve_contents(self, contents):
        self.__current_project = None
        for content in contents:
            content = content.strip()
            if not content:
                pass
            if Project.is_project(content):
                new_project = Project.get_project(content)
                if new_project.name in self.__projects:
                    self.__current_project = self.__projects[new_project.name]
                else:
                    self.__projects[new_project.name] = new_project
                    self.__current_project = new_project
            if Task.is_task(content) and self.__current_project is not None:
                task = Task.get_task(content)
                self.__current_project.add_task(task)

    def get_projects(self):
        return self.__projects


if __name__ == "__main__":
    resolver = Resolver()
    projects = resolver.resolve("../../plans")
    for project_name in projects:
        project = projects[project_name]
        tasks = project.get_tasks(TaskStatus.new) + project.get_tasks(TaskStatus.start)
        for task in tasks:
            print(project_name + ":" + str(task))
