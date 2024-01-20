import json
import argparse

def convert_nerf():
    NERF_SCENES = ['chair', 'drums', 'hotdog', 'lego', 'mic', 'ship']
    for scene in NERF_SCENES:
        with open (f"/home/ccw/project/3DSketch/final_data/nerf_synthetic/{scene}/transforms_test.json", "r") as f:
            meta = json.load(f)
        f = open(f"./data/Voxurf/{scene}_info.txt", "w")
        fov = meta['camera_angle_x']
        f.write(f"{fov}\n")
        for frame in meta['frames']:
            transform = frame['transform_matrix']
            for i in range(4):
                for j in range(4):
                    f.write(f"{transform[i][j]}")
                    if j != 3:
                        f.write(" ")
                f.write("\n")
        f.close()
    return

def convert_invrender():
    with open (f"/home/ccw/project/3DSketch/final_data/synthetic4relight/chair/transforms_test.json", "r") as f:
        meta = json.load(f)
    f = open("./data/Voxurf/invrender_chair_info.txt", "w")
    fov = meta['camera_angle_x']
    f.write(f"{fov}\n")
    for frame in meta['frames']:
        transform = frame['transform_matrix']
        for i in range(4):
            for j in range(4):
                f.write(f"{transform[i][j]}")
                if j != 3:
                    f.write(" ")
            f.write("\n")
    f.close()

    return

def convert_3doodle():
    SCENES = ['basketball', 'benz', 'bigbear', 'bigsnow', 'blueballoon', 'redballoon2', 'toycar', 'toyhorse']
    for scene in SCENES:
        with open (f"/home/ccw/project/3DSketch/final_data/ours/synthetic/{scene}/test/transform.json", "r") as f:
            meta = json.load(f)
        f = open(f"./data/Voxurf/{scene}_info.txt", "w")
        fov = meta['camera_angle_x']
        f.write(f"{fov}\n")
        for frame in meta['frames']:
            transform = frame['transform_matrix']
            for i in range(4):
                for j in range(4):
                    f.write(f"{transform[i][j]}")
                    if j != 3:
                        f.write(" ")
                f.write("\n")
        f.close()
    return


if __name__ == "__main__":
    convert_nerf()
    convert_3doodle()
    convert_invrender()

