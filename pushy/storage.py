from redis import StrictRedis


class MemoryStorage(object):
    def __init__(self):
        self.data = {}

    def get(self, item_id):
        return self.data.get(item_id)

    def set(self, item_id, item_value):
        self.data[item_id] = item_value

    def rm(self, item_id):
        self.data.pop(item_id)


class RedisStorage(object):
    def __init__(self, host, port):
        self.connection = StrictRedis(host=host, port=port)

    def get(self, item_id):
        return self.connection.get(item_id)

    def set(self, item_id, item_value):
        self.connection.rpush(item_id, item_value)

    def rm(self, item_id):
        self.connection.delete(item_id)
