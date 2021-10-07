from Time import Time

t1 = Time( 21 , 45 , 22 ) #9:45:22 pm
t2 = Time( 5, 23 , 17) #5:23:17 am
t3 = Time( 13 , 23, 55) #1:23:55 pm
t4 = Time(7 , 52 , 23) #7:52:23 am
t5 = Time(18,43,23) #6:43:23 pm

print(t1.toString())
print("hours =", t1.getHours())
print("minutes =",t1.getMinutes())
print("seconds =",t1.getSeconds())

print("time in seconds =", t1.timeInSeconds())

t1.changeTheTime(2,12,56)
print(t1.toString())

print(t3.twelveHourClock())
print(t2.twelveHourClock())

print(t5.whatTimeIsIt()) #evening
print(t3.whatTimeIsIt()) #afternoon
print(t2.whatTimeIsIt()) #nighttime
print(t4.whatTimeIsIt()) #morning

x = t1.compareTo(t2)
print(x)
y = t2.compareTo(t1)
print(y)