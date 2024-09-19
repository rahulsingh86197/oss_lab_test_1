import numpy as np
import matplotlib.pyplot as plt


lions = np.array([15, 16, 17, 20, 19, 21, 23, 24, 25, 27])
elephants = np.array([50, 52, 54, 53, 55, 56, 57, 59, 60, 62])
zebras = np.array([100, 98, 95, 97, 96, 94, 95, 93, 92, 90])


population_data = {
    'Lions': lions,
    'Elephants': elephants,
    'Zebras': zebras
}

def calculate_total_population(population_data):
    total_population = {species: np.sum(data) for species, data in population_data.items()}
    return total_population

def calculate_average_growth(population_data):
    average_growth = {}
    for species, data in population_data.items():
        yearly_growth = np.diff(data)  
        avg_growth = np.mean(yearly_growth)
        average_growth[species] = avg_growth
    return average_growth

def calculate_yearly_growth_rate(population_data):
    growth_rate = {}
    for species, data in population_data.items():
        yearly_growth_rate = np.diff(data) / data[:-1] * 100  
        growth_rate[species] = yearly_growth_rate
    return growth_rate

def visualize_population_trends(population_data):
    years = np.arange(1, 11)  
    plt.figure(figsize=(10, 6))
    
    for species, data in population_data.items():
        plt.plot(years, data, marker='o', label=species)
    
    plt.title('Population Trends Over 10 Years')
    plt.xlabel('Years')
    plt.ylabel('Population (in thousands)')
    plt.xticks(years)
    plt.legend()
    plt.grid(True)
    plt.show()

def analyze_species_performance(population_data):
    average_growth = calculate_average_growth(population_data)
    highest_growth_species = max(average_growth, key=average_growth.get)
    return highest_growth_species, average_growth[highest_growth_species]

def visualize_final_population(population_data):
    final_population = [data[-1] for data in population_data.values()]
    species_names = list(population_data.keys())
    
    plt.figure(figsize=(8, 5))
    plt.bar(species_names, final_population, color=['orange', 'blue', 'green'])
    plt.title('Final Population of Each Species After 10 Years')
    plt.ylabel('Population (in thousands)')
    plt.grid(axis='y')
    plt.show()


if __name__ == "__main__":
  
    total_population = calculate_total_population(population_data)
    average_growth = calculate_average_growth(population_data)
    
    print("Total Population for each species over 10 years:", total_population)
    print("Average Yearly Population Growth:", average_growth)
    
 
    yearly_growth_rate = calculate_yearly_growth_rate(population_data)
    for species, rates in yearly_growth_rate.items():
        print(f"Yearly Growth Rate for {species} (Year 1-9):", rates)

    
    visualize_population_trends(population_data)

    
    highest_growth_species, highest_growth_rate = analyze_species_performance(population_data)
    print(f"Species with highest average growth rate: {highest_growth_species} ({highest_growth_rate:.2f} thousands/year)")
    
    
    visualize_final_population(population_data)
