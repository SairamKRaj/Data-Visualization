Command to create Convexhull from the locations in LOCATION_COORDS table:

  select st_astext(polygon) ConvexHull from(select st_convexhull(st_collect(point_coordinates::geometry)) as polygon \
     from LOCATION_COORDS) value;

Determination of DISJOINT condition of polygons - Set1:
  
  SELECT ST_Disjoint(POLYGON'((-118.280984,34.033719), (-118.283735,34.035441), (-118.283520,34.034662), (-118.283805,34.034148),\
    (-118.282983,34.031143), (-118.280984,34.033719))'::geometry, POLYGON'((-118.273153,34.028614), (-118.278749,34.035146),\
    (-118.279541,34.033416), (-118.277695,34.031396), (-118.282058,34.030543), (-118.273153,34.028614))'::geometry);
  
 Determination of DISJOINT condition of polygons - Set2:
 
  SELECT ST_Disjoint(POLYGON'((-118.279541,34.033416), (-118.280984,34.033719), (-118.283735,34.035441), (-118.283520,34.034662),\
  (-118.283805,34.034148), (-118.279541,34.033416))'::geometry, POLYGON'((-118.273153,34.028614), (-118.277695,34.031396),\
  (-118.282983,34.031143), (-118.282058,34.030543), (-118.278749,34.035146), (-118.273153,34.028614))'::geometry);
  
