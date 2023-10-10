from random import randint

class Individual:
    def __init__(self, gnome="", fitness=0):
        self.gnome = gnome
        self.fitness = fitness

class TravelingSalesmanProblem:
    def __init__(self, cities=7):
        self.cities = cities
        self.genes = "ABCDEFG"
        self.max_distance = 1000000000000000000000000
        self.bestfit_found = self.max_distance
        self.best_route = ""

    def rand_num(self, initial, end):
        return randint(initial, end - 1)

    def create_gnome(self):
        gnome = "0"
        while len(gnome) < self.cities:
            temp = self.rand_num(1, self.cities)
            if str(temp) not in gnome:
                gnome += str(temp)
        return gnome + gnome[0]

    def create_map(self):
        return [
            [0, 12, 10, self.max_distance, self.max_distance, self.max_distance, 12],
            [12, 0, 8, 12, self.max_distance, self.max_distance, self.max_distance],
            [10, 8, 0, 11, 3, self.max_distance, 9],
            [self.max_distance, 12, 11, 0, 11, 10, self.max_distance],
            [self.max_distance, self.max_distance, 3, 11, 0, 6, 7],
            [self.max_distance, self.max_distance, self.max_distance, 10, 6, 0, 9],
            [12, self.max_distance, 9, self.max_distance, 7, 9, 0]
        ]

    def cal_fitness(self, gnome, mp):
        f = 0
        for i in range(len(gnome) - 1):
            if mp[int(gnome[i])][int(gnome[i + 1])] == self.max_distance:
                return self.max_distance
            f += mp[int(gnome[i])][int(gnome[i + 1])]
        return f

    def mutated_gene(self, gnome):
        gnome = list(gnome)
        while True:
            r, r1 = self.rand_num(1, self.cities), self.rand_num(1, self.cities)
            if r1 != r:
                gnome[r], gnome[r1] = gnome[r1], gnome[r]
                break
        return ''.join(gnome)

    def genetic_algorithm(self):
        mp = self.create_map()
        population_size = 1000
        generation_threshold = 5
        temperature = 10000

        population = [Individual(self.create_gnome(), 0) for _ in range(population_size)]

        for ind in population:
            ind.fitness = self.cal_fitness(ind.gnome, mp)

        for gen in range(1, generation_threshold + 1):
            population.sort(key=lambda x: x.fitness)

            new_population = []
            for ind in population:
                p1 = ind
                while True:
                    new_g = self.mutated_gene(p1.gnome)
                    new_ind = Individual(new_g, self.cal_fitness(new_g, mp))

                    if new_ind.fitness <= p1.fitness:
                        new_population.append(new_ind)
                        break
                    else:
                        prob = pow(2.7, -1 * (float(new_ind.fitness - p1.fitness) / temperature))
                        if prob > 0.5:
                            new_population.append(new_ind)
                            break

            temperature = (90 * temperature) / 100
            population = new_population

            print("Generation", gen)
            print("Route\t\t\tFitness Value")
            for ind in population:
                print(ind.gnome, ind.fitness)
                if ind.fitness < self.bestfit_found:
                    self.bestfit_found = ind.fitness
                    self.best_route = ind.gnome


tsp = TravelingSalesmanProblem()
tsp.genetic_algorithm()

input_str = tsp.best_route
digit_to_letter = {str(i): tsp.genes[i] for i in range(tsp.cities)}
best_route = []
for digit in input_str:
    letter = digit_to_letter[digit]
    best_route.append(letter)
print("\n")
print("The best route ")
for letter in best_route:
    print(letter, end="")
print("->" + str(tsp.bestfit_found) + "(distance)")
