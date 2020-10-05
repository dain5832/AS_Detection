# import the necessary packages
import os
import glob
import pandas as pd
import io
import argparse

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2' # Suppress Tensorflow logging
import tensorflow.compat.v1 as tf
from PIL import Image
from object_detection.utils import dataset_util, label_map_util
from collections import namedtuple

# Initiate argument parser
parser = argparse.ArgumentParser(
    description="Sample TensorFlow CSV-to-TFRecord converter")
parser.add_argument("-c",
                    "--csv_dir",
                    help="Path to the folder where the input .csv file is stored.",
                    type=str)
parser.add_argument("-l",
                    "--labels_path",
                    help="Path to the labels (.pdtxt) file.", type=str)
parser.add_argument("-o",
                    "--output_path",
                    help="Path of output TFRecord (.record) file.", type=str)
parser.add_argument("-i",
                    "--image_dir",
                    help="Path to the folder where the input image files are stored. "
                    "Defaults to the same directory as CSV_DIR.",
                    type=str, default=None)
args = parser.parse_args()

if args.image_dir is None:
    args.image_dir = args.csv_dir

label_map = label_map_util.load_labelmap(args.labels_path)
label_map_dict = label_map_util.get_label_map_dict(label_map)

# required csv file column: filename, width, height, class, xmin, ymin, xmax, ymax

def class_text_to_int(row_label):
    return label_map_dict[row_label]

# gb.groups.keys = unique한 파일이름, gb.groups = 파일이름과 해당하는 rowindex들이 저장되어있는 dict
# gb.get_group(key) = key에 해당되는 row가 return됨.
def split(df, group):
    data = namedtuple('data', ['filename', 'object'])
    gb = df.groupby(group)
    return [data(filename, gb.get_group(x)) for filename, x in zip(gb.groups.keys(), gb.groups)]

# input으로 들어가는 group은 1개의 file 정보가 들어있는 tuple.
def create_tf_example(group, path):
    with tf.gfile.GFile(os.path.join(path, '{}'.format(group.filename)), 'rb') as fid:
        encoded_jpg = fid.read()
    encoded_jpg_io = io.BytesIO(encoded_jpg)
    image = Image.open(encoded_jpg_io)
    width, height = image.size

    filename = group.filename.encode('utf8')
    image_format = b'jpg'
    xmins = []
    xmaxs = []
    ymins = []
    ymaxs = []
    classes_text = []
    classes = []

    for index, row in group.object.iterrows():
        scale = row['Scale']
        xmins.append((row['BX'] * scale) / width)
        xmaxs.append((row['BX'] + row['Width']) * scale / width)
        ymins.append((row['BY'] * scale) / height)
        ymaxs.append((row['BY'] + row['Height']) * scale / height)
        classes_text.append(row['label_SIJ'].encode('utf8'))
        classes.append(class_text_to_int(row['label_SIJ']))

    tf_example = tf.train.Example(features=tf.train.Features(feature={
        'image/height': dataset_util.int64_feature(height),
        'image/width': dataset_util.int64_feature(width),
        'image/filename': dataset_util.bytes_feature(filename),
        'image/source_id': dataset_util.bytes_feature(filename),
        'image/encoded': dataset_util.bytes_feature(encoded_jpg),
        'image/format': dataset_util.bytes_feature(image_format),
        'image/object/bbox/xmin': dataset_util.float_list_feature(xmins),
        'image/object/bbox/xmax': dataset_util.float_list_feature(xmaxs),
        'image/object/bbox/ymin': dataset_util.float_list_feature(ymins),
        'image/object/bbox/ymax': dataset_util.float_list_feature(ymaxs),
        'image/object/class/text': dataset_util.bytes_list_feature(classes_text),
        'image/object/class/label': dataset_util.int64_list_feature(classes),
    }))
    return tf_example


def main(_):

    writer = tf.python_io.TFRecordWriter(args.output_path)
    path = os.path.join(args.image_dir)
    examples = pd.read_csv(args.csv_dir)
    grouped = split(examples, 'Filename')
    for group in grouped:
        tf_example = create_tf_example(group, path)
        writer.write(tf_example.SerializeToString())
    writer.close()
    print('Successfully created the TFRecord file: {}'.format(args.output_path))


# check to see if the main thread should be started
if __name__ == "__main__":
    tf.app.run()
