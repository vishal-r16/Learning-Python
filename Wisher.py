import time
thour = int(time.strftime('%H'))
if (11>=thour>=3):
    print("Good Morning")
elif(16>=thour>11):
    print("Good Afternoon")
elif(19>=thour>16):
    print("Good Evening")
else:
    print("Good Night")