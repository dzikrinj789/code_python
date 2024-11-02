import os
import gpxpy
import geojson

# Specify the input and output directory paths
input_directory = r'C:\Users\dzikr\Documents\SELF DEVELOPMENT\Day 2'
output_directory = r'C:\Users\dzikr\Documents\SELF DEVELOPMENT\Day 2\geojson_files'

# Ensure the output directory exists
os.makedirs(output_directory, exist_ok=True)

# Function to convert a single GPX file to GeoJSON format
def gpx_to_geojson(gpx_file_path):
    # Open and parse the GPX file
    with open(gpx_file_path, 'r') as gpx_file:
        gpx = gpxpy.parse(gpx_file)

    # Prepare GeoJSON features
    features = []
    for track in gpx.tracks:
        for segment in track.segments:
            coordinates = [[point.longitude, point.latitude] for point in segment.points]
            line_string = geojson.LineString(coordinates)
            features.append(geojson.Feature(geometry=line_string))

    # Create a GeoJSON FeatureCollection
    return geojson.FeatureCollection(features)

# Process each GPX file in the input directory
for filename in os.listdir(input_directory):
    if filename.endswith('.gpx'):
        gpx_file_path = os.path.join(input_directory, filename)
        
        # Convert GPX to GeoJSON
        geojson_data = gpx_to_geojson(gpx_file_path)

        # Save GeoJSON file
        output_file_path = os.path.join(output_directory, filename.replace('.gpx', '.geojson'))
        with open(output_file_path, 'w') as geojson_file:
            geojson.dump(geojson_data, geojson_file, indent=2)

        print(f"Converted {filename} to {output_file_path}")
