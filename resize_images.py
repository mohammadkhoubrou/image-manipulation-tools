import os
from PIL import Image


def resize(saving_directory, location, sizes, crop=None):
    # create the saving location if it doesn't exist
    os.makedirs(saving_directory, exist_ok=True)
    for file in os.listdir(location):
        if file.endswith((".jpg", ".png")):
            # join the file names with the names of directories so that you can operate on them
            location_files = os.path.join(location, file)
            saving_location = os.path.join(saving_directory, file)

            # load image
            image = Image.open(location_files)
            if crop is not None:
                # crop image
                cropped = image.crop(crop)
                # resize image
                result = cropped.resize(sizes)

                # save result
                result.save(saving_location)
                print(f"file {file} resized & cropped & saved!")
            else:
                # resize image
                result = image.resize(sizes)
                # save result
                result.save(saving_location)
                print(f"file {file} resized & saved!")
        print(f"directory files, resized and saved to: {saving_directory}")

