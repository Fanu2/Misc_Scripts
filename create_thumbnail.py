from PIL import Image

def create_thumbnail(input_path, output_path, size):
    image = Image.open(input_path)
    image.thumbnail(size)
    image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'thumbnail_image.jpg'
    size = (128, 128)
    create_thumbnail(input_path, output_path, size)