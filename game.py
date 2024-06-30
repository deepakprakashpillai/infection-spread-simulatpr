from simulation import Simulation,Population

population_size = int(input("Enter population size: "))
initial_infection_rate = float(input("Enter initial infection rate (as a decimal): "))
recovery_rate = float(input("Enter recovery rate (as a decimal): "))
simulation_days = int(input("Enter number of simulation days: "))

sim = Simulation(population_size, initial_infection_rate, recovery_rate, simulation_days)
pop = Population(sim.population_size, sim.initial_infection_rate, sim.recovery_rate)

for _ in range(sim.simulation_days):
    pop.daily_update()

infected_count = sum(1 for person in pop.people if person.is_infected)
recovered_count = sum(1 for person in pop.people if person.is_recovered)
healthy_count = sim.population_size - infected_count - recovered_count
print(f"Number of infected people at the end of the simulation: {infected_count}")
print(f"Number of recovered people at the end of the simulation: {recovered_count}")
print(f"Number of people who remained healthy: {healthy_count}")
