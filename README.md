# BlueScheduler
A simple todo scheduler for Python

## 基本介绍

BlueScheduler是高效的生产力管理平台，集成了计划管理和计划提醒功能，利用vscode的Todo+(https://github.com/fabiospampinato/vscode-todo-plus) 插件来完成计划的编写，利用内置后台可以回顾任务完成情况及未来计划。

## TODO+插件介绍


* 标识符：用于标识任务的基本状态，包含建立、开始、完成和取消。

```
Box: - ❍ ❑ ■ ⬜ □ ☐ ▪ ▫ – — ≡ → › [] [ ]
Done: ✔ ✓ ☑ + [x] [X] [+]
Cancelled: ✘ x X [-]
```

* 常用标签

```
@started(21-01-21 14:31)     开始时间
@done(21-01-21 16:04)        完成时间
@cancelled(21-01-31 15:03)   取消时间
@remark(备注)                备注
@critical @high @low         优先级设置
@lasted(1w3d2h24m17s)        持续时间
@est(2h30m)                  预估时间

```

## 案例

```

Projects:
  ☐ Anything with a colon at the end of the line is a project
  ☐ Projects will show some statistics next to them @1h
    ✔ By default those statistics are the number of pending todos and the sum of their time estimates @30m
  Nested:
    ☐ You can nest projects inside each other and fold them

Todos:
  You can write plain text notes/descriptions wherever you want
  New:
    ☐ Press Cmd/Ctrl+Enter to add a new todo
  Done:
    ✔ Press Alt+D to mark a todo as done
    ✔ Press it again to undo the action
  Cancelled:
    ✘ Press Alt+C to mark a todo as cancelled
    ✘ Press it again to undo the action
  Tagging:
    ☐ You can add tags using the @ symbol, like this @tag
    ☐ There are some special, customizable tags: @critical @high @low @today
  Timekeeping:
    ✔ Completed todos can show a timestamp @done(17-11-03 10:42)
    ☐ Press Alt+S to mark a todo as started @started(17-11-03 10:42)
      ✔ Now it will show the elapsed time @started(17-11-03 10:42) @done(17-11-03 20:11) @lasted(9h29m)
    ☐ You can provide time estimates for your todos @1h30m
      ☐ We are even doing some natural language processing @est(1 day and 20 minutes)

Formatting:
  You can format text in a markdown-like fashion
  Bold:
    ☐ Use asterisks for *bold*
  Italic:
    ☐ Use underscores for _italic_
  Strikethrough:
    ☐ Use tildes for ~strikethrough~
  Code:
    ☐ Use backticks for `code`

Archive:
  ✔ You can archive finished todos here
  ✔ Congratulations, you are now a Todo+ master!
```

## 快速入门

```
cd BlueScheduler && pip3 install -r requirements.txt; 
cd BlueScheduler && sh start.sh;
http://127.0.0.1:9288/admin/todo/list 待完成的todo
http://127.0.0.1:9288/admin/plan/list 全部todo
```

