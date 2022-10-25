#2. Carregue a data atual do computador e apresente somente a data
import datetime

date = datetime.datetime.now()
print(date.day, '/', date.month, '/' , date.year)
print(f"Hoje é {date.day}/{date.month}/{date.year}")