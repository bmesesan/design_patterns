from PIL import Image
import numpy as np
import math

IMG_PATH = "./coding_exercise/lena.jpeg"


def save_jpeg(image, filepath, quality=75):
    img = Image.fromarray(image)
    img.save(filepath, format='JPEG', quality=quality)


def rotate(image: np.ndarray, theta: float) -> np.ndarray:
    # Apply a 90 degree offset to theta
    theta += math.radians(90) 
    
    # Dims of the original image
    h, w = image.shape
    
    # Determine the center coordinates of the original image 
    center_x, center_y = w / 2, h / 2
    
    # Allocate space for the result matrix
    dst_width, dst_height = w, h
    dst_image = np.zeros((dst_height, dst_width), dtype=np.uint8)

    for y in range(dst_height):
        for x in range(dst_width):
            # Apply the center x and the center y as offsets
            x_fixed = x - center_x
            y_fixed = y - center_y
            
            # Apply the rotation matrix in order to find the rotated x' and y'
            # Apply the center x and center y coordinates because the rotation is done with respect to the center
            x_rot = x_fixed * math.cos(theta) + y_fixed * math.sin(theta) + center_x
            y_rot = x_fixed * math.sin(theta) - y_fixed * math.cos(theta) + center_y

            # There might be cases in which the rotated coordinates exceed the resulting dims
            # In this case, those pixels are omitted
            if x_rot < 0 or x_rot >= w - 1 or y_rot < 0 or y_rot >= h - 1:
                continue
            
            # The rotated indices were determined
            x_int, y_int = int(x_rot), int(y_rot)
            
            # Use bilinear interpolation to determine the new pixel value at the destination
            x1, x2 = x_int, x_int + 1
            y1, y2 = y_int, y_int + 1
            
            f_x_y1 = ((x2 - x_rot) / (x2 - x1)) * image[x1, y1] + \
                     ((x_rot - x1) / (x2 - x1)) * image[x2, y1]   
            
            f_x_y2 = ((x2 - x_rot) / (x2 - x1)) * image[x1, y2] + \
                     ((x_rot - x1) / (x2 - x1)) * image[x2, y2]

            f_x_y = ((y2 - y_rot) / (y2 - y1)) * f_x_y1 + \
                    ((y_rot - y1) / (y2 - y1)) * f_x_y2
            
            # Set the pixel value of the destination image
            dst_image[y, x] = int(f_x_y)

    return dst_image


def main():
    # Load the original image and transform it to grayscale
    im = Image.open(IMG_PATH, formats=["JPEG"])
    my_image = np.array(im)
    
    rgb_weights = np.array([0.299, 0.587, 0.114], dtype=np.float32)
    imgf = my_image[..., :3]
    imgf = imgf.astype(np.float32) if imgf.dtype not in [np.float32, np.float64] else imgf
    my_image = np.dot(imgf, rgb_weights).astype(my_image.dtype)
    
    # Test cases: 0 to 360 degree rotation
    for i in range(0, 361, 15):
        out_img_path = f"./coding_exercise/lena_out_{i}.jpeg"
        result_image = rotate(my_image, math.radians(i))
        save_jpeg(result_image, out_img_path)


if __name__ == "__main__":
    main()