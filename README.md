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
./rtsc ../data/Voxurf/lego_final.ply ../data/Voxurftest_info.txt ../output/lego/

// enter the viewer
[keyboard input]: enter ' ' and 'i' to move onto next viewpoint and save images.

```


# Instruction for dg-mesh work

## preprocess poses
```
python make_pose_info.py
```

```
cd trimesh2
make
cd ../rtsc-1.7
make

./rtsc {mesh directory} {pose txt file directory} {output image fname}
(You need to pre-create directories for output images)
press 'i' to save image
```