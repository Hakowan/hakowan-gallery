# Hakowan Gallery

Generated from `recipe.toml` manifests. See [the manifest contract](RECIPE_MANIFEST.md).

## Recipes

| Recipe | Features | Backends | Result |
|---|---|---|---|
| [Connected Components](Components/README.md) | `surface, categorical, components, legend, multi-view` | `mitsuba, webgl` | [foot_front.webp](Components/results/foot_front.webp) |
| [Cross-Field Streamlines](CrossField/README.md) | `surface, curve, cross-field, streamline, composition, z-up` | `mitsuba, webgl` | [shark_stream_lines.webp](CrossField/results/shark_stream_lines.webp) |
| [Developable Surface Flow](Developable/README.md) | `surface, computed-normal, comparison, camera` | `mitsuba, webgl` | [mask_0.webp](Developable/results/mask_0.webp) |
| [Elevation Map](Elevation/README.md) | `surface, heightmap, scalar-field, legend, camera` | `mitsuba, webgl` | [usgs_1_n35112.webp](Elevation/results/usgs_1_n35112.webp) |
| [Face Texture and UV Layout](Face/README.md) | `surface, texture, uv, normal, comparison, camera-fit` | `mitsuba, webgl` | [face.webp](Face/results/face.webp) |
| [Fiber Curves](Fibers/README.md) | `curve, categorical, composition, materials` | `mitsuba, webgl` | [fibers.webp](Fibers/results/fibers.webp) |
| [Incremental Potential Contact](IPC/README.md) | `surface, deformation, glass, orthographic, multi-view` | `mitsuba, webgl` | [ipc_side_10.webp](IPC/results/ipc_side_10.webp) |
| [Layout Embedding](Layout/README.md) | `surface, curve, categorical, legend, glass, comparison` | `mitsuba, webgl` | [pig_embedded.webp](Layout/results/pig_embedded.webp) |
| [Mean Curvature Flow](Flow/README.md) | `surface, scalar-field, comparison, layout, legend, z-up` | `mitsuba, webgl` | [bust_comp.webp](Flow/results/bust_comp.webp) |
| [Mesh Deformation](Deformation/README.md) | `surface, filter, comparison, multi-view, materials` | `mitsuba, webgl` | [cylinder_1.webp](Deformation/results/cylinder_1.webp) |
| [Moon](Moon/README.md) | `surface, image-texture, bump-map, z-up, two-view` | `mitsuba, webgl` | [moon.webp](Moon/results/moon.webp) |
| [Penny](Penny/README.md) | `surface, conductor, render-passes, normal, depth` | `blender, webgl` | [penny.webp](Penny/results/penny.webp) |
| [Powell-Sabin Splines](PowellSabin/README.md) | `surface, point, curve, categorical, explode, legend` | `mitsuba, webgl` | [powell_sabin.webp](PowellSabin/results/powell_sabin.webp) |
| [Reconstructed 3D Sketches](Sketch/README.md) | `curve, line-art, materials, camera, environment` | `mitsuba, webgl` | [Prof2task2_guitar_01_rough_dark.webp](Sketch/results/Prof2task2_guitar_01_rough_dark.webp) |
| [Scalable Locally Injective Maps](Slim/README.md) | `surface, uv, image-texture, rotation` | `mitsuba, webgl` | [fig3.webp](Slim/results/fig3.webp) |
| [Smoothed Particle Hydrodynamics](SPH/README.md) | `point-cloud, vector-norm, scalar-field, legend, filter` | `mitsuba, webgl` | [waterbell_010_all.webp](SPH/results/waterbell_010_all.webp) |
| [Spot](Spot/README.md) | `surface, curve, wireframe, composition` | `mitsuba, webgl` | [spot_wireframe.webp](Spot/results/spot_wireframe.webp) |
| [Surface Skeleton](Skeleton/README.md) | `surface, point, curve, glass, composition` | `mitsuba, webgl` | [fertility_skeleton.webp](Skeleton/results/fertility_skeleton.webp) |
| [TetWild Cutaway](TetWild/README.md) | `surface, curve, tetrahedral, clipping, categorical, glass` | `mitsuba, webgl` | [bust.webp](TetWild/results/bust.webp) |
| [The Heat Method](Heat/README.md) | `surface, scalar-field, isocontour, legend, two-view` | `mitsuba, webgl` | [bunny_heat.webp](Heat/results/bunny_heat.webp) |
| [UV Seams](Seams/README.md) | `surface, curve, uv, seams, boundary, composition` | `mitsuba, webgl` | [spot_seam.webp](Seams/results/spot_seam.webp) |

## Features

