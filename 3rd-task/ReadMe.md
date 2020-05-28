# Image compression task

The required was performing a simple image compression algorithm by using `2D - Discrete Cosine Transform` on the image in the form of 8x8 block and retraining only few components on an image file

### Running the code

Just run `main.py` and then the program will run the algorithm 4 times for m from 1 to 4 each time retraining only the top left mxm block from each 8x8 block and output each compressed binary file in numpy file format and the decompressed image each named `decompressedm{the used m goes here}` e.g.`decompressedm1.bmp` .bmp for images and npy for compressed files.

The program also displays the original image and each of its color components separately.
