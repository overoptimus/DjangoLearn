from celery import task
import time

@task
def task1():
    print('celery test!')
    time.sleep(5)
    print('success')
    return True
