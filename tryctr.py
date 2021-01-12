import os
os.system("rosnode kill $(rosnode list) | grep simple_offboard")
# simple_offboard
os.system("rosnode kill $(rosnode list) | grep map_flipped_frame")
# map_flipped_frame
os.system("rosnode kill $(rosnode list) | grep mavros")
# mavros
os.system("rosnode kill $(rosnode list) | grep visualization")
# visualization
os.system("rosnode kill $(rosnode list) | grep nodelet_manager")
# nodelet_manager
os.system("rosnode kill $(rosnode list) | grep rangefinder_frame")
# rangefinder_frame
os.system("rosnode kill $(rosnode list) | grep rosout")
# rosout
os.system("rosnode kill $(rosnode list) | grep master")
# master
