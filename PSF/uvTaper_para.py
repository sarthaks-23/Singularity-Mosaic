# No UV taper (baseline)
tclean(vis='your_data.ms', 
       imagename='psf_no_uvtaper', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=0)

# With UV taper - degrades resolution, increases sensitivity to extended sources
tclean(vis='your_data.ms', 
       imagename='psf_with_uvtaper', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=0, 
       uvtaper=['2arcsec'])

# Stronger UV taper
tclean(vis='your_data.ms', 
       imagename='psf_strong_uvtaper', 
       imsize=512, 
       cell='1arcsec', 
       niter=0, 
       weighting='briggs', 
       robust=0, 
       uvtaper=['4arcsec'])