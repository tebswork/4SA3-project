################################################################################
# Python Redis Labs database demo code.
#
# Purpose: Demonstrating a Redis Labs database in Python.  We sign-up for an
# account at Redis Labs to setup a database and get credentials:
#   https://redislabs.com/
# And then we can install the redis Python module with this command:
#   pip3 install redis
# We can the use the package to access the database as outlined in this
# document: https://redislabs.com/lp/python-redis/.  Full documentation of
# the module is available here: https://redis-py.readthedocs.io/en/stable/
# See full list of redis commands: https://redis.io/commands
#
# Author: Kevin Browne
# Contact: brownek@mcmaster.ca
#
################################################################################
import redis

# Use the host, port and password credentials to connect to the database.
# We put decade_responses=True so that redis doesn't return byte strings (a
# default behaviour otherwise)
r = redis.Redis(
    host= 'redis-10460.crce174.ca-central-1-1.ec2.redns.redis-cloud.com:10460',
    port=6379,
    password='hT9E4QyQ0yUzj26YP10dktpQjlmflFjq',
    decode_responses=True)

# we can set and get values using aa key
r.set('some_key', 'some_value')
value = r.get('some_key')
print(value)

# the value can be different kinds of primitive values
r.set('some_other_key', 5)
other_value = r.get('some_other_key')
print(other_value)

# redis supports hash values... field/value pairs at a given key... so in the
# below example, the value of hash_key is a set of field/value pairs (we use
# the word field instead of key for hashes).  This can be useful for storing
# "tables of data", we can use a schema in redis like this...
#
# customer1 = { "name" : "Kevin", "email": "brownek@mcmaster.ca"}
# customer2 = { "name" : "Devon", "email": "devon@mcmaster.ca"}
#
# where customer1, customer2, ... , customeri are the keys to hashes of data
# with particular fields like name, email, etc.

# Set hash fields and associated values at the key hash_key
r.hset("hash_key", "hashfield1", "hasvalue1")
r.hset("hash_key", "hashfield2", 2)
r.hset("hash_key", "hashfield3", "hashavlue3")

# get all of the keys/fields at hash_key
hash_result = r.hgetall("hash_key")
print(hash_result)

# get a specific value using both the hash key and field
hash_val = r.hget("hash_key","hashkey3")
print(hash_val)

