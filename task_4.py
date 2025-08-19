new_tasks = ['task_001', 'task_011', 'task_007', 'task_015', 'task_005']
completed_tasks = ['task_002', 'task_012', 'task_006']

# Переношу task_005 из new_tasks в completed_tasks 
completed_tasks.append(new_tasks.pop(new_tasks.index('task_005')))

# Удаляю task_007 из списка new_tasks
new_tasks.remove('task_007')

print(new_tasks[-1])