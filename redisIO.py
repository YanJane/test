import redis

'''
Fuctions:
data_write write data into redis database
data_read  read data from redis database

'''

class Database:
        def __init__(self):
                self.host = 'localhost'
                self.port = 6379

        def data_write(self, key, value):
                r = redis.StrictRedis(host = self.host, port = self.port, decode_responses = True)
                r.set(key, value)

        def data_read(self, key):
                r = redis.StrictRedis(host = self.host, port = self.port, decode_responses = True)
                return(r.get(key))

if __name__ == '__main__':
        db = Database()
        db.data_write('key1','value1')
        print(db.data_read('key1'))
