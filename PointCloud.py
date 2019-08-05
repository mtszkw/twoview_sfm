import plyfile
import numpy as np

def normalizePointsWithCameraMatrix(points, K):
    focal, cx, cy = K[0, 0], K[0, 2], K[1, 2]
    return np.array([ [(p[0]-cx)/focal, (p[1]-cy)/focal] for p in points])


def savePointCloud(reprojectedPts, colors3D, outputFile):
    vertexes = [ (p[0], p[1], p[2], c[0], c[1], c[2]) for p, c in zip(reprojectedPts, colors3D)]
    # vertexes = [ v for v in vertexes if v[2] >= 0 ] # Discard negative z
    # print(f"\nSample 3D points with colors:\n", vertexes[0])
    dtypes = [('x', 'f8'), ('y', 'f8'), ('z', 'f8'), ('red', 'u1'), ('green', 'u1'), ('blue', 'u1')]
    array = np.array(vertexes, dtype=dtypes)
    element = plyfile.PlyElement.describe(array, "vertex")
    plyfile.PlyData([element]).write(outputFile)
    print("Saved point cloud to", outputFile)

