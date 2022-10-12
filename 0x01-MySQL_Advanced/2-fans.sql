-- Ranks country origins of bands, ordered by number of fans

SELECT origin, SUM(fans) AS metal_fans FROM metal_bands
GROUP BY origin
ORDER BY metal_fans DESC;