# GC Simulator

Interactive gas chromatography simulator with 102 compounds on DB-5MS UI, four carrier gases, isothermal and temperature-programmed methods, and chromatogram and method export.

This repository contains the standalone browser simulator. The complete website and contact service are in [gc-simulator-website](https://github.com/pgboswell/gc-simulator-website).

## Run locally

Serve the included `public/` directory over HTTP:

```
python -m http.server 8000 --directory public
```

Open http://localhost:8000/. No package installation is needed.

## Edit and build

Edit the application in `public/assets/simulator/` and its page template in `simulator/workspace.html`. Run `python build.py` to regenerate `public/index.html`. The build uses Python's standard library. The generated page is included for immediate use.

## Tests

Run `npm test` with Node.js. Included fixtures cover interpolation, transport, retention, peak width, sampling, and plotting behavior. See [model notes](public/MODEL.md) for assumptions and limitations.

## Hosting

Publish the `public/` directory on a static web host. This standalone application has no server-side service.

## License

CC BY-NC-SA 3.0 US. See LICENSE and NOTICE.
