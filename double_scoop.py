#Task 2- Your mood tracker

import random
my_moods = ["Happy", "Sad", "Angry", "Goofy", "Shocked", "Guilty", "Sentimental", "Excited", "Exhausted", "Annoyed", "Sick"]
days_of_the_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["morning", "afternoon", "evening"]

for d in days_of_the_week:
    for i in times_of_day:
        mood = random.choice(my_moods)
        print("On", d, i, "I felt", mood.lower())