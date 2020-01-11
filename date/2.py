import calendar
from datetime import datetime,timedelta

future = datetime.now() + timedelta(weeks=300)

print(calendar.month(future.year, future.month))