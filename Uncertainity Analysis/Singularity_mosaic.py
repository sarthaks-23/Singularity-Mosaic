def main():
    print("M87 Bayesian Uncertainty Quantification (GPU Accelerated, Batched)")
    fits_image_file = '/kaggle/input/fits-file/M87_final_image.fits'
    uvfits_file = '/kaggle/input/uvfits-files/UVFITSFiles/M87_combined_distinct.uvfits'
    target_size = (128, 128)  # Downsampled image size
    batch_size = 1000       # Batch size for visibilities

    print("1. Loading data...")
    image, pixel_scale = load_fits_image(fits_image_file, target_size=target_size)
    u_coords, v_coords, vis_data = load_uvfits_visibilities(uvfits_file)
    if image is None or vis_data is None:
        return None

    print("2. Estimating noise...")
    noise_std = cp.std(vis_data.real) + cp.std(vis_data.imag)
    print(f"noise_std = {noise_std}")

    print("3. Preparing initial image...")
    init_image = cp.abs(image) + 1e-6

    print("4. Running MCMC...")
    samples = metropolis_sampler(
        init_image, vis_data, u_coords, v_coords, pixel_scale, noise_std = noise_std,
        n_samples=100, proposal_std=0.005, l1w_weight=0.1, tv_weight=0.01, burn_in=20, batch_size=batch_size
    )

    print("5. Computing statistics...")
    mean_image = cp.mean(samples, axis=0)
    std_image = cp.std(samples, axis=0)
    lower_ci = cp.percentile(samples, 2.5, axis=0)
    upper_ci = cp.percentile(samples, 97.5, axis=0)

    # Convert back to NumPy for saving/plotting
    mean_image_np = cp.asnumpy(mean_image)
    std_image_np = cp.asnumpy(std_image)
    lower_ci_np = cp.asnumpy(lower_ci)
    upper_ci_np = cp.asnumpy(upper_ci)

    print("6. Saving results...")
    fits.writeto('/kaggle/working/M87_MCMC_mean_fixed.fits', mean_image_np.astype('float32'), overwrite=True)
    fits.writeto('/kaggle/working/M87_MCMC_uncertainty_fixed.fits', std_image_np.astype('float32'), overwrite=True)
    fits.writeto('/kaggle/working/M87_MCMC_lower_ci_fixed.fits', lower_ci_np.astype('float32'), overwrite=True)
    fits.writeto('/kaggle/working/M87_MCMC_upper_ci_fixed.fits', upper_ci_np.astype('float32'), overwrite=True)

    print("7. Plotting...")
    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    im1 = axes[0,0].imshow(mean_image_np, cmap='hot', origin='lower')
    axes[0,0].set_title('Posterior Mean Image')
    plt.colorbar(im1, ax=axes[0,0])
    im2 = axes[0,1].imshow(std_image_np, cmap='viridis', origin='lower')
    axes[0,1].set_title('Uncertainty')
    plt.colorbar(im2, ax=axes[0,1])
    interval_width = upper_ci_np - lower_ci_np
    im3 = axes[1,0].imshow(interval_width, cmap='plasma', origin='lower')
    axes[1,0].set_title('95% CI Width')
    plt.colorbar(im3, ax=axes[1,0])
    snr = mean_image_np / (std_image_np + 1e-10)
    im4 = axes[1,1].imshow(snr, cmap='coolwarm', origin='lower')
    axes[1,1].set_title('SNR')
    plt.colorbar(im4, ax=axes[1,1])
    plt.tight_layout()
    plt.savefig('M87_MCMC_uncertainty_fixed.png', dpi=200)
    plt.show()

    print("Analysis complete. Results saved.")

    # 8. Compare with original image
    print("8. Comparing with original image (MSE)...")
    orig_image_resized = resize_image(cp.asarray(image), target_size)
    orig_image_np = cp.asnumpy(orig_image_resized)
    mse = np.mean((orig_image_np - mean_image_np) ** 2)
    print(f"\nMSE between original FITS image and posterior mean: {mse:.6e}")

    return {
        'samples': samples,
        'mean_image': mean_image_np,
        'std_image': std_image_np,
        'lower_ci': lower_ci_np,
        'upper_ci': upper_ci_np,
        'snr_image': snr
    }


if __name__ == '__main__':
    results = main()