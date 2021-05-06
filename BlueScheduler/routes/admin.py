import math
import BlueScheduler.settings as settings
from datetime import datetime,date,timedelta
from flask import request, Blueprint, Markup, render_template
from BlueScheduler.util.resolver import *
from BlueScheduler.util.markdown import *

admin_bp = Blueprint('admin', __name__)


@admin_bp.route("/plan/list", methods=['GET'])
def list_plan():
    status = int(request.args.get('status', default=15))
    plan_resolver = Resolver()
    plan_projects = plan_resolver.resolve(settings.SOURCE_PATH)
    markdown_content = "#我的TODO#\n"
    for plan_project_name in plan_projects:
        flag = False
        plan_project = plan_projects[plan_project_name]
        for plan_task in plan_project.get_tasks():
            if int(math.pow(2, int(plan_task.status.value))) & status:
                if not flag:
                    markdown_content += "##{}\n".format(plan_project.name)
                    flag = True
                markdown_content += "* {}\n".format(str(plan_task))
        if flag:
            markdown_content += "\r\n"
    html_body = convert_markdown_html(markdown_content)
    content = Markup(html_body)
    return render_template('index.html', **locals())

@admin_bp.route("/todo/list", methods=['GET'])
def list_todo():
    plan_resolver = Resolver()
    plan_projects = plan_resolver.resolve(settings.SOURCE_PATH)
    markdown_content = "#我的TODO#\n"
    for plan_project_name in plan_projects:
        flag = False
        plan_project = plan_projects[plan_project_name]
        for plan_task in plan_project.get_tasks():
            if plan_task.status == TaskStatus.new or plan_task.status == TaskStatus.start:
                if not flag:
                    markdown_content += "##{}\n".format(plan_project.name)
                    flag = True
                markdown_content += "* {}\n".format(str(plan_task))
        if flag:
            markdown_content += "\r\n"
    html_body = convert_markdown_html(markdown_content)
    content = Markup(html_body)
    return render_template('index.html', **locals())


@admin_bp.route("/work/list/<int:days>",methods=['GET'])
def list_week_report(days):
    plan_resolver = Resolver()
    plan_projects = plan_resolver.resolve(settings.SOURCE_PATH)
    markdown_content = "#过去一段时间达成的工作#\n"
    for plan_project_name in plan_projects:
        flag = False
        plan_project = plan_projects[plan_project_name]
        for plan_task in plan_project.get_completed_tasks(date.fromtimestamp(time.time())-timedelta(days=days),date.fromtimestamp(time.time())):
            if not flag:
                markdown_content += "##{}\n".format(plan_project.name)
                flag = True
            markdown_content += "* {}\n".format(str(plan_task))
        if flag:
            markdown_content += "\r\n"
    html_body = convert_markdown_html(markdown_content)
    content = Markup(html_body)
    return render_template('index.html', **locals())