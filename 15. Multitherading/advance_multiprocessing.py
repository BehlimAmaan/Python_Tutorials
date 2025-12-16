from concurrent.futures import ThreadPoolExecutor
import time 

def square(numbers):
        time.sleep(2)
        return f"Square: {numbers * numbers}"

number = [1,4,7,2,7,3,8,47,93,35,67,4,6,3,5,3,6,5,2,4,5,6,7,8,6,3,2,6,7,9,0]

if __name__ =="__main__":
    with ThreadPoolExecutor(max_workers=4) as executor:
        results = executor.map(square,number)
        
for result in results:
    print(result)