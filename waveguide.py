import numpy as np
import math
import imageio.v2 as imageio
import cv2
import os

DISPLAY_SIMULATION = True
out_video_name = "waveguide1.mp4"
path_alpha = 0.2

# Function to calculate the Laplace operator used in the wave equation
def calculate_laplace_operator(displacement_grid, step_size):
    rows, cols = displacement_grid.shape[0], displacement_grid.shape[1]
    
    # Initialize arrays for second derivatives in x and y directions
    dx2 = np.zeros((rows, cols), np.float32)
    dy2 = np.zeros((rows, cols), np.float32)

    # Calculate second derivatives using finite difference method
    dx2[1:rows-1, 1:cols-1] = (displacement_grid[0:rows-2, 1:cols-1] - 2 * displacement_grid[1:rows-1, 1:cols-1] + displacement_grid[2:rows, 1:cols-1]) / (step_size ** 2)
    dy2[1:rows-1, 1:cols-1] = (displacement_grid[1:rows-1, 0:cols-2] - 2 * displacement_grid[1:rows-1, 1:cols-1] + displacement_grid[1:rows-1, 2:cols]) / (step_size ** 2)

    # Return the sum of second derivatives
    return dx2 + dy2

# Function to detect edges in the wave speed grid
def detect_edges(wave_speed_grid):
    rows, cols = wave_speed_grid.shape[0], wave_speed_grid.shape[1]

    dx = np.zeros((rows, cols), np.float32)
    contour = np.zeros((rows, cols), np.float32)

    # Detect edges based on differences in wave speed
    dx[0:rows-1, 0:cols-1] = np.abs(wave_speed_grid[0:rows-1, 1:cols] - wave_speed_grid[1:rows, 1:cols]) + np.abs(wave_speed_grid[1:rows, 0:cols-1] - wave_speed_grid[1:rows, 1:cols]) > 0
    contour[dx > 0] = 1

    return contour

# Function to run the wave simulation
def run_wave_simulation(pixel_size, time_step, grid_height, grid_width, simulation_steps, broadcast_function):
    displacement_grid = np.zeros((grid_height, grid_width), np.float32)
    velocity_grid = np.zeros((grid_height, grid_width), np.float32)

    output_data = np.zeros((grid_height, grid_width, 3), np.float32)

    # Create a video writer
    if os.path.exists(out_video_name):
        input("Video file already exists. Press Enter to overwrite or Ctrl+C to cancel.")
        os.remove(out_video_name)
    writer = imageio.get_writer(out_video_name, fps=30)

    for current_step in range(0, simulation_steps):
        print(f"Step {current_step}/{simulation_steps}", end="\r")

        # Get broadcasting elements, mask, and wave speed from the broadcast function
        broadcasting_elements, broadcasting_mask, wave_speed = broadcast_function(current_step)

        # Update displacement and velocity using wave equation
        displacement_grid[broadcasting_mask == 1] = broadcasting_elements[broadcasting_mask == 1]
        velocity_grid = velocity_grid + np.multiply(np.square(wave_speed), calculate_laplace_operator(displacement_grid, pixel_size) * time_step)
        displacement_grid = displacement_grid + velocity_grid * time_step

        # Update displacement considering broadcasting elements
        updated_displacement = displacement_grid
        updated_displacement[broadcasting_mask == 1] = 0

        # Update output data red and green channels with the updated displacement
        output_data[0:grid_height, 0:grid_width, 0] = np.maximum(updated_displacement, 0) / np.max(np.maximum(updated_displacement, 0) + 1e-10) * 255
        output_data[0:grid_height, 0:grid_width, 1] = np.minimum(updated_displacement, 0) / np.min(np.minimum(updated_displacement, 0) + 1e-10) * 255
        
        # mark the path
        output_data = output_data * (1 - path_alpha) + (waveguide_img) * path_alpha

        # Highlight edges in the blue channel
        output_data[0:grid_height, 0:grid_width, 2] = detect_edges(wave_speed) * 255

        # Append current frame to the video
        output_data = output_data.astype(np.uint8)
        writer.append_data(output_data)

        if DISPLAY_SIMULATION:
            # Display the current frame
            cv2.imshow("Waveguide", output_data)
            key = cv2.waitKey(1)
            if key == ord('q') or key == 27:
                break

# Simulation parameters
pixel_size = 0.1
time_step = 0.01
grid_height = 1024
grid_width = 1024
simulation_steps = 8000

# Broadcasting function based on an image
def image_broadcast_function(current_step):
    broadcasting_elements = np.zeros((grid_height, grid_width), np.float32)
    broadcasting_mask = np.zeros((grid_height, grid_width), int)

    wave_speed_constant = 6
    wave_speed = np.full((grid_height, grid_width), wave_speed_constant, np.float32)
    # wave_speed = np.ones((grid_height, grid_width), np.float32) * wave_speed_constant
    wave_speed[(waveguide_img[0:1024, 0:1024, 2] / 255) > 0.5] = wave_speed_constant * 0.3


    wave_center_x = 512
    broadcasting_elements[32:36, (wave_center_x - 40):(wave_center_x + 40)] = 0
    broadcasting_mask[32:36, (wave_center_x - 40):(wave_center_x + 40)] = 1

    broadcasting_mask[36:38, (wave_center_x - 30):(wave_center_x + 30)] = 1
    broadcasting_elements[36:38, (wave_center_x - 30):(wave_center_x + 30)] = math.sin(2 * math.pi * (current_step) * 0.008)

    return broadcasting_elements, broadcasting_mask, wave_speed

# Load image for broadcasting function
waveguide_img = imageio.imread("./guide_path.bmp")

# Run the wave simulation
run_wave_simulation(pixel_size, time_step, grid_height, grid_width, simulation_steps, image_broadcast_function)