- **boundary**: [UV Seams](Seams/README.md)
- **bump-map**: [Moon](Moon/README.md)
- **camera**: [Developable Surface Flow](Developable/README.md), [Elevation Map](Elevation/README.md), [Reconstructed 3D Sketches](Sketch/README.md)
- **camera-fit**: [Face Texture and UV Layout](Face/README.md)
- **categorical**: [Connected Components](Components/README.md), [Fiber Curves](Fibers/README.md), [Layout Embedding](Layout/README.md), [Powell-Sabin Splines](PowellSabin/README.md), [TetWild Cutaway](TetWild/README.md)
- **clipping**: [TetWild Cutaway](TetWild/README.md)
- **comparison**: [Developable Surface Flow](Developable/README.md), [Face Texture and UV Layout](Face/README.md), [Layout Embedding](Layout/README.md), [Mean Curvature Flow](Flow/README.md), [Mesh Deformation](Deformation/README.md)
- **components**: [Connected Components](Components/README.md)
- **composition**: [Cross-Field Streamlines](CrossField/README.md), [Fiber Curves](Fibers/README.md), [Spot](Spot/README.md), [Surface Skeleton](Skeleton/README.md), [UV Seams](Seams/README.md)
- **computed-normal**: [Developable Surface Flow](Developable/README.md)
- **conductor**: [Penny](Penny/README.md)
- **cross-field**: [Cross-Field Streamlines](CrossField/README.md)
- **curve**: [Cross-Field Streamlines](CrossField/README.md), [Fiber Curves](Fibers/README.md), [Layout Embedding](Layout/README.md), [Powell-Sabin Splines](PowellSabin/README.md), [Reconstructed 3D Sketches](Sketch/README.md), [Spot](Spot/README.md), [Surface Skeleton](Skeleton/README.md), [TetWild Cutaway](TetWild/README.md), [UV Seams](Seams/README.md)
- **deformation**: [Incremental Potential Contact](IPC/README.md)
- **depth**: [Penny](Penny/README.md)
- **environment**: [Reconstructed 3D Sketches](Sketch/README.md)
- **explode**: [Powell-Sabin Splines](PowellSabin/README.md)
- **filter**: [Mesh Deformation](Deformation/README.md), [Smoothed Particle Hydrodynamics](SPH/README.md)
- **glass**: [Incremental Potential Contact](IPC/README.md), [Layout Embedding](Layout/README.md), [Surface Skeleton](Skeleton/README.md), [TetWild Cutaway](TetWild/README.md)
- **heightmap**: [Elevation Map](Elevation/README.md)
- **image-texture**: [Moon](Moon/README.md), [Scalable Locally Injective Maps](Slim/README.md)
- **isocontour**: [The Heat Method](Heat/README.md)
- **layout**: [Mean Curvature Flow](Flow/README.md)
- **legend**: [Connected Components](Components/README.md), [Elevation Map](Elevation/README.md), [Layout Embedding](Layout/README.md), [Mean Curvature Flow](Flow/README.md), [Powell-Sabin Splines](PowellSabin/README.md), [Smoothed Particle Hydrodynamics](SPH/README.md), [The Heat Method](Heat/README.md)
- **line-art**: [Reconstructed 3D Sketches](Sketch/README.md)
- **materials**: [Fiber Curves](Fibers/README.md), [Mesh Deformation](Deformation/README.md), [Reconstructed 3D Sketches](Sketch/README.md)
- **multi-view**: [Connected Components](Components/README.md), [Incremental Potential Contact](IPC/README.md), [Mesh Deformation](Deformation/README.md)
- **normal**: [Face Texture and UV Layout](Face/README.md), [Penny](Penny/README.md)
- **orthographic**: [Incremental Potential Contact](IPC/README.md)
- **point**: [Powell-Sabin Splines](PowellSabin/README.md), [Surface Skeleton](Skeleton/README.md)
- **point-cloud**: [Smoothed Particle Hydrodynamics](SPH/README.md)
- **render-passes**: [Penny](Penny/README.md)
- **rotation**: [Scalable Locally Injective Maps](Slim/README.md)
- **scalar-field**: [Elevation Map](Elevation/README.md), [Mean Curvature Flow](Flow/README.md), [Smoothed Particle Hydrodynamics](SPH/README.md), [The Heat Method](Heat/README.md)
- **seams**: [UV Seams](Seams/README.md)
- **streamline**: [Cross-Field Streamlines](CrossField/README.md)
- **surface**: [Connected Components](Components/README.md), [Cross-Field Streamlines](CrossField/README.md), [Developable Surface Flow](Developable/README.md), [Elevation Map](Elevation/README.md), [Face Texture and UV Layout](Face/README.md), [Incremental Potential Contact](IPC/README.md), [Layout Embedding](Layout/README.md), [Mean Curvature Flow](Flow/README.md), [Mesh Deformation](Deformation/README.md), [Moon](Moon/README.md), [Penny](Penny/README.md), [Powell-Sabin Splines](PowellSabin/README.md), [Scalable Locally Injective Maps](Slim/README.md), [Spot](Spot/README.md), [Surface Skeleton](Skeleton/README.md), [TetWild Cutaway](TetWild/README.md), [The Heat Method](Heat/README.md), [UV Seams](Seams/README.md)
- **tetrahedral**: [TetWild Cutaway](TetWild/README.md)
- **texture**: [Face Texture and UV Layout](Face/README.md)
- **two-view**: [Moon](Moon/README.md), [The Heat Method](Heat/README.md)
- **uv**: [Face Texture and UV Layout](Face/README.md), [Scalable Locally Injective Maps](Slim/README.md), [UV Seams](Seams/README.md)
- **vector-norm**: [Smoothed Particle Hydrodynamics](SPH/README.md)
- **wireframe**: [Spot](Spot/README.md)
- **z-up**: [Cross-Field Streamlines](CrossField/README.md), [Mean Curvature Flow](Flow/README.md), [Moon](Moon/README.md)
