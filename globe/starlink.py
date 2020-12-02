import ephem
import datetime
from ephem import degree
import requests
import json

def getCoordinates(name, line1, line2):
	tle_rec = ephem.readtle(name, line1, line2);
	tle_rec.compute();
	lng = tle_rec.sublong / degree;
	lat = tle_rec.sublat / degree;
	return lng, lat

# response = requests.get('https://www.celestrak.com/NORAD/elements/starlink.txt')
# # print(response.text)
# f = open("starlink.txt", "w")
# for line in response.text:
# 	f.write(line)

# f.close()
# write_file = open("locations.json", "w")
f = open("starlink.txt", "r")
lines = f.readlines()
array_latlong = []
count = 0
length = int((len(lines)/3)-1)
for count in range(length):
	lng, lat = getCoordinates(lines[(count*3)], lines[(count*3)+1], lines[(count*3)+2])
	coord_dict = {"latitude": lat, "longitude": lng}
	array_latlong.append(coord_dict)
	count +=1

# array_latlong = '\n'.join(array_latlong)
	# array_latlong.append(json.dumps(coord_dict))
	# write_file.write(json.dumps(coord_dict))
with open("locations.json", "w") as write_file:
	json.dump(array_latlong, write_file)

# with open("locations.json", "w") as write_file:
# 	write_file.write(json.loads(array_latlong))

f.close()
# writ = open("locations.json", "w")
# writ.write((array_latlong))
# f.close()
# writ.close()

# print(lines[1])
# for line in lines:
# 	name = line

# json_data = json.loads(response.text)
# print(json_data)

# name = "STARLINK-24";
# line1 = "1 44238U 19029D   20283.54677831  .00002873  00000-0  17462-3 0  9991";
# line2 = "2 44238  52.9973  50.9457 0001721 105.4156 254.7026 15.13630451 74759";




# tle_rec = ephem.readtle(name, line1, line2);
# tle_rec.compute();

# print('Long : ', tle_rec.sublong / degree);
# print('Lat : ', tle_rec.sublat / degree);