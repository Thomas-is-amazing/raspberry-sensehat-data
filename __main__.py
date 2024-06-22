from sense_hat import SenseHat  # To access Sense HAT sensor data
import time  # To use time functions for delays
import numpy as np  # To perform numerical operations on data
from scipy.fft import fft  # To perform FFT analysis

sense = SenseHat()

# Parameters
sampling_rate = 50  # samples per second
record_time = 10    # seconds

# Initialize arrays for data storage
accel_data = {'x': [], 'y': [], 'z': []}
gyro_data = {'x': [], 'y': [], 'z': []}

start_time = time.time()
while time.time() - start_time < record_time:
    # Get accelerometer data
    acceleration = sense.get_accelerometer_raw()
    accel_data['x'].append(acceleration['x'])
    accel_data['y'].append(acceleration['y'])
    accel_data['z'].append(acceleration['z'])

    # Get gyroscope data
    gyro = sense.get_gyroscope_raw()
    gyro_data['x'].append(gyro['x'])
    gyro_data['y'].append(gyro['y'])
    gyro_data['z'].append(gyro['z'])

    # Wait for the next sample
    time.sleep(1 / sampling_rate)

# Convert lists to numpy arrays
accel_x = np.array(accel_data['x'])
accel_y = np.array(accel_data['y'])
accel_z = np.array(accel_data['z'])

gyro_x = np.array(gyro_data['x'])
gyro_y = np.array(gyro_data['y'])
gyro_z = np.array(gyro_data['z'])

# Calculate RMS values
rms_accel_x = np.sqrt(np.mean(accel_x**2))
rms_accel_y = np.sqrt(np.mean(accel_y**2))
rms_accel_z = np.sqrt(np.mean(accel_z**2))

rms_gyro_x = np.sqrt(np.mean(gyro_x**2))
rms_gyro_y = np.sqrt(np.mean(gyro_y**2))
rms_gyro_z = np.sqrt(np.mean(gyro_z**2))

print("RMS Acceleration X: {:.2f} g".format(rms_accel_x))
print("RMS Acceleration Y: {:.2f} g".format(rms_accel_y))
print("RMS Acceleration Z: {:.2f} g".format(rms_accel_z))

print("RMS Gyroscope X: {:.2f} °/s".format(rms_gyro_x))
print("RMS Gyroscope Y: {:.2f} °/s".format(rms_gyro_y))
print("RMS Gyroscope Z: {:.2f} °/s".format(rms_gyro_z))

# Perform FFT analysis on accelerometer data
n = len(accel_x)
t = 1.0 / sampling_rate
xf = np.fft.fftfreq(n, t)
yf_x = np.abs(fft(accel_x))
yf_y = np.abs(fft(accel_y))
yf_z = np.abs(fft(accel_z))

print("Frequency domain analysis (Acceleration X):")
for freq, magnitude in zip(xf, yf_x):
    if freq > 0:
        print("Frequency: {:.2f} Hz, Magnitude: {:.2f}".format(freq, magnitude))

# Similarly, you can analyze yf_y and yf_z
