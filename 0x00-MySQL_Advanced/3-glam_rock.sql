-- SQL script that lists all bands with Glam rock as their main style

SELECT `band_name`, IF(`formed` < '2022', `formed` - '2022', '0') AS lifespan
FROM `metal_bands`
ORDER BY lifespan DESC;
