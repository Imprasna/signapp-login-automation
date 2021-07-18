from apscheduler.schedulers.blocking import BlockingScheduler
from runthis import login_automate

sched = BlockingScheduler()

# Schedule job_function to be called every two hours
sched.add_job(login_automate, 'interval', seconds=5)

sched.start()