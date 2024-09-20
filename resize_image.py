from PIL import Image

def resize_image(input_path, output_path, size):
    image = Image.open(input_path)
    resized_image = image.resize(size)
    resized_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'resized_image.jpg'
    size = (800, 600)  # Width, Height
    resize_image(input_path, output_path, size)