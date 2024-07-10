# Coding-exercise-for-SW-developer-position
My approach for the coding exercise for the SW developer position. I tried to adapt to the coding conventions in the rtsa_decoder, e.g CamelCase for classes and snake_case for everything else.   

For the problem of identifying carriers in a spectrum I use a statistical approach, i.e. I calculate the mean value of the energies and look for areas that are a certain standard deviation away from it.
This algorithm is highly dependent on the threshold: a threshold that is too high includes individual statistical outliers, a threshold that is too small does not cover the entire frequency spectrum.

One way to counteract this would be a cluster analysis, but I have not written this (yet) because I was told that I should finish by the beginning of the week and it was already Wednesday, which is why I felt the urge to finish quickly. Regardless, one possible approach might be to only identify carriers if the range of frequencies has a minimum value. A perhaps more complicated approach could be to calculate distances between assigned coordinates and to carry out cluster analyses based on them, similar to, for example, statistical mechanics.
## Installation
git clone https://github.com/actopozipc/Coding-exercise-for-SW-developer-position
## Usage
If you have Jupyter Notebook installed, you should be able to open SW_dev_coding_exercise.ipynb with it. Note that one needs .rtsa files in the same directory as the notebook one. The project only works with relative paths, so the structure of the directories is important.  
The threshold parameter is outstanding and should be adjusted as needed. 
## License
[MIT](https://mit-license.org/)
