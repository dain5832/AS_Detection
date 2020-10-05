# import the necessary packages
from collections import namedtuple
from imutils import paths
import argparse
import imutils
import cv2
import os
from glob import glob
import pandas as pd
import random

# construct the argument parse and parse the arguments
ap = argparse.ArgumentParser()
ap.add_argument("-a", "--annot", required=False, default="/home/user/TensorFlow/workspace/training_AS/annotations/AS_annotation_task_revised.csv", help="path to input annotation file in csv format")
ap.add_argument("-o", "--output", required=False, default="/home/user/TensorFlow/workspace/training_AS/annotations/AS_annotation_task_updated.csv", help="path to output csv file")
args = vars(ap.parse_args())

# open csvfile that has annotation data
random.seed(42)
total = 0
csv_file = pd.read_csv(args["annot"], header=0)
col_list = csv_file.columns.to_list() + ["Grade"]
data = []

# gb.groups.keys = unique한 파일이름, gb.groups = 파일이름과 해당하는 rowindex들이 저장되어있는 dict
# gb.get_group(key) = key에 해당되는 row가 return됨.
def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

def yield_group(grouped_list):
    random.shuffle(grouped_list)
    for group in grouped_list:
        for (i, row) in group[1].iterrows():
            yield (i, row)

# open updated annotation file if exists
if os.path.exists(args["output"]):
    output = pd.read_csv(args["output"], header=0)
    filenames = output["Filename"].to_list()
else:
    output = pd.DataFrame(columns=col_list)
    filenames = []

try:
    # loop over the individual rows, skipping the header
    grouped = split(csv_file, 'Filename')

    for (i, row) in yield_group(grouped):
        print("[INFO] processing image {}/{}".format(total + 1, len(csv_file)))
        total += 1

        # break the row into components
        (_, _, filename, startX, startY, width, height, scale, img_height, img_width, label) = row
        if filename in filenames:
            print("[INFO] {} has been already annotated. Skip the file...".format(filename))
            continue
        (startX, startY) = (float(startX) * float(scale), float(startY) * float(scale))
        (width, height) = (float(width) * float(scale), float(height) * float(scale))
        (endX, endY) = (startX + width, startY + height)

        # build the path to the input image
        imagePath = glob('/home/user/TensorFlow/workspace/training_AS/images/*/' + filename)
        # load the input image
        image = cv2.imread(imagePath[0])
        
        # draw bounding box
        cv2.rectangle(image, (int(startX), int(startY)),
                      (int(endX), int(endY)), (0, 255, 0), 2)

        # show the output iamge
        cv2.imshow(filename, imutils.resize(image, width=700))
        key = cv2.waitKey(0)

        # if the '`' key is pressed, then ignore the chatacter
        if key == 27:
            print("[INFO] break")
            break
        else:
            key = chr(key).upper()

        # grab the key that was pressed and construct the path
        # the output directory
        row = row.to_list() + [key]
        data.append(row)

        cv2.destroyAllWindows()

except KeyboardInterrupt:
    print("[INFO] manually leaving script")

# an unknown error has occured for this particular image
except Exception as error:
    print("[INFO] skipping image...")
    print(error)

df = pd.DataFrame(data, columns=col_list)

# merge dataframes
output = output.append(df, ignore_index=True)
output.to_csv(args["output"], sep=",", index=False)
