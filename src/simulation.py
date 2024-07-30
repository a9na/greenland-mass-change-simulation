import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

data_dir = '../data'
os.makedirs(data_dir, exist_ok=True)

# Generate synthetic data for demonstration
# Assuming monthly data for 10 years
dates = pd.date_range(start='2010-01-01', end='2020-01-01', freq='M')
mass_change = np.cumsum(np.random.normal(0, 10, len(dates)))  # Cumulative sum to simulate mass change

# Create a DataFrame
grace_data = pd.DataFrame({'date': dates, 'mass_change': mass_change})

# Save the synthetic data to a CSV file
csv_path = os.path.join(data_dir, 'grace_greenland.csv')
grace_data.to_csv(csv_path, index=False)

# Load the synthetic data from the CSV file
grace_data = pd.read_csv(csv_path)

# Set the date as the index
grace_data['date'] = pd.to_datetime(grace_data['date'])
grace_data.set_index('date', inplace=True)

# Plot the mass change over time
plt.figure(figsize=(10, 6))
plt.plot(grace_data.index, grace_data['mass_change'], label='Mass Change (Gt)')
plt.xlabel('Date')
plt.ylabel('Mass Change (Gt)')
plt.title('Mass Change over Greenland')
plt.legend()
plt.grid(True)
plt.show()

# Calculating the Liquid Water Equivalent (LWE)
# Area of Greenland = 2.166 million km^2 = 2.166 * 10^12 m^2
area_greenland_m2 = 2.166 * 10**12
lwe = grace_data['mass_change'] * 10**12 / area_greenland_m2  # LWE in meters

# Convert LWE to mm
grace_data['LWE_mm'] = lwe * 1000

# Plot the LWE over time
plt.figure(figsize=(10, 6))
plt.plot(grace_data.index, grace_data['LWE_mm'], label='LWE (mm)')
plt.xlabel('Date')
plt.ylabel('Liquid Water Equivalent (mm)')
plt.title('Liquid Water Equivalent over Greenland')
plt.legend()
plt.grid(True)
plt.show()

# Range Acceleration over Ground Tracks (simplified example)
# Calculate the gradient of the mass change to represent range acceleration
grace_data['range_acceleration'] = np.gradient(grace_data['mass_change'])

# Plot the range acceleration
plt.figure(figsize=(10, 6))
plt.plot(grace_data.index, grace_data['range_acceleration'], label='Range Acceleration (Gt/month)')
plt.xlabel('Date')
plt.ylabel('Range Acceleration (Gt/month)')
plt.title('Range Acceleration over Ground Tracks')
plt.legend()
plt.grid(True)
plt.show()
