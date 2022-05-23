# 101_redis_first_steps
This is a repository to learn about redis. The programming language used will be python.

## Table of Contents
* [Create and run redis image](#create-and-run-redis-image)
* [Redis examples](#redis-examples)


## Create and run redis image
First of all we have to build the Dockerfile with then next command:
```sh
docker build -t redis .
```

Now we have created the docker image alpine-linux with redis and python. Run the command to run the container.
```sh
docker run --name my-redis -d redis
```

In this step we are going inside the container to start using redis.
```sh
docker exec -it my-redis /bin/ash
```

## Redis examples
In this step we are able to start using redis. It is very easy to use, redis is a cache service. We are going to do show some examples in order to know how it work and how it performs.

### Example 1
The first example explains how to set & read a cache
```sh
cd /tmp
python3 example_1_redis.py

output:
b'value'
```

### Example 2
The second example explains how to set the cache & measure the time that it takes
```sh
cd /tmp
python3 example_2_redis.py

output:
WriteFunction took 0.038167715072631836 seconds to complete its execution.
WriteFunction took 0.30928897857666016 seconds to complete its execution.
WriteFunction took 3.458836793899536 seconds to complete its execution.
WriteFunction took 34.42079019546509 seconds to complete its execution.
```

### Example 3
The third example explains how to set & read the cache & measure the time that it takes
```sh
cd /tmp
python3 example_3_redis.py

output:
WriteFunction took 0.035843849182128906 seconds to complete its execution.
ReadFunction took 0.033121347427368164 seconds to complete its execution.
WriteFunction took 0.33890390396118164 seconds to complete its execution.
ReadFunction took 0.3285794258117676 seconds to complete its execution.
WriteFunction took 3.4524381160736084 seconds to complete its execution.
ReadFunction took 3.4135544300079346 seconds to complete its execution.
WriteFunction took 34.63904881477356 seconds to complete its execution.
ReadFunction took 33.290050745010376 seconds to complete its execution.
```

### Example 4
The fourth example explains how to create a cache strategy
```sh
cd /tmp
python3 example_4_redis.py

output:
42
```

### Example 5
The fifth example explains how to set / read and delete the cache & measure the time that it takes
```sh
cd /tmp
python3 example_5_redis.py

output:
WriteFunction took 0.03921318054199219 seconds to complete its execution.
ReadFunction took 0.034618377685546875 seconds to complete its execution.
DeleteFunction took 0.03240370750427246 seconds to complete its execution.
WriteFunction took 0.3082084655761719 seconds to complete its execution.
ReadFunction took 0.3028452396392822 seconds to complete its execution.
DeleteFunction took 0.3495149612426758 seconds to complete its execution.
WriteFunction took 3.429778575897217 seconds to complete its execution.
ReadFunction took 3.3526546955108643 seconds to complete its execution.
DeleteFunction took 3.4181325435638428 seconds to complete its execution.
WriteFunction took 35.393630504608154 seconds to complete its execution.
ReadFunction took 34.688477993011475 seconds to complete its execution.
DeleteFunction took 34.887418270111084 seconds to complete its execution.
```