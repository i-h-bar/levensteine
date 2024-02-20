from time import perf_counter

from levensteine import cydist
from pylevesteine import pydist
from cpplev import cppdist
from mimesis import Text


funcs = [pydist, cydist, cppdist]
samples = 1000
rand = Text()
words1 = [" ".join(rand.words(5)) for _ in range(samples)]
words2 = [" ".join(rand.words(5)) for _ in range(samples)]

for func in funcs:
    averages = []
    for i in range(samples):
        word1, word2 = words1[i], words2[i]
        t1 = perf_counter()
        func(word1, word2)
        averages.append(perf_counter() - t1)

    print(f"{func.__name__}: {(sum(averages) / samples) * 1000000:.5f}µs")
