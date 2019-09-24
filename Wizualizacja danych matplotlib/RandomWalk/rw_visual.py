import matplotlib.pyplot as plt

from random_walk import RandomWalk

#Tworzenie nowego błądzenia losowego, dopóki program pozostaje aktywny.
while True:

    #Przygotowanie danych błądzenia losowego i wyświetlenie punktów
    rw = RandomWalk(50000)
    rw.fill_walk()

    #Określenie wielkości okna wykresu.
    plt.figure(dpi=128, figsize=(10, 6))

    point_numbers = list(range(rw.num_points))
    plt.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues, edgecolor='none', s=1)
    #plt.plot(rw.x_values, rw.y_values)
    #Podkreślenie pierwszego i ostatniego punktu bładzenia loswego.
    plt.scatter(0, 0, c='green', edgecolors='none', s=100)
    plt.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors='none', s=100)

    plt.show()

    keep_running = input(("Utworzyć nowe błądzenie losowe? (t/n): "))
    if keep_running.lower() == 'n':
        break