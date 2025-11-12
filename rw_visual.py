import matplotlib.pyplot as plt

from random_walk import RandomWalk

# Новые блуждания строятся до тех пор, пока программа остаётся активной.

while True:
    # Построение случайного блуждания
    rw = RandomWalk()
    rw.fill_walk()

    # Нанесение точек на диаграмму
    plt.style.use('classic')
    fig, ax = plt.subplots()
    points_numbers = range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=points_numbers, cmap=plt.cm.Blues, edgecolors='none', s=15)
    plt.show()

    keep_running = input("Make another walk? (y/n): ")
    if keep_running == 'n':
        break