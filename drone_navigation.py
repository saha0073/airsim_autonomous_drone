import airsim
import time

# Connect to AirSim
client = airsim.MultirotorClient(ip="127.0.0.1", port=41451)
client.confirmConnection()
print("Connected to AirSim!")

# Enable API control
client.enableApiControl(True, "Drone1")
client.armDisarm(True, "Drone1")

# Take off
print("Taking off...")
client.takeoffAsync(vehicle_name="Drone1").join()

# Move to a position
print("Moving to (5, 0, -10)...")
client.moveToPositionAsync(5, 0, -10, 5, vehicle_name="Drone1").join()

# Hover
print("Hovering...")
client.hoverAsync(vehicle_name="Drone1").join()
time.sleep(5)

# Land
print("Landing...")
client.landAsync(vehicle_name="Drone1").join()

# Cleanup
client.armDisarm(False, "Drone1")
client.enableApiControl(False, "Drone1")
print("Done!")