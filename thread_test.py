import threading
from queue import Queue
import time


print_lock=threading.Lock()


def exampleJob(worker):
    time.sleep(.5) # pretend to do some work.
    with print_lock:
        print(threading.current_thread().name,worker)

def threader():
    while True:
        # gets an worker from the queue
        worker = q.get()

        # Run the example job with the avail worker in queue (thread)
        exampleJob(worker)

        # completed with the job
        q.task_done()




q=Queue()

for x in range(10):

    t = threading.Thread(target=threader)

    t.daemon = True

    t.start()

start = time.time()

for worker in range(20):
    q.put(worker)


q.join()

print('Entire job took:',time.time() - start)
