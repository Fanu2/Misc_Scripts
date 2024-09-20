import cv2

def detect_edges(input_path, output_path):
    image = cv2.imread(input_path, 0)
    edges = cv2.Canny(image, 100, 200)
    cv2.imwrite(output_path, edges)

if __name__ == "__main__":
    input_path = 'input_image.jpg'
    output_path = 'edges_image.jpg'
    detect_edges(input_path, output_path)