# Create jobs

from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler() # APScheduler()
def job_0():
    for e in range(3):
        print("task: ", e)
    print("-----end-----")

def job_1():
    print("updated")

def start_job():
    # run job once a day at 3:20 AM
    scheduler.add_job(id = "Task 1", func=job_0, trigger='cron', hour=3, minute=20, second=0)
    # run job every 30 seconds
    scheduler.add_job(id = "Task 1", func=job_1, trigger = 'interval', seconds = 30)

    scheduler.start()