# Robust = +2 (similar to natural - sensitive, large beam)
tclean(vis='your_data.ms', 
       imagename='psf_robust_plus2', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=2)

# Robust = 0 (middle ground)
tclean(vis='your_data.ms', 
       imagename='psf_robust_0', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=0)

# Robust = -2 (similar to uniform - sharp beam, less sensitive)
tclean(vis='your_data.ms', 
       imagename='psf_robust_minus2', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=-2)