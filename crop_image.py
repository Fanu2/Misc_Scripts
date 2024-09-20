from PIL import Image

def crop_image(input_path, output_path, crop_rectangle):
    image = Image.open(input_path)
    cropped_image = image.crop(crop_rectangle)
    cropped_image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'cropped_image.jpg'
    crop_rectangle = (100, 100, 400, 400)  # (left, upper, right, lower)
    crop_image(input_path, output_path, crop_rectangle)