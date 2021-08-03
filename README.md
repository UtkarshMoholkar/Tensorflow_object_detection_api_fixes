# Tensorflow_object_detection_api_fixes

Fix files for issues commonly experienced with tensorflow object detection api


generate_tfrecord.py
for those that experience issues with generate_tfrecord error:
child index pit pf range int(member[4][0].text)
![image](https://user-images.githubusercontent.com/49776926/126252699-5f1985fd-7015-42f7-853a-531c2fba49cf.png)


### Error
https://exerror.com/importerror-cannot-import-name-invalidschemecombination-from-pip-_internal-exceptions/
![image](https://user-images.githubusercontent.com/49776926/127997537-5e8135a9-7056-479f-9688-1eec47284ba1.png)
1. pip uninstall h5py
2. pip install h5py==2.10.0

### Unable to detect gpu
![image](https://user-images.githubusercontent.com/49776926/128021513-69448a71-a4b4-40ca-b672-c0bdce659630.png)
reinstall 

"""
git clone https://github.com/tensorflow/models.git
copy object_detection\packages\tf2\setup.py .
python -m pip install .
"""

## Evaluation
https://www.youtube.com/watch?v=oqXDdxF_Wuw
