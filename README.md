# rio-terrarium
Encode arbitrary bit depth rasters in pseudo base-256 as Terrarium RGB

## Original code

This code is based on the original code from [rio-rgbify](https://github.com/mapbox/rio-rgbify).

## Installation

### Development
```
git clone git@github.com:smellman/rio-terrarium.git

cd rio-terrarium

pip install -e '.[test]'

```

## CLI usage

- Input can be any raster readable by `rasterio`
- Output can be any raster format writable by `rasterio` OR
- To create tiles _directly_ from data (recommended), output to an `.mbtiles`

```
Usage: rio terrarium [OPTIONS] SRC_PATH DST_PATH

Options:
  --bidx INTEGER         Band to encode [DEFAULT=1]
  --max-z INTEGER        Maximum zoom to tile (.mbtiles output only)
  --bounding-tile TEXT   Bounding tile '[{x}, {y}, {z}]' to limit output tiles
                         (.mbtiles output only)
  --min-z INTEGER        Minimum zoom to tile (.mbtiles output only)
  --format [png|webp]    Output tile format (.mbtiles output only)
  -j, --workers INTEGER  Workers to run [DEFAULT=4]
  -v, --verbose
  --co NAME=VALUE        Driver specific creation options.See the
                         documentation for the selected output driver for more
                         information.
  --help                 Show this message and exit.
```
