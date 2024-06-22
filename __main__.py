from sense_hat import SenseHat
import time

sense = SenseHat()

while True:
    # Get temperature
    temp = sense.get_temperature()
    print("Temperature: {:.2f} °C".format(temp))

    # Get humidity
    humidity = sense.get_humidity()
    print("Humidity: {:.2f} %".format(humidity))

    # Get pressure
    pressure = sense.get_pressure()
    print("Pressure: {:.2f} hPa".format(pressure))

    # Get orientation
    orientation = sense.get_orientation()
    print("Pitch: {:.2f}°".format(orientation['pitch']))
    print("Roll: {:.2f}°".format(orientation['roll']))
    print("Yaw: {:.2f}°".format(orientation['yaw']))

    # Get accelerometer data
    acceleration = sense.get_accelerometer_raw()
    print("Acceleration X: {:.2f} g".format(acceleration['x']))
    print("Acceleration Y: {:.2f} g".format(acceleration['y']))
    print("Acceleration Z: {:.2f} g".format(acceleration['z']))

    # Get gyroscope data
    gyro = sense.get_gyroscope_raw()
    print("Gyroscope X: {:.2f} °/s".format(gyro['x']))
    print("Gyroscope Y: {:.2f} °/s".format(gyro['y']))
    print("Gyroscope Z: {:.2f} °/s".format(gyro['z']))

    # Get magnetometer data
    mag = sense.get_compass_raw()
    print("Magnetometer X: {:.2f} μT".format(mag['x']))
    print("Magnetometer Y: {:.2f} μT".format(mag['y']))
    print("Magnetometer Z: {:.2f} μT".format(mag['z']))

    # Wait for a second before next read
    time.sleep(10)