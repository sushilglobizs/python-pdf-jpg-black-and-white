import os
from PIL import Image

def convert_to_bw_and_darken(input_folder, output_folder, darken_factor=0.8):
    # Create output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Process each file in the input folder
    for filename in os.listdir(input_folder):
        if filename.endswith(".jpg") or filename.endswith(".jpeg"):
            input_path = os.path.join(input_folder, filename)
            output_path = os.path.join(output_folder, filename)

            # Open the image
            image = Image.open(input_path)

            # Copy DPI information
            dpi = image.info.get("dpi")

            # Convert the image to grayscale (black and white)
            bw_image = image.convert("L")

            # Get the pixel data
            pixel_data = list(bw_image.getdata())

            # Darken the image by reducing the red channel
            darkened_data = [((int(pixel * darken_factor),) * 3) for pixel in pixel_data]

            # Create a new image with the darkened pixel data
            darkened_image = Image.new("RGB", bw_image.size)

            # Copy DPI information to the new image
            darkened_image.info["dpi"] = dpi

            darkened_image.putdata(darkened_data)

            # Save the result
            darkened_image.save(output_path, dpi=dpi)

if __name__ == "__main__":
    input_folder = input("Enter the path to the input folder: ")
    output_folder = input_folder + " bw"

    convert_to_bw_and_darken(input_folder, output_folder)

    print(f"Conversion complete. Black and white images saved in '{output_folder}'.")
