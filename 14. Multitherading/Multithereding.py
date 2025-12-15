import multiprocessing 
import time

def square():
    for i in range(5):
        time.sleep(1)
        print(f"Square : {i*i}")

def cube():
    for i in range(5):
        time.sleep(1)
        print(f"Cube: {i*i*i}") 

if __name__=="__main__":
        
    m1=multiprocessing.Process(target=square)
    m2=multiprocessing.Process(target=cube)

    t=time.time()

    m1.start()
    m2.start()
    
    m1.join()
    m2.join()

    finished_time=time.time()-t
    print(finished_time)