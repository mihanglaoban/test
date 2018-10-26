from info import redis_store
from . import index_blue

@index_blue.route('/')
def index():
    redis_store.set("name", "tar")
    return "success!"
