# Importing necessary libraries
import random  # for generating random numbers
import math    # for mathematical functions like sqrt
import pandas as pd  # for handling data in a DataFrame
import matplotlib.pyplot as plt  # for creating plots

# Function to simulate dart throws and estimate pi
def throw_darts(num_darts):
    inside_circle = 0

    for _ in range(num_darts):
        # Generate random coordinates for each dart throw
        x = random.random()
        y = random.random()

        # Calculate the distance from the origin (0,0)
        distance = math.sqrt(x**2 + y**2)

        # Check if the dart landed inside the unit circle
        if distance <= 1:
            inside_circle += 1

    # Calculate the probability of hitting inside the unit circle
    probability_of_hitting = inside_circle / num_darts

    # Use the probability to estimate pi
    estimated_pi = 4 * probability_of_hitting

    return estimated_pi

# Function to run multiple simulations with different parameters
def run_simulation(num_darts_list, num_experiments, num_runs):
    all_results = []

    for num_darts in num_darts_list:
        experiment_results = []

        for _ in range(num_experiments):
            pi_values = []

            for _ in range(num_runs):
                # Run the dart throwing simulation multiple times
                estimated_pi = throw_darts(num_darts)
                pi_values.append(estimated_pi)

            # Calculate mean and mode of the estimated pi values
            mean_pi = sum(pi_values) / num_runs
            mode_pi = max(set(pi_values), key=pi_values.count)

            # Record the results for this experiment
            experiment_results.append({
                'Num Darts': num_darts,
                'Mean Pi': mean_pi,
                'Mode Pi': mode_pi,
            })

        # Collect results from all experiments
        all_results.extend(experiment_results)

    # Save results to an Excel file
    results_df = pd.DataFrame(all_results)
    results_df.to_excel('C:\\Users\\Mathu\\OneDrive\\Desktop\\dart_simulation_results.xlsx', index=False)

    return results_df

# Function to plot the results of the simulation
def plot_results(dataframe):
    # Plot the mean and mode of estimated pi values
    plt.figure(figsize=(10, 6))
    plt.plot(dataframe['Num Darts'], dataframe['Mean Pi'], marker='o', label='Mean Pi')
    plt.plot(dataframe['Num Darts'], dataframe['Mode Pi'], marker='o', label='Mode Pi')

    # Plot a horizontal line representing the exact value of pi
    plt.axhline(y=math.pi, color='r', linestyle='--', label='Exact Pi')

    # Set plot properties
    plt.xscale('log')
    plt.xlabel('Number of Darts')
    plt.ylabel('Estimated Pi')
    plt.title('Estimation of Pi using Dart Simulation')
    plt.legend()
    plt.grid(True)

    # Save plot to a file and display it
    plt.savefig('pi_estimation_plot.png')
    plt.show()

# Main block to define simulation parameters and execute the code
if __name__ == "__main__":
    # Define parameters for the simulation
    num_darts_list = [1000, 10000, 100000, 1000000]
    num_experiments = 10
    num_runs = 10

    # Run the simulation and store the results
    simulation_results = run_simulation(num_darts_list, num_experiments, num_runs)

    # Plot the results
    plot_results(simulation_results)
