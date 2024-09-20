from PIL import Image

def rotate_image(input_path, output_path, angle):
    image = Image.open(input_path)
    rotated_image = image.rotate(angle)
    rotated_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'rotated_image.jpg'
    angle = 45  # degrees
    rotate_image(input_path, output_path, angle)