from PIL import Image, ImageFilter

def blur_image(input_path, output_path):
    image = Image.open(input_path)
    blurred_image = image.filter(ImageFilter.BLUR)
    blurred_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'blurred_image.jpg'
    blur_image(input_path, output_path)