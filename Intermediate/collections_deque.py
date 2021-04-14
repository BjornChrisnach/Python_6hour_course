# collections deque 8
import collections
from collections import deque

d = deque("hello", maxlen=5)
d.extend([1, 2, 3])
# d.pop()
# d.popleft()

# d.clear()

# d.extend("456")
# d.extend([1, 2, 3])
# d.extendleft("hey")

# d.rotate(-2)
print(d)
