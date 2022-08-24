import time

from celery import shared_task


@shared_task
def test_celery():
    t = time.time()
    time.sleep(3)
    print('GGGGGGGGGGGGGGGGGGGGGGGGGGGGGg')
    print(time.time() - t)


