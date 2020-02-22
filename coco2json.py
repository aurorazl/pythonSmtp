import os
import json
import argparse
import random
from shutil import copyfile
from pycocotools.coco import COCO

# ref:  https://blog.csdn.net/wc781708249/article/details/79603522
#       https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py

def separate_dataset(input_path, output_path, img_prefix, num_sample):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    if not os.path.exists(os.path.join(output_path, "images")):
        os.makedirs(os.path.join(output_path, "images"))
    coco = COCO(input_path)
    
    # save meta.json        
    meta_json_dict = {
        "info": coco.dataset.get('info', []), 
        "licenses": coco.dataset.get('licenses', []), 
        "type": coco.dataset.get('type', "instance"),
        "categories": coco.dataset.get('categories')}
    
    with open(os.path.join(output_path, "meta.json") , "w") as f:
        f.write(json.dumps(meta_json_dict,indent=4, separators=(',', ':')))  
    
    # Create indivisual coco json annotation
    ImgIDs = list(coco.imgs.keys())
    if num_sample > 0:
        ImgIDs = random.sample(ImgIDs, num_sample) # randomly select N sample
        #ImgIDs = ImgIDs[:num_sample]    # select first N
    
    # export a full list of ImgIDs
    with open(os.path.join(output_path, "list.json") , "w") as f:
        f.write(json.dumps({"ImgIDs":ImgIDs},indent=4, separators=(',', ':'))) 
        
    # export a sequence of ImgIDs lists, separate by category ids 
    for cat in coco.getCatIds():
        ImgIDs_list_by_cat = coco.getImgIds(imgIds=ImgIDs, catIds=[cat])
        with open(os.path.join(output_path, "list_{}.json".format(cat)) , "w") as f:
            f.write(json.dumps({"ImgIDs":ImgIDs_list_by_cat},indent=4, separators=(',', ':'))) 
    
    for ImgID in ImgIDs:
        json_dict = {}
        json_dict["images"] = coco.loadImgs([ImgID])
        json_dict["annotations"] = coco.loadAnns(coco.getAnnIds(imgIds=[ImgID]))
                
        # save json 
        with open(os.path.join(output_path, "images", "{}.json".format(ImgID)), "w") as f:
            f.write(json.dumps(json_dict,indent=4, separators=(',', ':')))
        
        # copy img file
        img_path = os.path.join(img_prefix, json_dict["images"][0]["file_name"])
        if os.path.exists(img_path):
            copyfile(img_path, os.path.join(output_path, "images", "{}.jpg".format(ImgID)))
        else:
            print("'{}' file does not exist.".format(img_path))
    
    """
        image = {"file_name": outout_filename,
                "height": bg_y,
                "width": bg_x,
                "id": img_id,
                    }
                    
        images = [image]
                    
        ann = {"area": o_w * o_h,
                       "iscrowd": 0,
                       "image_id": img_id,
                       "bbox": [random_obj_x_pos, random_obj_y_pos, o_w, o_h],
                       "category_id": category_id,
                       "id": bnd_id,
                       "ignore": 0,
                       "segmentation": [],
                } 
        anns = [ann_1, ann_2, ann_3......]
        
        categories = [{'supercategory': 'prohibited', 'id': 1, 'name': 'lighter'},
                     {'supercategory': 'prohibited', 'id': 2, 'name': 'match'}....]
                    
       """     
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="COCO to JSON" )
    parser.add_argument("-input", type=str, default="/data/coco2017/annotations/instances_val2017.json", help="COCO json annotation path")
    parser.add_argument('-output', type=str, default="/data/wedward/coco_v11/")
    parser.add_argument('-img_prefix', type=str, default="/data/coco2017/val2017/", help="COCO image prefix")
    parser.add_argument('-num_sample', type=int, default=1, help="Select 0 if want to process all")
    args = parser.parse_args()

    separate_dataset(args.input, args.output, args.img_prefix, num_sample=args.num_sample)