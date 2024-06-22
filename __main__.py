from sense_hat import SenseHat  # To access Sense HAT sensor data
import time  # To use time functions for delays
import math  # To perform mathematical operations

sense = SenseHat()

# Parameters
sampling_rate = 50  # samples per second
record_time = 10    # seconds

# Initialize lists for data storage
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

# Helper function to calculate RMS
def calculate_rms(values):
    return math.sqrt(sum(v**2 for v in values) / len(values)) if values else 0

# Calculate RMS values
rms_accel_x = calculate_rms(accel_data['x'])
rms_accel_y = calculate_rms(accel_data['y'])
rms_accel_z = calculate_rms(accel_data['z'])

rms_gyro_x = calculate_rms(gyro_data['x'])
rms_gyro_y = calculate_rms(gyro_data['y'])
rms_gyro_z = calculate_rms(gyro_data['z'])

print("RMS Acceleration X: {:.2f} g".format(rms_accel_x))
print("RMS Acceleration Y: {:.2f} g".format(rms_accel_y))
print("RMS Acceleration Z: {:.2f} g".format(rms_accel_z))

print("RMS Gyroscope X: {:.2f} °/s".format(rms_gyro_x))
print("RMS Gyroscope Y: {:.2f} °/s".format(rms_gyro_y))
print("RMS Gyroscope Z: {:.2f} °/s".format(rms_gyro_z))

# Helper function for FFT
def fft(x):
    N = len(x)
    if N <= 1: 
        return x
    even = fft(x[0::2])
    odd = fft(x[1::2])
    T = [math.e**(-2j * math.pi * k / N) * odd[k] for k in range(N // 2)]
    return [even[k] + T[k] for k in range(N // 2)] + [even[k] - T[k] for k in range(N // 2)]

# Perform FFT analysis on accelerometer data
def fft_magnitudes(values, sampling_rate):
    N = len(values)
    if N == 0:
        return [], []
    
    f_values = fft(values)
    magnitudes = [abs(f) for f in f_values[:N // 2]]
    frequencies = [i * sampling_rate / N for i in range(N // 2)]
    return frequencies, magnitudes

# Convert data to complex format for FFT
def convert_to_complex(data_list):
    return [complex(v, 0) for v in data_list]

accel_x_complex = convert_to_complex(accel_data['x'])
accel_y_complex = convert_to_complex(accel_data['y'])
accel_z_complex = convert_to_complex(accel_data['z'])

# Get frequency and magnitude for X axis
frequencies_x, magnitudes_x = fft_magnitudes(accel_x_complex, sampling_rate)

print("Frequency domain analysis (Acceleration X):")
for freq, magnitude in zip(frequencies_x, magnitudes_x):
    if freq > 0:
        print("Frequency: {:.2f} Hz, Magnitude: {:.2f}".format(freq, magnitude))

# Similarly, you can analyze frequencies_y and frequencies_z
