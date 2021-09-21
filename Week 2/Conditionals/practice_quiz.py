# Complete the script by filling in the missing parts. The function receives a
# name, then returns a greeting based on whether or not that name is
# "Taylor".

def greeting(name):
    if name == "Taylor":
        return "Welcome back Taylor!"
    else:
        return "Hello there, " + name


print(greeting("Taylor"))
print(greeting("John"))


# If a filesystem has a block size of 4096 bytes, this means that a file comprised
# of only one byte will still use 4096 bytes of storage. A file made up of 4097
# bytes will use 4096 * 2 = 8192 of storage. Knowing this, can you fill in the
# gaps in the calculate_storage function below, which calculates the total
# number of bytes needed to store a file of a given size?
def calculate_storage(filesize):
    block_size = 4096
    # Use floor division to calculate how many blocks can occupied
    full_blocks = filesize // block_size
    # Use the modulo operator to check whether there's any remainder
    partial_block_remainder = filesize % block_size
    if partial_block_remainder > 0:
        return (full_blocks + 1) * block_size
    return block_size


print(calculate_storage(1))  # Should be 4096
print(calculate_storage(4096))  # Should be 4096
print(calculate_storage(4097))  # Should be 8192
print(calculate_storage(6000))  # Should be 8192


def num(number):
    if number > 11:
        print(0)
    elif number != 10:
        print(1)
    elif number >= 20 or number < 12:
        print(2)
    else:
        print(3)


num(10)
