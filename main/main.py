import load
import map3d
import argparse
import pandas as pd

# Hyunjae Lee , Sungjae Min is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''

# MAIN
if __name__ == "__main__":

    # Parsing arguments
    parser = argparse.ArgumentParser(
        description='This is simple User Data-Driven Map Visualization program.', prog='VAMAP')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    parser.add_argument('files', metavar='Ref', type=argparse.FileType('r'), nargs='?',
                        help='a reference excel file to be decided by you')
    # we need an argument for 'Coverage'

    args = parser.parse_args()

    # Default map view
    Map_Object = folium.Map(location=[37.566345, 126.977893], zoom_start=17)

    # Global tooltip
    tooltip = 'Click For More Info'

    # Load custom marker icon

    # Load default markers (roads, buildings, subways)

    # Load default circlemarker based on user input (coverage)

    # Load value markers (calculated by 'scroing')

    # Save as html file
    Map_Object.save('MAP.html')
