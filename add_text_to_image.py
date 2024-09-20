from PIL import Image, ImageDraw, ImageFont

def add_text_to_image(input_path, output_path, text, position):
    image = Image.open(input_path)
    draw = ImageDraw.Draw(image)
    font = ImageFont.load_default()
    draw.text(position, text, font=font, fill="white")
    image.save(output_path)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'image_with_text.jpg'
    text = 'Hello, World!'
    position = (50, 50)  # (x, y)
    add_text_to_image(input_path, output_path, text, position)