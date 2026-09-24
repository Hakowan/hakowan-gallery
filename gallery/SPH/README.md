# Smoothed Particle Hydrodynamics

This example aims to reproduce Figure 9 from the paper "[Implicit Surface Tension for SPH Fluid Simulation](https://animation.rwth-aachen.de/media/papers/85/2023-TOG-SPH_Implicit_Surface_tension-compressed.pdf)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010_all.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010_all.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030_all.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030_all.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060_all.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060_all.webp?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133.webp?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133_all.webp?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133_all.webp?raw=true)

[Interactive demo](https://qnzhou.github.io/hakowan-gallery/gallery/SPH/results/waterbell_010_all.html)

## Data

The data is genearted using the [SPlisHSPlasH](https://splishsplash.physics-simulation.org/gallery/)
library which comes with the scene files used to generate the original figure:

```sh
SPHSimulate ../data/Scenes/SurfaceTension_WaterBell_JWL+23.json
```

## Input contract

- `particles`: point-cloud from `data/ParticleData_Fluid_0_10.vtk`; `velocity` (vertex 3-channel vector).
- `emitter`: surface from `data/emitter.msh`; no pre-existing attributes required.

## Reproduce and inspect

```sh
python ../render_gallery.py --check SPH
python ../render_gallery.py --artifacts SPH
```

[Python](sph.py) · [Manifest](recipe.toml) · [Inspection](artifacts/inspect.json) · [Canonical JSON](artifacts/figure.json) · [Validation](artifacts/validation.json)
