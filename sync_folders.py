import os
import shutil
import hashlib
import argparse
import time


# To get arguments in the command line
def get_args():
    parser = argparse.ArgumentParser(description='Synchronize two folders')
    parser.add_argument('source_folder', help='path to the source folder')
    parser.add_argument('replica_folder', help='path to the replica folder')
    parser.add_argument('interval', type=int, help='synchronization interval in seconds')
    parser.add_argument('log_file', help='path to the log file')
    return parser.parse_args()


# To calculate the MD5 hash of a file
def get_file_hash(path):
    hash_md5 = hashlib.md5()
    with open(path, 'rb') as f:
        for chunk in iter(lambda: f.read(4096), b""):
            hash_md5.update(chunk)
    return hash_md5.hexdigest()


# Process and check if the folders are in sync
def synchronize_folders(source_folder, replica_folder, log_file):
    # Loop to process each file in the source folder
    for root, dirs, files in os.walk(source_folder):
        for file_name in files:
            source_path = os.path.join(root, file_name)
            replica_path = source_path.replace(source_folder, replica_folder)
            if not os.path.exists(replica_path) or get_file_hash(source_path) != get_file_hash(replica_path):
                shutil.copy2(source_path, replica_path)
                log_file.write(f'Copied {source_path} to {replica_path}\n')
                print(f'Copied {source_path} to {replica_path}')
    # Loop to process each file in the replica folder
    for root, dirs, files in os.walk(replica_folder):
        for file_name in files:
            replica_path = os.path.join(root, file_name)
            source_path = replica_path.replace(replica_folder, source_folder)
            if not os.path.exists(source_path):
                os.remove(replica_path)
                log_file.write(f'Removed {replica_path}\n')
                print(f'Removed {replica_path}')
                

if __name__ == '__main__':
    args = get_args()
    with open(args.log_file, 'a') as log_file:
        while True:
            synchronize_folders(args.source_folder, args.replica_folder, log_file)
            time.sleep(args.interval)
