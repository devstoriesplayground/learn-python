# A memory view is a safe way to expose the buffer protocol in Python. It allows you to access the internal buffers of an object by creating a memory view object.

#random bytearray
random_byte_array = bytearray('ABC', 'utf-8')

mv = memoryview(random_byte_array)

# access memory view's zeroth index
print(mv[0]) # 65 

# create byte from memory view
print(bytes(mv[0:2])) # b'AB'

# create list from memory view
print(list(mv[0:3])) # [ 65, 66, 67]