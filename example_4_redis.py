import redis


def do_some_query():
    # Replace with actual querying code to a database,
    # a remote REST API, etc.
    return 42


# Don't forget to run `memcached' before running this code
r = redis.Redis(host='localhost', port=6379, db=0)
result = r.get('some_key')

if result is None:
    # The cache is empty, need to get the value
    # from the canonical source:
    result = do_some_query()

    # Cache the result for next time:
    r.set('some_key', result)

# Whether we needed to update the cache or not,
# at this point you can work with the data
# stored in the `result` variable:
print(result)