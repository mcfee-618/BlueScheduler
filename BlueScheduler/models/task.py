import re
import time
from datetime import datetime,date,time
from enum import Enum

## identifer
new_pattern = "^☐.*"
finish_pattern = "^✔.*"
cancel_pattern = "^✘.*"

## tag-status
started_pattern = ".*@started\((.*)\)"
done_pattern = ".*@done\((.*)\)"
cancelled_pattern = ".*@cancelled\((.*)\)"
schedule_pattern = ".*@schedule\((.*)\)"

## tag-remark
remark_pattern = ".*@remark\((.*)\)"

## tag-level
low_pattern = "@low"
high_pattern = "@high"
critical_pattern = "@critical"


class TaskStatus(Enum):
    new = 0
    start = 1
    finish = 2
    cancel = 3


class TaskLevel(Enum):
    low = 0
    high = 1
    critical = 2


class Task:

    def __init__(self, name, text, status):
        self.name = name
        self.text = text
        self.started_time = None
        self.finished_time = None
        self.schedule_time = None
        self.status = status
        self.level = TaskLevel.high
        self.remark = None

    def compute_time(self):
        pass

    @staticmethod
    def is_task(content):
        content = content.strip()
        patterns = [new_pattern, finish_pattern, cancel_pattern]
        for pattern in patterns:
            if re.match(pattern, content) is not None:
                return True
        return False

    @staticmethod
    def get_task(content):
        status = Task.parse_status(content)
        name = Task.parse_name(content)
        task = Task(name, content, status)
        # level
        levels = {low_pattern: TaskLevel.low, high_pattern: TaskLevel.high,
                  critical_pattern: TaskLevel.critical}
        for pattern in levels:
            if pattern in content:
                task.level = levels[pattern]
        # tags
        sub_contents = content.split("@")
        for sub_content in sub_contents:
            sub_content = "@" + sub_content
            if not task.remark:
                task.remark = Task.parse_tag(sub_content, remark_pattern)
            if not task.started_time:
                task.started_time = Task.parse_tag(sub_content, started_pattern)
            if not task.finished_time:
                task.finished_time = Task.parse_tag(sub_content, done_pattern)
            if not task.schedule_time:
                task.schedule_time = Task.parse_tag(sub_content, schedule_pattern)
        return task
    
    def is_delay(self):
        if self.schedule_time is None or self.status not in [TaskStatus.new, TaskStatus.start]:
            return False
        return Task.parse_date(self.schedule_time) <= datetime.now().date()
    
    @property
    def delay_time(self):
        if not self.is_delay():
            return None
        current_time = datetime.now()
        schedule_time = datetime.combine(Task.parse_date(self.schedule_time),time())
        return (current_time-schedule_time).days
        
        
    @staticmethod
    def parse_status(content):
        content = content.strip()
        status = TaskStatus.new
        status_patterns = {new_pattern: TaskStatus.new, finish_pattern: TaskStatus.finish,
                           cancel_pattern: TaskStatus.cancel}
        for pattern in status_patterns:
            if re.match(pattern, content) is not None:
                status = status_patterns[pattern]
        if status == TaskStatus.new and re.match(started_pattern, content) is not None:
            status = TaskStatus.start
        return status

    @staticmethod
    def parse_name(content):
        content = content[1:].strip()
        end = content.find("@")
        if end == -1:
            return content
        else:
            return content[0:end].strip()

    @staticmethod
    def parse_tag(content, pattern):
        result = re.match(pattern, content)
        if result is not None:
            return result.groups()[0].strip()
        else:
            return None

    def __str__(self):
        return self.text
    
    @staticmethod
    def parse_date(content):
        time = f'{20}{content}'
        return datetime.strptime(time, "%Y-%m-%d %H:%M").date()
        


if __name__ == "__main__":
    assert Task.is_task("✔ 代码文档补充 @done(21-02-02 10:12)")
    assert Task.parse_status("✔ 代码文档补充 @done(21-02-02 10:12)") == TaskStatus.finish
    assert Task.parse_name("✔ 代码文档补充 @done(21-02-02 10:12)") == "代码文档补充"
    assert Task.parse_tag("✔ 代码文档补充 @done(21-02-02 10:12)", done_pattern) == "21-02-02 10:12"
    task = Task.get_task(
        "拥塞控制 @started(21-01-21 14:31)  @schedule(21-08-01 19:39) @lasted(1w4d5h8m56s) @critical @remark(很重要)")
    assert task.level == TaskLevel.critical
    assert task.remark == "很重要"
    assert Task.parse_date(task.started_time) == date.fromisoformat('2021-01-21')
    assert Task.parse_date(task.started_time) >= date.fromisoformat('2021-01-12')
    assert task.is_delay()
    assert task.delay_time == 10
