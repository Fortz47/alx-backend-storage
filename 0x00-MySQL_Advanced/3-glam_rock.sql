-- SQL script that lists all bands with Glam rock as their main style

SELECT `band_name`, IF(`formed` < '2022', '2022' - `formed`, '0') AS lifespan
FROM `metal_bands`
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;
