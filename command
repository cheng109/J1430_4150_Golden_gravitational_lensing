./lensview -logfilepath . -tracelevel 2 -pixelres 0.05 -datafile Gold_gal_subtracted.fits -sourcefile empty300by300.fits -psffile Gold_PSF.fits -nice 2 -pixelratio 2 -maxiter 100 -paramfile parameter_config -srcxoffset -20 -srcyoffset -20 -useminfinder -srcdefaultval 0.1 -noisefile Gold_var.fits -targetchisqu 0 -mask mask.fits $*
