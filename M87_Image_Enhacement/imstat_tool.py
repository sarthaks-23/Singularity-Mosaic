import numpy as np
from astropy.io import fits

def imstat(image_path, box=None):
    data = fits.getdata(image_path).squeeze()
    if box:
        x1, y1, x2, y2 = box
        data = data[y1:y2, x1:x2]
    
    valid = data[np.isfinite(data)]
    return {
        "mean": np.mean(valid),
        "median": np.median(valid),
        "sigma": np.std(valid),
        "rms": np.sqrt(np.mean(valid**2)),
        "min": np.min(valid),
        "max": np.max(valid),
        "npts": valid.size,
        "sum": np.sum(valid)
    }

# Example
if __name__ == "__main__":
    stats = imstat("M87_final_image.fits", box=(100, 100, 200, 200))
    for k, v in stats.items():
        print(f"{k}: {v}")
