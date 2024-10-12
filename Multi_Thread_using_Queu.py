import threading, time, random
from queue import Queue

jobs = Queue()

# tạo một hàm lấy dữ liệu ra từ queue
def do_stuff(q):
    while not q.empty():
        value = q.get()
        time.sleep(random.randint(1, 10))
        print(value)
        q.task_done()
# gửi các dữ liệu cần chạy vào queue
for i in range(10):
    jobs.put(i)

for i in range(3):
#   tạo 3 thread cùng xử lí dữ liệu trong queue , vì queue là một safe thread nên nó sẽ không xung đột dữ liệu
    worker = threading.Thread(target=do_stuff, args=(jobs,))
    worker.start()

print("waiting for queue to complete", jobs.qsize(), "tasks")
jobs.join()
print("all done")
