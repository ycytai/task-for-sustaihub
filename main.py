import time

from apscheduler.schedulers.background import BackgroundScheduler
from loguru import logger

from tasks import get_stock_price_task

scheduler = BackgroundScheduler()
# NOTE: This is a simple example of how to use the scheduler.
# cron_task = {
#     'Stock': {
#         'Collect price': {
#             'func': get_stock_price_task,
#             'hour': 15,
#             'minute': 3,
#         },
#     }
# }

# for category, tasks in cron_task.items():
#     for task, config in tasks.items():
#         scheduler.add_job(
#             config['func'],
#             'cron',
#             hour=config['hour'],
#             minute=config['minute'],
#             id=f'{category:<10} - {task}',
#         )

# NOTE: For demo purpose, we will use a simple interval trigger.
scheduler.add_job(get_stock_price_task, 'interval', seconds=20)


scheduler.start()


jobs = scheduler.get_jobs()
count = 0
for job in jobs:
    count += 1
    logger.info(f'No: {count:<5} | {job.id:<30} | {job.trigger}')


logger.info('Scheduler started.')

try:
    while True:
        time.sleep(1)
except (KeyboardInterrupt, SystemExit):
    scheduler.shutdown()
    logger.info('Scheduler shut down successfully.')
