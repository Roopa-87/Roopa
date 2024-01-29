import time
def duration(func):
    def inner():
        start=time.time()
        func()
        end=time.time()
        print(f'the total time taken to answer to answer the question is {end-start} secs')
    return inner
@duration
def question1():
    print('who is the principle of mca in MTCA')
    response=input('enter thev response')
@duration 
def question2():
    print('who is the prime minster of andrapradesh')
    response=input('enter your response')
question1()
question2()   