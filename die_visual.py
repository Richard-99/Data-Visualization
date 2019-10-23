import pygal
from die import Die

# Creating a D6 die
die = Die()

# Make some rolls and store the values
results = []
for value in range(1000):
    result = die.roll()
    results.append(result)

# Analyze the results
frequencies = []
for value in range(1, die.num_sides + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling a D6 die 1000 times"
hist.x_label = ['1', '2', '3', '4', '5', '6']
hist.x_title = "Result"
hist.y_title = "Frequency of results"

hist.add('D6', frequencies)
hist.render_to_file('die_visual.svg')
