"""
This script is used to find two videos with the labels Driving , Nature and Vehicle
"""
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import os
import warnings
warnings.filterwarnings('ignore')


if __name__ == '__main__':
    video_lvl_path= video_lvl_path = "./train/"
    labels_df = pd.read_csv('label_names.csv')

    matching_filenames = []
    for filename in os.listdir(video_lvl_path):
        if filename.endswith(".tfrecord"):
            for example in tf.python_io.tf_record_iterator(video_lvl_path + filename):

                tf_example = tf.train.Example.FromString(example)
                label_example = list(tf_example.features.feature['labels'].int64_list.value)
                label_example_textual = list(labels_df[labels_df['label_id'].isin(label_example)]['label_name'])
                label_match_count = 0
                for label in label_example_textual:
                    if label == 'Driving' or label == 'Nature' or label == 'Vehicle':
                        label_match_count += 1

                if label_match_count == 3:
                    matching_filenames.append(filename)
                    print(label_match_count)
        else:
            continue