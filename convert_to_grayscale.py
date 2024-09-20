from PIL import Image

def convert_to_grayscale(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert('L')
    grayscale_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'grayscale_image.jpg'
    convert_to_grayscale(input_path, output_path)