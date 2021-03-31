from pycocotools import mask
from skimage import measure
import numpy as np
import json
import cv2
import matplotlib.pyplot as plt
from shapely.geometry import Polygon, MultiPolygon
from PIL import Image
from PIL import ImageDraw
a =  {"image_id": 579, "bbox": [407.4486999511719, 236.60690307617188, 57.411163330078125, 56.066925048828125], "score": 0.9970695972442627, "category_id": 1, "segmentation": {"size": [394, 556], "counts": "`Pn4=k;3N1N2O2M2N2N3M2M3N2M4K4O2N1O1O2O001O001O00001O00001O1O01O00001O0O1O2O0N3N1O2M3K4N3L3N3L3N2L4O2M2N3N2M3M3MoTS1"}}
print(mask.decode(a["segmentation"]))
print(mask.area(a["segmentation"]))
print(mask.toBbox(a["segmentation"]))
contours = measure.find_contours(mask.decode(a["segmentation"]), 0.5)
def close_contour(contour):
    if not np.array_equal(contour[0], contour[-1]):
        contour = np.vstack((contour, contour[0]))
    return contour
for contour in contours:
    segmentation = contour.ravel().tolist()

    print(len(segmentation))
    poly = Polygon(contour)
    poly = poly.simplify(0.001, preserve_topology=True)
    segmentation = np.array(poly.exterior.coords).ravel().tolist()
    # contour = close_contour(contour)
    # contour = measure.approximate_polygon(contour, 0.01)
    # contour = np.flip(contour, axis=1)
    # segmentation = contour.ravel().tolist()
    print(len(segmentation))


contours,_= cv2.findContours(mask.decode(a["segmentation"]).astype(np.uint8), 2,4)
segmentation = []
for contour in contours:
    contour = contour.flatten().tolist()
    plt.plot(contour)
    plt.show()
    # segmentation.append(contour)
    if len(contour) > 4:
        segmentation.append(contour)
    if len(segmentation) == 0:
        continue
    print(len(contour))