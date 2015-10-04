import sys, os, thread, time
sys.path.append("./lib")                            # Append path to Leap SDK
output = file("./datasets/learndata.dat", 'a')      # Define an output file
import Leap                                         # Import Leap library
from sklearn.externals import joblib
from sklearn import svm, datasets
import numpy as np
from collections import Counter
neigh = joblib.load('model.pkl')
translate = {101:"a", 102:"b", 103:"c", 104:"d", 105:"e", 106:"f", 107:"g",
108:"h", 109:"i", 110:"j", 111:"k", 112:"l", 113:"m", 114:"n", 115:"o",
116:"p", 117:"q", 118:"r", 119:"s", 120:"t", 121:"u", 122:"v", 123:"w",
124:"x", 125:"y", 126:"z"};

def main():
    controller = Leap.Controller()      # Make a Leap Controller object
    counter = 0;
    while True:
        letter = ""
        time.sleep(0.02)
        try:
            frame = controller.frame()
            data_list = []
            if len(frame.hands)==1:

                hand = frame.hands[0]
                hand_x_basis = hand.basis.x_basis
                hand_y_basis = hand.basis.y_basis
                hand_z_basis = hand.basis.z_basis
                hand_origin = hand.palm_position
                hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
                hand_transform = hand_transform.rigid_inverse()
                for finger in hand.fingers:
                    transformed_position = hand_transform.transform_point(finger.tip_position)
                    transformed_direction = hand_transform.transform_direction(finger.direction)
                    for b in range(0, 4):
                        bone = finger.bone(b)
                        transformed_joint_position = hand_transform.transform_point(bone.prev_joint)
                        transform_bone_direction = hand_transform.transform_point(bone.direction)
                        data_list.append(transformed_joint_position[0])
                        data_list.append(transformed_joint_position[1])
                        data_list.append(transformed_joint_position[2])
                        data_list.append(transform_bone_direction[0])
                        data_list.append(transform_bone_direction[1])
                        data_list.append(transform_bone_direction[2])
                data_list.append(transformed_position[0])
                data_list.append(transformed_position[1])
                data_list.append(transformed_position[2])
                data_list.append(transformed_direction[0])
                data_list.append(transformed_direction[1])
                data_list.append(transformed_direction[2])
                data_list.append(hand.palm_normal[0])
                data_list.append(hand.palm_normal[1])
                data_list.append(hand.palm_normal[2])
                data_list.append(hand.direction[0])
                data_list.append(hand.direction[1])
                data_list.append(hand.direction[2])

                test = np.transpose(data_list);
                results_Array =  neigh.predict(test)
                for ele in data_list+[letter]:
                    output.write(str(ele)+" ")
                output.write("\n")

                results = []
                for i in range (0,len(results_Array)):
                    results.append(translate[results_Array[i]])

                counter = counter + 1
                if (counter == 25):
                    data = Counter(results)
                    print [(i[0]) for i in data.most_common(1)][0]

                    counter = 0

        except KeyboardInterrupt:
            output.close()
            return
main()
