from POSTGRES.repository.connections import TaskRepo
from POSTGRES.repository.cache import CacheTask
from POSTGRES.repository.connections import Task_FA

from dataclasses import dataclass

@dataclass
class TaskService:
    
    task_repository: TaskRepo
    task_cache: CacheTask

    def get_service_task(self):
        if tasks := self.task_cache.get_task():
            return tasks
        else:
            tasks = self.task_repository.get_tiker() 
            task_sch = [Task_FA.model_validate(task) for task in tasks]
            self.task_cache.set_tasks(task_sch)
            return  tasks
        

# Task_Service = TaskService()