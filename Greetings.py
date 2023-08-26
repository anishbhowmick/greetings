import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp =int(time.strftime('%H'))
if 5<=timestamp<12:
    print("Good morning 🌼")
elif 12<=timestamp<16:
    print("Good afternoon 🌼")
elif 16<=timestamp<19:
    print("Good evening 🌼")
else:
    print("Good night 🌼")
    