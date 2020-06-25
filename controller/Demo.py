from controller.record_module import *
from controller.username import *
import os


# print("Press enter to record")
# record_audio()
# print("done!!!")

# print("recognizing.........")
# print("Hello: " + test1())

for root, dirs, files in os.walk("../test_data"):
    numberFile = 0
    trueFile = 0
    for filename in files:
        # print(test1("../test_data/" + filename))
        numberFile += 1
        if(filename.startswith(test1("../test_data/" + filename))):
            trueFile += 1

print("Rate: " + str(100*trueFile/numberFile) +"%")


