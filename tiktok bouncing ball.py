import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import random

# Number of balls
NUM_BALLS = 10

# Create the figure and axis
fig, ax = plt.subplots()
ax.set_xlim(0, 10)  # Set x-axis boundaries
ax.set_ylim(0, 10)  # Set y-axis boundaries
ax.set_aspect('equal')  # Equal scaling

# Initialize ball positions and velocities
balls = {
    "x": np.random.uniform(1, 9, NUM_BALLS),  # Random x positions
    "y": np.random.uniform(1, 9, NUM_BALLS),  # Random y positions
    "vx": np.random.uniform(-0.2, 0.2, NUM_BALLS),  # Random x velocities
    "vy": np.random.uniform(-0.2, 0.2, NUM_BALLS),  # Random y velocities
}

# Create scatter plot for balls
scatter = ax.scatter(balls["x"], balls["y"], s=100, c=[random.choice(['red', 'blue', 'green', 'orange', 'purple']) for _ in range(NUM_BALLS)])

# Update function for animation
def update(frame):
    # Update positions
    balls["x"] += balls["vx"]
    balls["y"] += balls["vy"]

    # Check for collisions with walls and reverse velocity if needed
    for i in range(NUM_BALLS):
        if balls["x"][i] <= 0 or balls["x"][i] >= 10:
            balls["vx"][i] *= -1
        if balls["y"][i] <= 0 or balls["y"][i] >= 10:
            balls["vy"][i] *= -1

    # Update scatter plot data
    scatter.set_offsets(np.c_[balls["x"], balls["y"]])

# Create animation
ani = FuncAnimation(fig, update, frames=500, interval=20)

# Save the animation as a video or GIF
ani.save("bouncing_balls.gif", writer="pillow", fps=30)  # Save as GIF
# ani.save("bouncing_balls.mp4", writer="ffmpeg", fps=30)  # Save as MP4

# Show the animation
plt.show()
