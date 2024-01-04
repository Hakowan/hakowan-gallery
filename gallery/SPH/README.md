# Smoothed Particle Hydrodynamics

This example aims to reproduce Figure 9 from the paper "[Implicit Surface Tension for SPH Fluid Simulation](https://animation.rwth-aachen.de/media/papers/85/2023-TOG-SPH_Implicit_Surface_tension-compressed.pdf)".

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010.png?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010_all.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_010_all.png?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030.png?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030_all.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_030_all.png?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060.png?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060_all.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_060_all.png?raw=true)

[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133.png?raw=true)
[<img src="https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133_all.png?raw=true" width=45%/>](https://github.com/qnzhou/hakowan-gallery/blob/main/gallery/SPH/results/waterbell_133_all.png?raw=true)

## Data

The data is genearted using the [SPlisHSPlasH](https://splishsplash.physics-simulation.org/gallery/)
library which comes with the scene files used to generate the original figure:

```sh
SPHSimulate ../data/Scenes/SurfaceTension_WaterBell_JWL+23.json
```
