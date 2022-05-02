import levensteine
import pylevesteine
import time

t1 = time.time()
levensteine.loop_distance("benyam", "ephrem")
print(time.time() - t1)

t1 = time.time()
for _ in range(25_000):
    pylevesteine.distance("benyam", "ephrem")
print(time.time() - t1)
