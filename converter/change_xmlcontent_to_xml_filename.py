import os
import re
import xml.etree.ElementTree as ET

list_of_files = os.listdir()
list_of_xml = list(filter(lambda x:x.split(".")[-1]=="xml", list_of_files))

for xml_file in list_of_xml:
    with open(xml_file) as temp:
        xml_content = temp.read()

    #remove space in the name
    no_space_xml_file = xml_file.replace(" ", "")
    os.rename(xml_file, no_space_xml_file)

    img_file = xml_file.replace("xml", "jpg")
    no_space_img_file = no_space_xml_file.replace("xml", "jpg")
    os.rename(img_file ,no_space_img_file)


    new_xml_content = re.sub("<filename>.+</filename>", f"<filename>{img_file}</filename>", xml_content)
    with open(no_space_xml_file, "w") as temp2:
        temp2.write(new_xml_content)

    tree = ET.parse(no_space_xml_file)
    root = tree.getroot()
    all_path = root.findall("path")
    if all_path:
        path = all_path [0]
        root.remove(path)
        with open(no_space_xml_file , 'wb') as f:
            tree.write(f)
#
# list_of_files = os.listdir()
# list_of_jpg = list(filter(lambda x:x.split(".")[-1]=="jpg", list_of_files))
# for img in list_of_jpg:
#     no_space_img_file = img.replace(" ", "")
#     os.rename(img, no_space_img_file)