import matplotlib.pyplot as plt

def generate_bar_chart(name, labels, values):
    #labels = ["a", "b", "c"]
    #values = [100, 200, 80]
    fig, ax = plt.subplots()
    ax.bar(labels, values)
    plt.savefig(f'./imgs/{name}.png')
    plt.close()

def generate_pie_chart(labels, values):
    fig, ax = plt.subplots()
    ax.pie(values, labels = labels)
    ax.axis("equal")
    plt.savefig('pie.png')
    plt.close()


if __name__ == "__main__":
    labels = ["a", "b", "c"]
    values = [10, 40, 800]
    #generate_bar_chart(labels, values)
    generate_pie_chart(labels, values)

"""
Pyplot de Matplotlib
La mayoría de las utilidades de Matplotlib se encuentran en el pyplotsubmódulo y, por lo general, se importan con el plt alias:
import matplotlib.pyplot as plt

Ahora se puede hacer referencia al paquete Pyplot como plt.
Aprenderá más sobre dibujar (trazar) en los próximos capítulos.
"""