import MoodFinder
mf = MoodFinder.MoodFinder()
mf.setResolution(640,480);
avg = mf.calculateAverageValence()
print("Average is " + str(avg))