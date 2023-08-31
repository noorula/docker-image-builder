import os
import shutil
import argparse
 
def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dockerfile', type=str, default="")
    parser.add_argument('--docker-tag', type=str, default="")
    parser.add_argument('--repository', type=str, default="")
    #parser.add_argument('--awsregion', type=str, default="")
    return parser.parse_args()

def check_input():
    if os.path.isfile('/valohai/inputs/dockerfileinput/Dockerfile'):
        return True
    else:
        return False
    
def main():
    # Check if the Dockerfile was provided as an input and copy it to the working directory.
    if check_input():
        print("Dockerfile provided as an input.")
        shutil.copy('/valohai/inputs/dockerfileinput/Dockerfile', '/valohai/repository/Dockerfile')
    else:
        # Read the contents from the dockerfile parameter
        # and write them into Dockerfile
        args = parse_args()

        if args.dockerfile:
            print("Dockerfile contents provided as a parameter.")
            f = open("/valohai/repository/Dockerfile", "a")
            f.write(args.dockerfile)
            f.close()
        else:
            print("Please provide the Dockerfile contents as a parameter or the actual file as an input.") 

if __name__ == '__main__':
    main()