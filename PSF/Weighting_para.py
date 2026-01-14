# Natural weighting - highest sensitivity, larger rounder beam
tclean(vis='your_data.ms', 
       imagename='psf_natural', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='natural')

# Uniform weighting - high resolution, smaller elongated beam
tclean(vis='your_data.ms', 
       imagename='psf_uniform', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='uniform')

# Briggs weighting - balance between natural and uniform
tclean(vis='your_data.ms', 
       imagename='psf_briggs', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=0)