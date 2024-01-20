import trimesh

SCENE = ["basketball", "benz", "bigbear", "bigsnow", "blueballoon", "chair", "drums", "hotdog", "invrender_chair", "lego", "mic", "redballoon2", "ship", "toycar", "toyhorse"]
print(len(SCENE))

for scene in SCENE:
    mesh_path = f'./data/Voxurf/{scene}_final.ply'
    mesh = trimesh.load(mesh_path)
    mesh.vertices *= (1. / 1.05)
    trimesh.exchange.export.export_mesh(mesh, f'./final_mesh/{scene}.ply')