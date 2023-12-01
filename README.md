# Annotation false positive validation by Daksh Shah
This project has been tested using Python 3.10.12 and Ubuntu 22.04.

## Visualize.py
To use this project, first edit the variables:
- `image_dir` with the path to the images directory
- `GT_dir` with the path to the ground truth labels directory
- `HL_dir` with the path to the predicted labels directory
- `validated_dir` with the path to the validated data directory

When running the project, it has only been implemented to work with specific image numbers and hasn't been tested with a larger series of files sequentially. 

> Note: The current version has only been tested to work on a specific file. Before running, edit line 133 so that `image_name()` has a parameter containing the image/file number you want to validate.
## Dependencies:
- numpy
- opencv
- tkinter
- PIL