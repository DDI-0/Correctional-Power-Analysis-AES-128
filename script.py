import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os
import csv

# Number of bytes and top correlations
num_bytes = 16
top_n = 3

os.makedirs('plots', exist_ok=True)

for byte_idx in range(num_bytes):
    filename = f"byte_{byte_idx}_correlations.csv"
    
    try:
        # Read CSV file
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            data = [row for row in reader]
        
        # For each of the top 3 correlations
        for rank in range(min(top_n, len(data))):
            if rank < len(data):
                # Get data for this rank
                row = data[rank]
                key_byte = int(row[1])
                correlation = float(row[2])
                
                # Parse data points (hamming distances and power values)
                data_str = row[3]
                data_points = data_str.split('|')
                
                # Extract hamming distances and power values
                hamming_distances = []
                power_values = []
                
                for point in data_points:
                    if ':' in point:
                        h, p = point.split(':')
                        hamming_distances.append(float(h))
                        power_values.append(float(p))
                
                # Convert to numpy arrays
                hamming_distances = np.array(hamming_distances)
                power_values = np.array(power_values)
                
                plt.figure(figsize=(12, 8))
                
                marker_size = max(1, min(10, 9000 / len(hamming_distances)))
                
                # Create scatter plot with alpha transparency to show density
                plt.scatter(hamming_distances, power_values, s=marker_size, alpha=0.5)
                

                
                
                plt.title(f"Byte {byte_idx}, Key Value {key_byte}, Rank {rank+1}\nPearson Correlation: {correlation:.6f}")
                plt.xlabel("Hamming Distance")
                plt.ylabel("Power Consumption")
                plt.grid(True, alpha=0.3)
                
                # correlation coefficient annotation
                plt.annotate(f"r = {correlation:.4f}", 
                            xy=(0.05, 0.95), 
                            xycoords='axes fraction',
                            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
                
                # point count annotation
                plt.annotate(f"Points: {len(hamming_distances)}", 
                            xy=(0.05, 0.89), 
                            xycoords='axes fraction',
                            bbox=dict(boxstyle="round,pad=0.3", fc="white", ec="gray", alpha=0.8))
                
                # Save the plot
                plot_filename = f"plots/byte_{byte_idx}_rank_{rank+1}.png"
                plt.savefig(plot_filename, dpi=300)
                plt.close()
                
                print(f"Created plot {plot_filename}")
                
    except Exception as e:
        print(f"Error processing {filename}: {e}")

