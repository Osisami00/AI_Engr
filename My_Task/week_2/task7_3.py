# Task3: Day And Activities Pairing
days =("Sunday", "Monday", "Tuesday", "Wednesday","Thursday","Friday")
# collect active days  from users
day1 = input('Enter first day of the week where you perform an activity: ')
day2 = input('Enter second day of the week where you perform an activity: ')
day3 = input('Enter third day of the week where you perform an activity: ')

# collect activity data from users
activity1 =input("Enter activity for day one: ")
activity2 =input("Enter activity for day two: ")
activity3 = input("Enter acyivity for day three :")

# save data in tuple
active_days =(day1,day2,day3)
activities =(activity1, activity2,activity3)
print({day: activity for day, activity in zip(active_days, activities)})