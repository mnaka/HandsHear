import sys, os, thread, time
sys.path.append("../")					# Append path to Leap SDK 
output = file("./output2.txt", 'w')		# Define an output file
import Leap								# Import Leap library

def main():
    controller = Leap.Controller()		# Make a Leap Controller object
    letter = ''					
    while True:
        letter = raw_input("Gimme a letter: ")	# Asks for a letter
        if letter == 'XXX':						# Dump in an XXX to quit
            output.close()
            return
        frame = controller.frame()
        data_list = []
        for hand in frame.hands:
            hand_x_basis = hand.basis.x_basis
            hand_y_basis = hand.basis.y_basis
            hand_z_basis = hand.basis.z_basis
            hand_origin = hand.palm_position
            hand_transform = Leap.Matrix(hand_x_basis, hand_y_basis, hand_z_basis, hand_origin)
            hand_transform = hand_transform.rigid_inverse()
            for finger in hand.fingers:
                transformed_position = hand_transform.transform_point(finger.tip_position)
                transformed_direction = hand_transform.transform_direction(finger.direction)
            data_list.append(transformed_position[0])
            data_list.append(transformed_position[1])
            data_list.append(transformed_position[2])
        for ele in data_list+[letter]:
            output.write(str(ele)+" ")
        output.write("\n")

main()


