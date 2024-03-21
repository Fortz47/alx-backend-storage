-- SQL script that ranks country origins of bands, ordered by
-- the number of (non-unique) fans

SELECT `origin`, `fans` FROM `metal_bands`
GROUP BY origin;
