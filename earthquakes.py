'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''



import json

def main():
   infile = open('eq_data.json', 'r')

   earthquakes = json.load(infile)
   min_magnitude = 6

   eq_dict = {}
   quake_info = earthquakes["features"]
   for quake_info in quake_info:
      magnitude = quake_info['properties']['mag']
      if magnitude > min_magnitude:
         eq_dict['Magnitude'] = quake_info['properties']['mag']
         eq_dict['Location'] = quake_info['properties']['place']
         eq_dict['Latitude'] = quake_info['geometry']['coordinates'][1]
         eq_dict['Longitude'] = quake_info['geometry']['coordinates'][0]
         print(f"Location: {eq_dict['Location']}")
         print(f"Magnitude: {eq_dict['Magnitude']}")
         print(f"Longitude: {eq_dict['Longitude']}")
         print(f"Latitude: {eq_dict['Latitude']}")
         print('\n'*2)
         
if __name__ == '__main__':
   main()