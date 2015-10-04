import sys, os, thread, time
sys.path.append("../../")                            # Append path to Leap SDK
output = file("./datasets/learndata.dat", 'a')      # Define an output file
import Leap                                         # Import Leap library

def main():
    controller = Leap.Controller()      # Make a Leap Controller object
    letter = raw_input("Gimme a letter: ")
    for i in range (0, 200):
        try:
            time.sleep(0.005)
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
                for ele in data_list+[letter]:
                    output.write(str(ele)+" ")
                output.write("\n")

        except KeyboardInterrupt:
            output.close()
            return
main()
