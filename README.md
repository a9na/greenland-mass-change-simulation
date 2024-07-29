# Greenland Mass Change Simulation

This project simulates projecting range acceleration, liquid water equivalent (LWE), and mass concentrations over Greenland using synthetic data.

Explanation:
Synthetic Data Generation: We generate synthetic monthly mass change data for 10 years. The np.cumsum(np.random.normal(0, 10, len(dates))) function creates a cumulative sum of normally distributed random values to simulate the mass change over time.

DataFrame Creation: The synthetic data is stored in a Pandas DataFrame and the date is set as the index.

Mass Change Plot: The mass change over time is plotted using Matplotlib.

Liquid Water Equivalent (LWE) Calculation: The LWE is calculated from the mass change data. The mass change is converted to kilograms (1 Gt = 10^12 kg) and then divided by the area of Greenland to get LWE in meters. This is then converted to millimeters.

LWE Plot: The LWE over time is plotted.

Range Acceleration Calculation: The gradient of the mass change is calculated to represent the range acceleration.

Range Acceleration Plot: The range acceleration over time is plotted.

Notes:
This is a simplified example to demonstrate the process. Real-world data from GRACE satellites would require more sophisticated handling and preprocessing.
