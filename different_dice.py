import pygal
from die import Die

# Create a D6 and a D10
die1 = Die()
die2 = Die(10)

# Make some rolls, and store results in a list
results = []
for roll_num in range(50000):
    result = die1.roll() + die2.roll()
    results.append(result)

# Analyze the results
frequencies = []
max_result = die1.num_sides + die2.num_sides
for value in range(2, max_result + 1):
    frequency = results.count(value)
    frequencies.append(frequency)

# Visualize the results
hist = pygal.Bar()

hist.title = "Results of rolling one D6 and one D10 die 50000 times"
hist.x_lables = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16']
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D6 + D10', frequencies)
hist.render_to_file('dice_visual2.svg')
