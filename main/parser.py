import argparse

# Sungjae Min is in charge

''' 
<How to work>

<Usage> 
 Input example  :
 Output example :

'''


def Parser():
    # Parsing arguments
    parser = argparse.ArgumentParser(
        description='This is simple User Data-Driven Map Visualization program.', prog='VAMAP')
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')
    # we need an argument for 'Coverage'

    # [Plan]
    # parser.add_argument('files', metavar='Ref', type=argparse.FileType('r'), nargs='?',
    #                     help='a reference excel file to be decided by you')

    # Version
    parser.add_argument('--version', action='version', version='%(prog)s 1.0')

    # Read Setup.txt
    f = open("C:/Users/user/Documents/GitHub/Team16_Development/Setup.txt", 'r')

    lines = f.readlines()

    # Tokenizing lines by '='
    arr1 = lines[0].split('=')
    arr2 = lines[1].split('=')
    arr3 = lines[2].split('=')
    arr4 = lines[3].split('=')

    # Split view coordinate
    arr5 = arr4[1].split('/')

    # Save value
    Base_dir = arr1[1]
    User_file = arr2[1]
    Coverage = arr3[1]

    View_coordinate_default1 = arr5[0]
    View_coordinate_default2 = arr5[1]
    View_coordinate_default3 = arr5[2]
    View_coordinate_default4 = arr5[3]

    '''
    print(Base_dir)
    print(User_file)
    print(Coverage)
    print(View_coordinate_default1)
    print(View_coordinate_default2)
    print(View_coordinate_default3)
    print(View_coordinate_default4)
    '''

    f.close()
    args = parser.parse_args()
