from astropy.io import fits
import numpy as np

def load_image(path):
    return fits.getdata(path).squeeze()

def evaluate_resolution(freq_hz, diameter_m):
    # Angular resolution (radians) = λ / D
    c = 3e8
    wavelength = c / freq_hz
    return wavelength / diameter_m

def local_rms(image, box):
    x1, y1, x2, y2 = box
    region = image[y1:y2, x1:x2]
    return np.std(region)

def dynamic_range(image, box):
    x1, y1, x2, y2 = box
    region = image[y1:y2, x1:x2]
    return np.max(region) / np.std(region)

# Example usage
if __name__ == "__main__":
    img = load_image("M87_final_image.fits")
    print("Resolution (optical, 500nm, 1m):", evaluate_resolution(6e14, 1), "rad")
    print("Local RMS (100–200 box):", local_rms(img, (100,100,200,200)))
    print("Dynamic Range:", dynamic_range(img, (100,100,200,200)))
