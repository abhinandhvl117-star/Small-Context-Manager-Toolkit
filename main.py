import time
from contextlib import contextmanager

# class Timer:
 
#     def __enter__(self):
#         self.start = time.time()
    
#     def __exit__(self, exc_type, exc, tb):
#         self.end = time.time()
#         print(round(self.end - self.start, 2)) 
        
# try:
#     with Timer():
#         time.sleep(1)
#         raise ValueError("Something went wrong")
# except ValueError:
#     print("Exception caught")

# @contextmanager
# def timer():
#     try:
#         start = time.time()
#         yield
#     finally:
#         end = time.time()
#         print(round(end - start, 2))
        
# try:
#     with timer():
#         time.sleep(1)
#         raise ValueError("Oops")
# except ValueError:
#     print("Caught")
    
    
