# The bytes() method returns an immutable bytes object initialized with the given size and data.

message = 'Learning python is fun'

# convert string to bytes
byte_message = bytes(message, 'utf-8')
print(byte_message)

# Output: b'Learning python is fun'
