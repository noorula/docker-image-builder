import os
import shutil
import argparse
 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dockerfile', type=str, default="")
    return parser.parse_args()

# Check if the Dockerfile was provided as an input.
def check_input():
    if os.path.isfile('/valohai/inputs/dockerfileinput/Dockerfile'):
        return True
    else:
        return False
    
def main():
    # Check if the Dockerfile was provided as an input or 
    # build it based on a dockerfile parameter.
    if check_input():
        print("Dockerfile provided as an input.")
        shutil.copy('/valohai/inputs/dockerfileinput/Dockerfile', '/valohai/repository/Dockerfile')
    else:
        # Read the contents from the dockerfile parameter
        # and write them into Dockerfile
        args = parse_args()

        if args.dockerfile:
            print("Dockerfile contents provided as a parameter.")
            f = open("/valohai/repository/Dockerfile", "w+")
            f.write(args.dockerfile)
            f.close()
        else:
            print("Please provide the Dockerfile contents as a parameter or the actual file as an input.") 

if __name__ == '__main__':
    main()