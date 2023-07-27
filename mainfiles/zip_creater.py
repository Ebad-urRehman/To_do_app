import pathlib
import zipfile
# zipfile is library name and Zipfile is function name
# in zipfile library we give path as ('path' + '\' + 'filename.zip'
# pathlib is another library with the hellp of which we give paths as (path,filename.zip)
# pathlib is intellignent to know what to use / or \ in file paths
def make_archive(filepaths_arg,dest_folder):
    dest_path_with_name = pathlib.Path(dest_folder, "compressfile.zip")
    with zipfile.ZipFile(dest_path_with_name, "w") as archive:
        for filepath in filepaths_arg:
            filepath = pathlib.Path(filepath)
            # above line make filepath special type of object called PosixPath
            # and filepath.name (Posix path object) extracts only name of that path
            # in summary for every file the directory change to main directory means files only compressed alone not
            # with directories till username
            archive.write(filepath, arcname = filepath.name)


# test
if __name__ == "__main__":
    make_archive(filepaths_arg=["6_main.py", "1_main.py"], dest_folder="zip_folder")