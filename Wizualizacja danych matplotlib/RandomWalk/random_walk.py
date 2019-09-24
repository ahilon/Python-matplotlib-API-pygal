from random import choice

class RandomWalk():
    """Klasa przeznaczona do wygenerowania bładzenia losowego."""

    def __init__(self, num_points=5000):
        """Inicjalizacja atrybutów błądzenia"""
        self.num_points = num_points

        #punkt początkowy ma współrzędne (0,0).
        self.x_values = [0]
        self.y_values = [0]

    def fill_walk(self):
        """Wygenerowanei wszystkich punktów dla bładzenia loswego."""

        #Wykonywanie kroków aż do chwili osiągnięcia oczekiwanej liczby kierunku.
        while len(self.x_values) < self.num_points:
            x_direction = choice([1, -1])
            x_distance = choice(list(range(1,9)))
            x_step = x_direction * x_distance

            y_direction = choice([1, -1])
            y_distance = choice(list(range(1,9)))
            y_step = y_direction * y_distance

            #Odrzucenie kroków które prowadzą donikąd
            if x_step == 0 and y_step == 0:
                continue

            #ustalanie następnych wartości X i Y:
            next_x = self.x_values[-1] + x_step
            next_y = self.y_values[-1] + y_step

            self.x_values.append(next_x)
            self.y_values.append(next_y)
