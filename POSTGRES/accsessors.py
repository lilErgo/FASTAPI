from POSTGRES.config import settings
import redis

def create_connection() -> redis.Redis:
    instance = redis.Redis(
                                host=settings.REDIS_HOST,
                                port=settings.REDIS_PORT,
                                password=settings.REDIS_PASSWORD,
                                db=0,
                                decode_responses=False
    )
    return instance

# def create_task():
#     instance = create_connection()
#     # instance.set(name='rappers:XXXTENTACION',value='Artist XXXTENTACION, have album 17, bad vibes forever, ?, Revenge')
#     instance.lpush('myList','rappers:JuiceWrld')
    
    
   
# create_task()