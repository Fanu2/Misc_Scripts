from PIL import Image

def overlay_image(background_path, overlay_path, output_path, position):
    background = Image.open(background_path)
    overlay = Image.open(overlay_path)
    background.paste(overlay, position, overlay)
    background.save(output_path)

if __name__ == "__main__":
    background_path = 'background_image.jpg'
    overlay_path = 'overlay_image.png'
    output_path = 'image_with_overlay.jpg'
    position = (50, 50)  # (x, y)
    overlay_image(background_path, overlay_path, output_path, position)