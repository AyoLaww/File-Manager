import os 
import shutil


img_ends = ['.png', '.jpg', '.JPG']
document_ends = ['.txt', '.pdf', '.docx']
executable_ends = ['.exe']
torrent_ends = ['.torrent']
rar_ends = ['.rar', '.zip']

source_dir = "C:\\Users\HP\Downloads"
image_dir = "C:\\Users\HP\Downloads\images"
document_dir = "C:\\Users\HP\Downloads\documents"
executables_dir = "C:\\Users\HP\Downloads\executables"
torrents_dir = "C:\\Users\HP\Downloads\Torrents"
rars_dir = "C:\\Users\HP\Downloads\Rars"

scan = os.listdir(source_dir)



def FileManager():
    for x in scan:
        full_path = os.path.join(source_dir, x)

        if full_path.endswith(tuple(img_ends)):
            shutil.move(full_path, os.path.join(image_dir, x))

        elif full_path.endswith(tuple(document_ends)):
            shutil.move(full_path, os.path.join(document_dir, x))

        elif full_path.endswith(tuple(executable_ends)):
            shutil.move(full_path, os.path.join(executables_dir, x))

        elif full_path.endswith(tuple(torrent_ends)):
            shutil.move(full_path, os.path.join(torrents_dir, x))

        elif full_path.endswith(tuple(rar_ends)):
            shutil.move(full_path, os.path.join(rars_dir, x))

        else:
            print("No file location for this file")

        break

FileManager()
