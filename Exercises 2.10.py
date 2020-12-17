# Exercise 2.1

pi = 3.1415926535897932
r = 5
print(4/3*pi*r**3)

# Exercise 2.2

shipping = 3 + 0.75 * 59
book = 24.95
discount = 24.95 * 0.40
total_cost = (book-discount)*60 + shipping
print(total_cost)

# Exercise 2.3

start = (6*60+52)*60
easy = (8*60+15)*2
tempo = (7*60+12)*3
finish_hour = (start+easy+tempo)/(60*60.0)
finish_floored = (start+easy+tempo)//(60*60)
finish_minute = (finish_hour - finish_floored)*60
print ('Finish time was %d:%d' % (finish_hour, finish_minute))
