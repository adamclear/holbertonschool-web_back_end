-- lists all bands with "Glam rock" as their main style by longevity

SELECT band_name, (IFNULL(split, 2020) - formed) as lifespan
FROM metal_bands
WHERE style LIKE '%Glam rock%'
ORDER BY lifespan DESC;