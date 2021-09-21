import time

def ntime(array, answer):
    length = len(array)
    for x in range(length):
        if array[x] == answer:
            return True
    return False

array = (range(300))
if ntime(array, 234) == True:
    tiempo = time.process_time()

print(tiempo)