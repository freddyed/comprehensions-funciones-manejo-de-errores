import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('TkAgg')  # o 'Qt5Agg' si prefieres usar Qt5

def generate_bar_chart():
    labels = ['a', 'b', 'c']
    values = [100, 200, 300]

    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.show()

if __name__ == '__main__':
    generate_bar_chart()
