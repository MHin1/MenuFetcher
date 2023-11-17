import subprocess
import os

# Full path to the ImageMagick convert executable
magick_path = r'D:\Pythoni\ImageMagick-7.1.1-21-portable-Q16-x64\magick.exe'  # Replace with your actual path

# Input directory containing .txt files
input_dir = r"D:\Menus"

# Output directory for .png files
output_dir = r"D:\Menus\Menu Pictures"

# Ensure the output directory exists
os.makedirs(output_dir, exist_ok=True)

# Loop through .txt files in the input directory
for txt_file in os.listdir(input_dir):
    if txt_file.endswith('.txt'):
        # Construct the input file path
        input_file = os.path.join(input_dir, txt_file)

        # Construct the output file path with the same name as the input file
        output_file = os.path.join(output_dir, os.path.splitext(txt_file)[0] + '.png')

        # ImageMagick command to convert .txt to .png using the full path to magick
        cmd = [
            magick_path,
            'convert',
            '-size', '1080x1440',
            '-background', 'white',
            '-fill', 'black',
            '-font', r'D:\Menus\Fonts\arial.ttf',  # Specify the full path to arial.ttf
            '-pointsize', '40',  # Set the font size to 12
            f'label:@{input_file}',
            output_file
        ]

        # Run the ImageMagick command
        subprocess.run(cmd, shell=True)

print("Conversion complete. PNG files saved in the output directory with the same names as the input files.")

# Open the output directory in the file explorer
subprocess.Popen(['explorer', output_dir])
