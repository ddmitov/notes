#!/usr/bin/env python3

from hashlib import blake2b
import time

hash_key          = str(time.time()).encode('utf-8')
hash_final        = blake2b(key=hash_key, digest_size=64)
hash_final_string = str(hash_final.hexdigest())
