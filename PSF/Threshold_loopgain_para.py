# Get RMS first
imstat('your_dirty_image.residual')

# Different threshold values (affects final cleaned image, not PSF)
tclean(vis='your_data.ms', 
       imagename='clean_threshold_3rms', 
       imsize=512, 
       cell='1arcsec', 
       niter=1000, 
       weighting='briggs', 
       robust=0,
       threshold='0.001Jy')  # Set to ~3x RMS value

# Different loopgain values
tclean(vis='your_data.ms', 
       imagename='clean_loopgain_01', 
       imsize=512, 
       cell='1arcsec', 
       niter=1000, 
       weighting='briggs', 
       robust=0,
       loopgain=0.1)

tclean(vis='your_data.ms', 
       imagename='clean_loopgain_05', 
       imsize=512, 
       cell='1arcsec', 
       niter=1000, 
       weighting='briggs', 
       robust=0,
       loopgain=0.5)