-- SQL script that lists all bands with Glam rock as their main style

SELECT `band_name`, IF NULL(`split`, '2022' - `formed`, `split` - `formed`) AS lifespan
FROM `metal_bands`
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
