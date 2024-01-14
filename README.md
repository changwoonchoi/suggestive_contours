# suggestive_contours
Modified version of suggestive contour rendering from https://gfx.cs.princeton.edu/proj/sugcon/

# Installation and Usasge
You need g++ to compile these libraries.
```
// install 
cd trimesh2
make
cd ../rtsc-1.6
make

// view suggestive contours
./rtsc ../data/lego.obj ../data/test_65.txt ../output/test_65.ppm
// spacebar reset to default view
// I (uppercase of i) dump the image to the given save path
```