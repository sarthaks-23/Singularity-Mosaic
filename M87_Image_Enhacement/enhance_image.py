import numpy as np
from scipy.ndimage import gaussian_filter, median_filter

def gain_calibrate(vis, g_amp, g_phase):
    # V_obs = g1 * V_true * conj(g2)
    corrected_vis = vis / (g_amp * np.exp(1j * g_phase))
    return corrected_vis

def clean_algorithm(dirty_image, psf, threshold=0.01, max_iter=100):
    # Simple CLEAN loop (conceptual)
    model = np.zeros_like(dirty_image)
    res = dirty_image.copy()
    for _ in range(max_iter):
        peak = np.max(np.abs(res))
        if peak < threshold:
            break
        y, x = np.unravel_index(np.argmax(np.abs(res)), res.shape)
        model[y, x] += peak
        res -= peak * psf  # Assumes centered PSF
    return model + res  # Restored image

def apply_weighting(visibilities, weights):
    return visibilities * weights

def post_process(image, method="gaussian"):
    if method == "gaussian":
        return gaussian_filter(image, sigma=1)
    elif method == "median":
        return median_filter(image, size=3)
    else:
        return image

# Dummy usage
if __name__ == "__main__":
    fake_image = np.random.randn(256, 256)
    smoothed = post_process(fake_image, "gaussian")
