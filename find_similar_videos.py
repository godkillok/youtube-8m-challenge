"""
This script is used to find two videos with the labels Top Labels: Driving , Nature, Animal, Music and Vehicle /
"""
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import tensorflow as tf
import os
import warnings
warnings.filterwarnings('ignore')


if __name__ == '__main__':
    video_lvl_path= video_lvl_path = "./train/"
    labels_df = pd.read_csv('label_names.csv')

    file_match_count =0
    for filename in os.listdir(video_lvl_path):
        if filename.endswith(".tfrecord"):
            for example in tf.python_io.tf_record_iterator(video_lvl_path + filename):

                tf_example = tf.train.Example.FromString(example)
                label_example = list(tf_example.features.feature['labels'].int64_list.value)
                label_example_textual = list(labels_df[labels_df['label_id'].isin(label_example)]['label_name'])

                label_match_count = 0
                video_labels = []
                for label in label_example_textual:
                    if label == 'Driving' or label == 'Nature' or label == 'Vehicle' or label == 'Animal' or label == 'Music':
                        label_match_count += 1
                        video_labels.append(label)

                if label_match_count == 3:
                    file_match_count +=1
                    print("-------------------- Video: " +  file_match_count +  "----------------\n")
                    print("Filename: " + filename + "\n")
                    print("Labels: " + video_labels[0] + ", " + video_labels[1] + ", " + video_labels[3] + "\n" )
        else:
            continue