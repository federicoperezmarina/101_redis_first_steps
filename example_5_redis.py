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

@timer_func
def ReadFunction(numIterations):
   for x in range(numIterations):
      r.get(str(numIterations))   

@timer_func
def DeleteFunction(numIterations):
   for x in range(numIterations):
      r.delete(str(numIterations))   

if __name__ == '__main__':

   r = redis.Redis(host='localhost', port=6379, db=0)

   WriteFunction(100)
   ReadFunction(100)
   DeleteFunction(100)

   WriteFunction(1000)
   ReadFunction(1000)
   DeleteFunction(1000)

   WriteFunction(10000)
   ReadFunction(10000)
   DeleteFunction(10000)

   WriteFunction(100000)
   ReadFunction(100000)
   DeleteFunction(100000)
