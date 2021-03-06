import numpy
import math
from abaqus import mdb
import abaqusConstants as aq 
from hAssembly import *
from hCoordinates import *
from hJob import *
from hMaterial import *
from hMesh import *
from hModel import *
from hPart import *
from hProperty import *
from hStep import *
session.journalOptions.setValues(replayGeometry=COORDINATE, recoverGeometry=COORDINATE)

cylinders = [[[[172.221, 117., 80.6], [167.992, 123.899, 62.3099]], 
  3], [[[119.213, 69.8651, 154.28], [132.045, 59.1809, 165.288]], 
  3], [[[66.5381, 61.9916, 85.9758], [69.4275, 77.3903, 73.5447]], 
  3], [[[84.7198, 66.1184, 87.5074], [79.662, 67.7371, 68.2253]], 
  3], [[[102.031, 155.939, 100.878], [83.2839, 153.706, 94.278]], 
  3], [[[79.4471, 132.007, 105.134], [87.7911, 145.2, 117.636]], 
  3], [[[37.1558, 139.213, 46.3465], [41.1799, 156.033, 56.3912]], 
  3], [[[72.1218, 175.711, 69.0969], [77.9154, 173.308, 88.0879]], 
  3], [[[187.268, 146.822, 151.292], [189.439, 160.619, 136.977]], 
  3], [[[128.496, 124.949, 82.0603], [137.837, 107.299, 83.1685]], 
  3], [[[20.2758, 129.324, 127.208], [21.5814, 149.067, 130.127]], 
  3], [[[72.9312, 37.197, 31.2934], [84.435, 22.0617, 37.5051]], 
  3], [[[43.8387, 81.0387, 141.963], [50.2986, 72.5358, 125.053]], 
  3], [[[116.029, 32.6558, 50.387], [98.3836, 42.026, 51.2996]], 
  3], [[[82.3727, 54.8213, 137.353], [93.0997, 71.6229, 138.977]], 3],
  [[[122.488, 68.2229, 125.62], [105.009, 67.5764, 115.92]], 
  3], [[[128.125, 117.859, 43.7277], [138.829, 100.969, 43.3133]], 
  3], [[[142.968, 183.635, 86.8428], [158.474, 188.89, 98.3305]], 
  3], [[[95.1378, 120.208, 45.53], [75.882, 114.806, 45.7175]], 
  3], [[[125.347, 175.07, 123.541], [114.851, 169.418, 107.482]], 
  3], [[[114.623, 101.894, 146.643], [114.502, 82.5115, 141.714]], 
  3], [[[56.8849, 84.2373, 64.3962], [73.3324, 95.5013, 66.0093]], 
  3], [[[141.766, 74.7416, 114.032], [131.635, 68.7534, 130.203]], 
  3], [[[37.5254, 140.791, 145.224], [36.8658, 151.735, 128.497]], 
  3], [[[51.9668, 90.4625, 109.144], [57.3243, 72.935, 117.149]], 
  3], [[[102.541, 82.4594, 133.435], [96.5765, 94.2731, 118.439]], 
  3], [[[118.099, 97.0398, 57.7541], [127.77, 79.557, 58.6654]], 
  3], [[[196.595, 97.3998, 95.9589], [199.112, 81.6336, 83.9136]], 
  3], [[[175.503, 114.958, 183.658], [179.034, 134.555, 185.527]],
  3], [[[42.35, 119.816, 162.958], [58.5593, 118.07, 174.542]], 
  3], [[[144.097, 69.5964, 95.0958], [136.174, 51.2376, 95.5184]], 
  3], [[[117.556, 128.656, 103.411], [128.527, 137.97, 89.5228]], 
  3], [[[76.6208, 106.427, 160.996], [86.197, 121.381, 151.795]], 
  3], [[[119.465, 171.756, 158.372], [115.479, 179.28, 140.276]], 
  3], [[[153.714, 157.148, 157.891], [170.353, 155.896, 168.916]], 
  3], [[[95.8907, 96.5172, 54.6998], [82.3136, 82.5559, 59.2545]], 
  3], [[[121.329, 24.332, 66.4592], [102.743, 29.681, 71.5541]], 
  3], [[[54.7745, 182.512, 120.426], [40.2219, 192.143, 130.197]], 
  3], [[[110.145, 141.632, 45.4709], [95.0871, 154.742, 44.2867]], 
  3], [[[85.5059, 186.068, 44.6973], [72.4072, 197.284, 34.567]], 
  3], [[[87.4805, 196.889, 115.796], [82.6448, 195.778, 96.4211]], 
  3], [[[73.9157, 81.4794, 202.558], [82.7309, 63.5271, 202.655]], 
  3], [[[126.366, 57.9674, 62.0306], [142.787, 62.172, 72.645]], 
  3], [[[58.2374, 72.6139, 120.822], [50.9366, 87.7198, 131.709]], 
  3], [[[94.6435, 131.35, 159.443], [109.957, 143.085, 154.173]], 
  3], [[[50.1544, 120.165, 91.2816], [46.4372, 102.41, 99.7038]], 
  3], [[[85.5949, 133.312, 83.5669], [95.7984, 121.928, 96.4627]], 
  3], [[[165.264, 146.706, 105.107], [171.166, 127.712, 107.208]], 
  3], [[[109.039, 144.768, 111.955], [116.209, 134.652, 96.2625]], 
  3], [[[81.7754, 105.19, 144.469], [86.1145, 88.2529, 134.757]], 
  3], [[[35.0072, 105.431, 173.575], [31.6012, 87.3542, 181.424]], 
  3], [[[144.531, 90.6878, 149.446], [133.1, 101.559, 137.152]], 
  3], [[[41.8874, 84.4824, 153.731], [38.9179, 76.4838, 135.643]], 
  3], [[[62.056, 155.683, 129.403], [61.8081, 151.403, 109.868]], 
  3], [[[108.085, 75.526, 38.6315], [123.184, 87.9542, 34.4381]], 
  3], [[[30.7111, 124.873, 85.1418], [30.4723, 122.389, 104.986]], 
  3], [[[67.9046, 141.409, 95.1048], [67.2072, 146.863, 114.334]], 
  3], [[[63.7624, 96.0511, 114.421], [78.8331, 95.3103, 127.548]], 
  3], [[[110.908, 114.821, 51.4107], [120.344, 99.1093, 59.4183]], 
  3], [[[126.825, 113.938, 112.007], [116.456, 108.781, 128.314]], 
  3], [[[45.814, 146.664, 109.641], [60.4839, 147.107, 96.0539]], 
  3], [[[61.7512, 123.653, 61.2726], [74.2027, 111.908, 71.6177]], 
  3], [[[33.2561, 118.281, 113.252], [44.9992, 123.832, 128.46]], 
  3], [[[143.494, 154.343, 62.3645], [129.34, 144.921, 72.8949]], 
  3], [[[150.621, 40.1627, 49.4019], [133.59, 43.0839, 39.3304]], 
  3], [[[106.846, 67.5071, 82.9847], [103.77, 63.2367, 102.28]], 
  3], [[[61.6731, 115.173, 87.7353], [51.0605, 101.976, 77.0957]], 
  3], [[[34.5338, 64.847, 39.7021], [26.0893, 70.8904, 56.795]], 
  3], [[[176.882, 49.4644, 163.303], [180.513, 60.4, 146.956]], 
  3], [[[77.4894, 104.786, 121.56], [88.9037, 113.911, 107.906]], 
  3], [[[182.645, 111.987, 68.4272], [182.489, 122.732, 85.2946]], 
  3], [[[168.601, 194.765, 80.3426], [179.694, 197.754, 63.972]], 
  3], [[[107.969, 90.9313, 114.598], [108.903, 72.7399, 122.856]], 
  3], [[[158.611, 69.2433, 115.205], [141.607, 61.4861, 122.323]], 
  3], [[[101.432, 167.774, 13.1107], [94.9262, 186.556, 15.3254]], 
  3], [[[54.2791, 27.6617, 136.591], [56.7417, 32.0917, 155.938]], 
  3], [[[97.0936, 126.117, 122.781], [113.037, 133.545, 113.261]], 
  3], [[[180.498, 132.981, 59.3957], [182.197, 119.44, 74.0162]], 
  3], [[[97.2601, 42.3554, 103.6], [111.918, 46.6931, 116.497]], 
  3], [[[54.0389, 101.592, 127.23], [51.8282, 117.058, 139.717]], 
  3], [[[152.352, 109.496, 168.643], [157.564, 95.6466, 155.189]], 
  3], [[[76.2554, 109.081, 81.7384], [70.8512, 95.9506, 95.823]], 
  3], [[[146.606, 53.7539, 161.085], [155.172, 63.6085, 176.235]], 
  3], [[[171.154, 85.2846, 114.014], [173.421, 87.4933, 94.2663]], 
  3], [[[111.552, 49.6382, 107.127], [110.03, 46.924, 87.3704]], 
  3], [[[105.964, 123.04, 171.172], [104.47, 103.266, 168.571]], 
  3], [[[121.982, 149.738, 179.6], [141.874, 148.964, 177.674]], 
  3], [[[153.341, 130.48, 117.197], [135.413, 125.189, 124.311]], 
  3], [[[104.152, 149.101, 154.617], [86.2493, 142.045, 149.168]], 
  3], [[[76.8494, 60.0475, 30.7148], [92.2339, 72.6707, 28.7224]], 
  3], [[[66.6915, 54.2462, 124.682], [76.1965, 59.6605, 141.425]], 
  3], [[[189.098, 94.3483, 103.258], [180.459, 100.556, 86.3215]], 
  3], [[[41.0195, 159.781, 106.915], [38.1139, 156.09, 87.4743]], 
  3], [[[133.507, 170.566, 113.363], [134.083, 176.964, 94.423]], 3]]

materials = getMatListCNT()
matrix = 'ESBR'
filler = 'CNT'

modelObject, modelName = createModel(2)
side, radius, length, portions, dP, dM, cP, cM = defExperimentFiber(modelObject, matrix, filler)

## HERE we could do something like Calculate number of fibers, then generate the points, etc
## But Just trying to script the assembly of fibers from a pre-made coordinate system.

##

part = createMatrix(modelObject, side, False)
edges1, vertices1, face1 = assignGeomSequence(part) # Create references to important sets in our matrix
part2 = createFiber(modelObject, radius, length) # Create Fiber part
edges2, vertices2, face2 = assignGeomSequence(part2) # Create references to important sets in fiber 
matrixSet, fiberSet = create3DInitialSetsFibers(part, part2, side)

createSection(modelObject, part, matrix, matrixSet) # Create section for matrix material
createSection(modelObject, part2, filler, fiberSet) # Create section for filler material

warningPoints = ""

modelRootAssembly, fullMatrixPart = create3DMatrixFiberInclusions(modelObject, part, part2, cylinders) # Create assembly and return references to assembly sets

