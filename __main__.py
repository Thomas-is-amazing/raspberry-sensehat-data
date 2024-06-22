from sense_hat import SenseHat  # To access Sense HAT sensor data
import time  # To use time functions for delays
import math  # To perform mathematical operations
import cmath  # For handling complex numbers

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

print("RMS Acceleration X: {:.4f} g".format(rms_accel_x))
print("RMS Acceleration Y: {:.4f} g".format(rms_accel_y))
print("RMS Acceleration Z: {:.4f} g".format(rms_accel_z))

print("RMS Gyroscope X: {:.4f} °/s".format(rms_gyro_x))
print("RMS Gyroscope Y: {:.4f} °/s".format(rms_gyro_y))
print("RMS Gyroscope Z: {:.4f} °/s".format(rms_gyro_z))