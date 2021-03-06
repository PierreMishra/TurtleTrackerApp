#-------------------------------------------------------------
# ARGOSTrackingTool.py
#
# Description: Reads in an ARGOS tracking data file and allows
#   the user to view the location of the turtle for a specified
#   date entered via user input.
#
# Author: Pierre Mishra (prashank.mishra@duke.edu)
# Date:   Fall 2020
#--------------------------------------------------------------

# ask user for search data
user_date = input("Enter date to search for Sara [M/D/YYYY]: ")

#create variable pointing to the data file
file_name = './data/raw/Sara.txt'

#create a file object from file
file_object = open(file_name, 'r')

#read contents of file into a list
line_list = file_object.readlines()

#close file
file_object.close()

#create two empty dictionary object
date_dict = {}
coord_dict = {}

#for while loop, read the first line in th file
#lineString = file_object.readline()

#iterate using a while loop
#while loop is much more memory efficient
#while lineString:

# pretend we line one line of data from file
#lineString = '20616	29051	7/3/2003 9:13	3	66	33.898	-77.958	27.369	-46.309	6	0	-126	529	3	401 651134.7	0'
#lineString = line_list[100]

#iterate through all lines in the lineList
for lineString in line_list:
    
    if lineString[0] in ("#","u"):
        #read the next line
        #lineString = file_object.readline()
        continue
    
    #split the string into a list of data items
    lineData = lineString.split()
    
    #extract items in list into variables
    record_id = lineData[0]
    obs_date = lineData[2]
    obs_lc = lineData[4]
    
#    if obs_lc not in ("1", "2", "3"):
#        continue
    obs_lat = lineData[6]
    obs_lon = lineData[7]
    
    #print the location if lc is 1, 2 or 3
    if obs_lc in ("1", "2", "3"):
        #print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {obs_date}")
        date_dict[record_id] = obs_date
        coord_dict[record_id] = (obs_lat, obs_lon)
    
    #read the next line
    #lineString = file_object.readline()
    
#close the file
#file_object.close()

# Create empty list to hold matching keys
matching_keys = []

#Loop through items in the date_Dict and collect keys for mathcing ones
#Database lookup
for date_item in date_dict.items():
    # GEt the kney and date of the dictionary item
    the_key, the_date = date_item
    if the_date == user_date:
        matching_keys.append(the_key)
        
# if no records found, tell the user
if len(matching_keys) == 0:
    print(f"No record found on {user_date}. Is your date format valid?")

# Reveewal locations for each key in matching keys
for matching_key in matching_keys:
    obs_lat, obs_lon = coord_dict[matching_key]
    #obs_date = date_dict[matching_key]
    print(f"Record {record_id} indicates Sara was seen at lat:{obs_lat}, lon:{obs_lon} on {user_date}")
        