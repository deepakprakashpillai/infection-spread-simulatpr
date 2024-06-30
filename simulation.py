
import random

class Simulation:
    def __init__(self, population_size, initial_infection_rate, recovery_rate, simulation_days):
        self.population_size = population_size
        self.initial_infection_rate = initial_infection_rate
        self.recovery_rate = recovery_rate
        self.simulation_days = simulation_days

class Person:
    infection_probability = 0.1  # Class variable for infection probability

    def __init__(self, is_infected=False, is_recovered=False):
        self.is_infected = is_infected
        self.is_recovered = is_recovered

    def interact(self, other):
        if self.is_infected and not other.is_infected and not other.is_recovered:
            if random.random() < Person.infection_probability:
                other.is_infected = True

class Population:
    def __init__(self, size, initial_infection_rate, recovery_rate):
        self.size = size
        self.recovery_rate = recovery_rate
        self.people = [Person(is_infected=(random.random() < initial_infection_rate)) for _ in range(size)]

    def daily_update(self):
        for person in self.people:
            if person.is_infected and not person.is_recovered:
                if random.random() < self.recovery_rate:
                    person.is_infected = False
                    person.is_recovered = True

        for person in self.people:
            if not person.is_infected and not person.is_recovered:
                other = random.choice([p for p in self.people if p != person])
                person.interact(other)

    def __add__(self, other):
        combined_size = self.size + other.size
        combined_people = self.people + other.people
        new_population = Population(0, 0, 0)  # Temporary values, we'll overwrite them
        new_population.size = combined_size
        new_population.people = combined_people
        return new_population



