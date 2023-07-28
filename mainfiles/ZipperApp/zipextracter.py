import zipfile

def extract_archive(archive_path_arg, dest_dir_arg):
    with zipfile.ZipFile(archive_path_arg, "r") as archive_file:
        archive_file.extractall(dest_dir_arg)


if __name__ == "__main__":
    extract_archive("/mainfiles/compressfile.zip", "C:\\Users\\infall\\PycharmProjects\\pythonProject1\\mainfiles\\zip_folder")