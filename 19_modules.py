import sys  
print(sys.path)

import re
text = 'Mi numero de celular es 983333333, el codigo del pais es 51, mi numero de la suerte es 7'

result = re.findall('[0-9]+', text)
print(result)

import time
timestamp = time.time()
local = time.localtime()
result = time.asctime(local)
print(result)

import collections
numbers = [1,1,2,1,1,4,5,3,3,21]
counter = collections.Counter(numbers)
print(counter)