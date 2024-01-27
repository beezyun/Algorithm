# https://www.acmicpc.net/problem/10699
# Bronze 5 오늘 날짜

from datetime import datetime, timedelta

seoul = datetime.now() + timedelta(hours=9)
print(seoul.strftime('%Y-%m-%d'))