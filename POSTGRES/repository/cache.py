from redis import Redis
from FASTAPI.schema import Task_FA
import json

class CacheTask:
    def __init__(self, redis: Redis):
        self.redis = redis

    def get_task(self)-> list[Task_FA]:
        with self.redis as redis:
            tasks_json = redis.lrange('tasks',0,-1)
            return [Task_FA.model_validate(json.loads(task))for task in tasks_json]

    def set_tasks(self, tasks: list[Task_FA]):
        task_json = [task.json() for task in tasks]
        with self.redis as redis:
            redis.lpush('tasks',*task_json)