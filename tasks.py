from apscheduler.schedulers.background import BackgroundScheduler

scheduler = BackgroundScheduler() # APScheduler()
def job_0():
    for e in range(3):
        print("task: ", e)
    print("-----end-----")

def job_1():
    print("updated")

def start_job():
    scheduler.add_job(id = "Task 1", func=job_0, trigger='cron', hour=3, minute=20, second=0)
    # scheduler.add_job(id = "Task 1", func=job_1, trigger = 'interval', seconds = 30)
    # scheduler.add_job(id = "Scheduled task", func=job_0, trigger = 'interval', seconds = 5)
    scheduler.start()