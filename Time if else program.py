import time
clock = time.strftime('%H:%M:%S')
print(clock)

t = int(time.strftime('%H'))
if(t>=6 and t<12):
    print('Good morning Dark Lord.')
elif(t>=12 and t<17):
    print('Good afternoon Dark Lord.')
elif(t<=17 and t<20):
    print('Good evening Dark Lord.')
else:
    print('Good night Dark Lord.')

# https://docs.python.org/3/library/time.html#time.strftime