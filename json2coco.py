import os
import json
import argparse
import random
from shutil import copyfile
from pycocotools.coco import COCO

# ref  https://blog.csdn.net/wc781708249/article/details/79603522
#      https://github.com/cocodataset/cocoapi/blob/master/PythonAPI/pycocotools/coco.py

def group_dataset(input_path, output_path, img_prefix, num_sample):
    if not os.path.exists(input_path):
        print("Invalid input folder path!")
        os._exit()
    if not os.path.exists(img_prefix):
        os.makedirs(img_prefix)
    
    # load meta.json        
    with open(os.path.join(input_path, "meta.json"), "r") as f:
        coco = json.load(f)
    coco["images"] = []
    coco["annotations"] = []
        
    with open(os.path.join(input_path, "list.json"), "r") as f:
        ImgIDs = json.load(f)["ImgIDs"]
    
    if num_sample > 0:
        ImgIDs = random.sample(ImgIDs, num_sample) # randomly select N sample
        #ImgIDs = ImgIDs[:num_sample]    # select first N
    
    for ImgID in ImgIDs:
        with open(os.path.join(input_path, 'images', "{}.json".format(ImgID)), "r") as f:
            json_dict = json.load(f)
    
        coco["images"].extend(json_dict["images"])
        coco["annotations"].extend(json_dict["annotations"]) 
        
        # copy img file
        original_img_name = json_dict["images"][0]["file_name"]
        source_path = os.path.join(input_path, 'images', "{}.jpg".format(ImgID))
        if os.path.exists(source_path):
            copyfile(source_path, os.path.join(img_prefix, original_img_name))
        else:
            print("'{}' file does not exist.".format(source_path))
    
    # save json 
    with open(output_path, "w") as f:
        f.write(json.dumps(coco, indent=4, separators=(',', ':')))
            
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
                    
       """     
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="JSON to COCO" )
    parser.add_argument("-input", type=str, default="/data/wedward/coco_v11/", help="Meta/list json's dir path")
    parser.add_argument('-output', type=str, default="/data/wedward/coco_v11/coco_validation.json", help="Json annotation output path")
    parser.add_argument('-img_prefix', type=str, default="/data/wedward/coco_v11/validation/", help="COCO image prefix")
    parser.add_argument('-num_sample', type=int, default=0, help="Select 0 if want to process all, or provide an integer")
    args = parser.parse_args()

    group_dataset(args.input, args.output, args.img_prefix, num_sample=args.num_sample)
