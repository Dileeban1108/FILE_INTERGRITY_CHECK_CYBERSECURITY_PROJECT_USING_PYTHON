import os
import hashlib
def calculate_sha256(file_path):
    sha256_hash=hashlib.sha256()
    with open(file_path,'rb') as file:
        while True:
            data=file.read(655366)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

# Checking integrity, in the context of data or files,
# refers to the process of ensuring that the data or files
# have not been altered, tampered with, corrupted, or modified
# in an unauthorized or unintended manner.
def check_intergrity(directory_path):
    if not os.path.exists(directory_path) or not os.path.isdir(directory_path):
        print(f'{directory_path} is not exist')
        return

    for root,dirs,files in os.walk(directory_path):
        for file_name in files:
            file_path=os.path.join(root,file_name)
            calculated_hash=calculate_sha256(file_path)
            print(f'File name: {file_path} \n Hash: {calculated_hash}')


if __name__=="__main__":
    directory_to_check=input("Enter your directory: ")
    check_intergrity(directory_to_check)