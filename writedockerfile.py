import os
import shutil
import argparse
 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dockerfile', type=str, default="")
    parser.add_argument('--image-name', type=str, default="")
    parser.add_argument('--docker-tag', type=str, default="")
    parser.add_argument('--repository', type=str, default="")
    return parser.parse_args()

def check_input():

    if os.path.isfile('/valohai/inputs/dockerfile/Dockerfile'):
        return True
    else:
        return False
    
def main():

    if check_input():
        print("Dockerfile provided as an input.")
        shutil.copy('/valohai/inputs/dockerfile/Dockerfile', '/valohai/repository/Dockerfile')
    else:
        # Reading Dockerfile contents from the parameter
        args = parse_args()
 
        #contents = valohai.parameters('dockerfile').value

        if args.dockerfile:
            print("Dockerfile contents provided as a parameter.")
            f = open("Dockerfile", "a")
            f.write(args.dockerfile)
            f.close()
        else:
            print("Please provide the Dockerfile contents as a parameter or the actual file as an input.") 

main()