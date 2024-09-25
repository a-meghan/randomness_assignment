#Task 1- Your mood today

import random
my_moods = ["Happy", "Sad", "Angry", "Goofy", "Shocked", "Guilty", "Sentimental", "Excited"]
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for i in days_of_the_week:
    mood = random.choice(my_moods)
    print("I felt", mood.lower(), "on", i)