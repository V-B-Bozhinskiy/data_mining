from plotly.graph_objs import Bar, Layout
from plotly import offline

from die import Die

#Создание кубика Д6
die_1 = Die() #D6 по умолчанию
die_2 = Die(10) #D10

# Моделирование серии бросков с сохранением результата в списке.
results = []
for roll_num in range(100):
    result = die_1.roll() + die_2.roll()
    results.append(result)

print(results)

# Анализ результатов.
frequencies = []
max_result = die_1.num_sides + die_2.num_sides
for value in range(2, max_result+1):
    frequency = results.count(value)
    frequencies.append(frequency)

print(frequencies)

# Визуализация результатов
x_values = list(range(2,max_result+1))
data = [Bar(x=x_values, y=frequencies)]

x_axis_config = {'title': 'Result', 'dtick': 1}
y_axis_config = {'title': 'Frequency of Result'}

my_layout = Layout(title='Result of rollnig D6 and D10 100 times', xaxis=x_axis_config, yaxis=y_axis_config)
offline.plot({'data': data, 'layout': my_layout}, filename='d6_d10.html')