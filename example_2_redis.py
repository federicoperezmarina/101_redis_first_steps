import random
import time
import redis

def timer_func(func):

   def function_timer(*args, **kwargs):
      start = time.time()
      value = func(*args, **kwargs)
      end = time.time()
      runtime = end - start
      msg = "{func} took {time} seconds to complete its execution."
      print(msg.format(func = func.__name__,time = runtime))
      return value
   
   return function_timer

@timer_func
def WriteFunction(numIterations):
   for x in range(numIterations):
      r.set("'"+str(numIterations)+"'", 'value iteration '+str(numIterations))

if __name__ == '__main__':

   r = redis.Redis(host='localhost', port=6379, db=0)

   WriteFunction(100)
   WriteFunction(1000)
   WriteFunction(10000)
   WriteFunction(100000)
