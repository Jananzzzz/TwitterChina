from datetime import date, datetime, timedelta

today = datetime.now()
yesterday = today - timedelta(days=12)

print(str(today))
print(str(yesterday))