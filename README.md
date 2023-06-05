# Synchronize-Folders

A python program that synchronizes two folders: source and replica. It maintains a full, identical copy of source folder at replica folder.

The synchronization is done periodically without using third party libraries that implement folder synchronization.
The file creation/copying/ removal operations are logged to a file and a console output.  

The python file should be run using the command line where the arguments are given for the source folder path, replica folder path, time interval and log file path.


Example:

python sync_folders.py D:\source D:\replica 5 D:\log_file.log


# Helper functions

The program has 3 helper methods: 


1. get_args() : This helper method uses the ArgumentParser to get the necessary arguments like source folder path, replica folder path, time interval and log file path from the command line. argparse library is used in this method.


2. get_file_hash(path): This method calculates the MD5 hash of a file using hashlib library. This in turn is used to check whether any changes have been made to a file by validating the hash of the file in source and replica folders. The path of the file is given as argument.


3. synchronize_folders(source_folder, replica_folder, log_file) : This method loops through each file in the source and replica folder to process them and check if any changes have made in the source folder and make the necessary changes in the replica folder along with log details. The path to the sorce, replica and log file have been passed as arguments.
