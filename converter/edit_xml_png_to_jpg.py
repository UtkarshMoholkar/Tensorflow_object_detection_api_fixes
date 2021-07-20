import os


list_of_files = os.listdir()
list_of_xml = list(filter(lambda x:x.split(".")[-1]=="xml", list_of_files))

for xml_file in list_of_xml:
    with open(xml_file) as temp:
        xml_content = temp.read()

    new_xml_content = xml_content.replace("png", "jpg")
    with open(xml_file, "w") as temp2:
        temp2.write(new_xml_content)


