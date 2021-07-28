import os
import glob
import io
import xml.etree.ElementTree as ET

import pandas as pd

import random



def remove(num_obj, num_img_removed):
    all_singleobj_files = []
    for xml_file in glob.glob("./train/" + '/*.xml'):
        tree = ET.parse(xml_file)
        root = tree.getroot()
        obj_list = root.findall('object')
        if len(obj_list)==num_obj:
            all_singleobj_files.append(xml_file)


    some_singleobj_files = random.sample(all_singleobj_files, num_img_removed)
    for xml_file in some_singleobj_files:
        img_name = xml_file.replace("xml", "jpg")
        os.remove(img_name)
        os.remove(xml_file)
#
#
# remove(1, 30)
# remove(1, 35)


counter = {}
class_dic = {}
counter_above2 = 0
total_img = 0



xml_list = []
for xml_file in glob.glob("./train/" + '/*.xml'):
    tree = ET.parse(xml_file)
    root = tree.getroot()
    obj_list = root.findall('object')
    total_img += 1
    if len(obj_list) > 2:
        counter_above2 += 1

    if len(obj_list) not in counter:
        counter[len(obj_list)] = 1
    else:
        counter[len(obj_list)] += 1

    for member in obj_list:
            class_name = member.find('name').text

            if class_name not in class_dic:
                class_dic[class_name] = [1,]
            else:
                class_dic[class_name][0] += 1


print("counter_above2", counter_above2)
print("total_img", total_img)
print(class_dic)

# # temp
# for key, value in class_dic:
#
class_table = pd.DataFrame(class_dic).T
dataset_distrib = pd.DataFrame(counter, index= [0]).T.sort_index()
print("class_table", class_table)
print("dataset_distrib", dataset_distrib)

import matplotlib.pyplot as plt
plt.bar(dataset_distrib.index, dataset_distrib[0])
plt.title("frequency of num_classes per img")
plt.xlabel("number of objects")
plt.ylabel("frequency")
plt.savefig("distrib.png")

plt.clf()
plt.bar(class_table.index, class_table[0])
plt.title("frequency of each class")
plt.xlabel("number of objects")
plt.ylabel("frequency")
plt.savefig("class_distrib.png")


#
import random
#

#check whether all img are in a jpg & xml pair
imgs = glob.glob("./train/" + '/*.jpg')
xmls = glob.glob("./train/" + '/*.xml')
for xml_file in xmls:
    img_name = xml_file.replace("xml", "jpg")
    if img_name not in imgs:
        print(xml_file.replace(".xml", ""), "is NOT MATCHING, remove it")

for jpg_file in imgs:
    xml_name = jpg_file.replace("jpg", "xml")
    if xml_name not in xmls:
        print(jpg_file.replace(".jpg", ""), "is NOT MATCHING, remove it")
