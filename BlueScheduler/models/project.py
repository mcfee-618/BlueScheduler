import re

from BlueScheduler.models.task import Task, TaskStatus


class Project:
    def __init__(self, name):
        self.name = name
        self.__completed_tasks = []
        self.__unstarted_tasks = []
        self.__proceed_tasks = []
        self.__canceled_tasks = []

    def add_task(self, task):
        if task.status == TaskStatus.new:
            self.__unstarted_tasks.append(task)
        elif task.status == TaskStatus.start:
            self.__proceed_tasks.append(task)
        elif task.status == TaskStatus.finish:
            self.__completed_tasks.append(task)
        elif task.status == TaskStatus.cancel:
            self.__canceled_tasks.append(task)

    def get_tasks(self, task_status=None):
        if task_status is None:
            return self.__unstarted_tasks + self.__proceed_tasks + self.__completed_tasks + self.__canceled_tasks
        if task_status == TaskStatus.finish:
            return self.__completed_tasks
        elif task_status == TaskStatus.start:
            return self.__proceed_tasks
        elif task_status == TaskStatus.new:
            return self.__unstarted_tasks
        elif task_status == TaskStatus.cancel:
            return self.__canceled_tasks

    def get_completed_tasks(self, start_time, end_time):
        tasks = []
        for task in self.__completed_tasks:
            if start_time is not None:
                if task.finished_time is None:
                    continue
                if start_time > Task.parse_date(task.finished_time):
                    continue
            if end_time is not None:
                if task.finished_time is None:
                    continue
                if end_time < Task.parse_date(task.finished_time):
                    continue
            tasks.append(task)
        return tasks

    @staticmethod
    def is_project(content):
        content = content.strip()
        if re.match(".*:$", content) is not None:
            return True
        return False

    @staticmethod
    def get_project(content):
        content = content.strip()
        return Project(content[0:-1])


if __name__ == "__main__":
    assert Project.is_project("新项目:")
    project = Project.get_project("新项目:")
    assert project.name == "新项目"
