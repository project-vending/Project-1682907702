 
import os

# Define the root directory for the project
root_dir = "./data-lake"

# Create the directories for the project
os.makedirs(root_dir, exist_ok=True)
os.makedirs(os.path.join(root_dir, "raw"), exist_ok=True)
os.makedirs(os.path.join(root_dir, "clean"), exist_ok=True)
os.makedirs(os.path.join(root_dir, "transformed"), exist_ok=True)

# Create empty files in each directory
open(os.path.join(root_dir, "raw", "data.txt"), "w").close()
open(os.path.join(root_dir, "clean", "data.txt"), "w").close()
open(os.path.join(root_dir, "transformed", "data.txt"), "w").close()

