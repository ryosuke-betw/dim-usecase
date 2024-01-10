import subprocess
import os
import glob
import pandas as pd
import difflib
import urllib.request
import zipfile
import tempfile
import shutil
from datetime import datetime

# Open Data Installation
def dim_install():
    print("Open Data Installation")
    install_command = ["dim","install"]
    subprocess.run(install_command, capture_output=True, text=True)


def install_opendata(url, name):
    print(f"Open Data Installation({name})")
    install_command = ["dim", "install", url, "-n", name, "-p", "unzip"]
    subprocess.run(install_command, capture_output=True, text=True)


# Download Comparison Folder
def download_comparison_folder(url, target_folder, folder_name):
    # Create temporary zip storage directory
    zip_file_folder = tempfile.mkdtemp()
    try:
        # Download zip file
        zip_file_path = os.path.join(zip_file_folder, f"{folder_name}.zip")
        urllib.request.urlretrieve(url, zip_file_path)

        # Extract the zip file
        extracted_folder = os.path.join(zip_file_folder, folder_name)
        with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
            zip_ref.extractall(extracted_folder)

        # Delete folders if they exist in the destination directory
        target_folder_path = os.path.join(target_folder, folder_name)
        if os.path.exists(target_folder_path):
            shutil.rmtree(target_folder_path)

        # Copy the extracted folder to the destination directory
        shutil.copytree(extracted_folder, target_folder_path)
        print(f"Folder '{folder_name}' downloaded to: {target_folder_path}")

    finally:
        # Delete temporary zip storage directory
        os.remove(zip_file_path)
        shutil.rmtree(zip_file_folder)


# Update Data
def update_data():
    print("\n ========== Update Data ==========\n")
    # User input
    user_input = input("Do you want to update all data, update specific data, or skip the update? "
                       "(Type 'all', 'specific', or 'skip'): ").strip().lower()
    if user_input == 'all':
        # Update all data
        update_all()
    elif user_input == 'specific':
        # Update specific data
        name = input("Enter the name of the specific data to update: ").strip()
        update_specified_folder(name)
    elif user_input == 'skip':
        # Update skipped
        print("Data update skipped.")
    else:
        # Invalid imput
        print("Invalid input. Please enter 'all', 'specific', or 'skip'.")


# All open data updates
def update_all():
    print("\n ========== Update All data ==========\n")
    all_update_cmd = ["dim", "update"]
    res = subprocess.run(all_update_cmd, capture_output=True, text=True)
    print(res.stdout)


# Specific open data updates
def update_specified_folder(name):
    print(f"\n ========== Update Specific Data: {name} ==========\n")
    specified_update_cmd = ["dim", "update", name]
    res = subprocess.run(specified_update_cmd, capture_output=True, text=True)
    print(res.stdout)

 
 # Load Existing Data File
def read_existing_data(base_dir):
    # List to accumulate existing data
    existing_files = []
    # Load all existing data
    print("\n Loading Existing Files... \n")
    folders = os.listdir(base_dir)
    for folder in folders:
        dir_path = os.path.join(base_dir, folder)
        if os.path.isdir(dir_path):
            file_list = glob.glob(os.path.join(dir_path, "*.txt"))
            for file_path in file_list:
                existing_file = pd.read_csv(file_path)
                existing_files.append(existing_file)

    return existing_files


# Loading Current File
def read_current_data(base_dir):
    current_files = [] # List to accumulate updated data
    file_names = [] # List to get file names
    print("\n Loading Current Files... \n")
    folders = os.listdir(base_dir)
    for folder in folders:
        dir_path = os.path.join(base_dir, folder)
        if os.path.isdir(dir_path):
            file_list = glob.glob(os.path.join(dir_path, "*.txt"))
            for file_path in file_list:
                current_file = pd.read_csv(file_path)
                current_files.append(current_file)
                file_names.append((folder, os.path.basename(file_path)))
    return current_files, file_names


# Show Data Difference
def show_data_diff(file_names, existing_files, current_files):
    print("\n Create HTML Output... \n")
    # Get the current date and time
    '''
    current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    html_output = "<html><head></head><body>\n"
    html_output += f"<p>HTML File Created: {current_datetime}</p>\n"
    html_output += "\n========== Data Difference ==========\n"
    '''
    for (folder_name, file_name), existing_file, current_file in zip(file_names, existing_files, current_files):
        if not existing_file.equals(current_file):
            ###html_output += f"<p>Folder:{folder_name}, File:{file_name}</p>"
            print(f"Folder:{folder_name}, File:{file_name}")
            existing_lines = existing_file.to_string().split('\n')
            current_lines = current_file.to_string().split('\n')
            differ = difflib.Differ()
            diff = differ.compare(existing_lines, current_lines)
            for data in diff:
                if data[0:1] in ['+', '-']:
                    print(data)
                    ###html_output += f"<p>{data}</p>"
    '''                
    html_output += "</body></html>"
    with open("data_difference_output.html", "w", encoding="utf-8") as html_file:
        html_file.write(html_output)
        subprocess.run(["open", "data_difference_output.html"])
    '''

