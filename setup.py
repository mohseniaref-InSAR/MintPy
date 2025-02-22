#!/usr/bin/env python
############################################################
# Program is part of MintPy                                #
# Copyright (c) 2013, Zhang Yunjun, Heresh Fattahi         #
# Author: Zhang Yunjun, Nov 2020                           #
############################################################

import os
import sys
# Always prefer setuptools over distutils
from setuptools import setup, find_packages

# Grab version and description from version.py
# link: https://stackoverflow.com/questions/53648900
sys.path.append(os.path.dirname(__file__))
from mintpy.version import version, description

# Grab long_description from README.md
with open("docs/README.md", "r") as f:
    long_description = f.read()

setup(
    name="mintpy",
    version=version,
    description=description,
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/insarlab/MintPy",
    download_url=("https://github.com/insarlab/MintPy/archive/v{}.tar.gz".format(version)),
    author="Zhang Yunjun, Heresh Fattahi",
    author_email="yunjunzgeo@gmail.com",
    license="GPL-3.0-or-later",
    license_files=("LICENSE",),

    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Topic :: Scientific/Engineering",
        "License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
    ],
    keywords="InSAR, deformation, time-series, volcano, earthquake, tectonics, geodesy, geophysics, remote-sensing",

    project_urls={
        "Bug Reports": "https://github.com/insarlab/mintpy/issues",
        "Documentation": "https://mintpy.readthedocs.io/",
        "Source": "https://github.com/insarlab/mintpy",
    },

    # dependencies
    python_requires=">=3.6",
    install_requires=[
        "cartopy",
        "cvxopt",
        "dask>=1.0",
        "dask-jobqueue>=0.3",
        "defusedxml",
        "h5py",
        "joblib",
        "lxml",
        "matplotlib",
        "numpy",
        "pyaps3>=0.3",
        "pykml>=0.2",
        "pyproj",
        "pyresample",  # pip installed version does not work
        "setuptools",
        "scikit-image",
        "scipy",
    ],
    extras_require={
        "cli": ["argcomplete"],
        'platemotion': ['platemotion', 'astropy'],  # will be removed in the coming new version of plate motion script
    },

    # package discovery
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'mintpy = mintpy.__main__:main',
            'add_attribute.py = mintpy.add_attribute:main',
            'add.py = mintpy.add:main',
            'asc_desc2horz_vert.py = mintpy.asc_desc2horz_vert:main',
            'bulk_plate_motion.py = mintpy.bulk_plate_motion:main',
            'closure_phase_bias.py = mintpy.closure_phase_bias:main',
            'dem_error.py = mintpy.dem_error:main',
            'dem_gsi.py = mintpy.dem_gsi:main',
            'diff.py = mintpy.diff:main',
            'generate_mask.py = mintpy.generate_mask:main',
            'geocode.py = mintpy.geocode:main',
            'ifgram_inversion.py = mintpy.ifgram_inversion:main',
            'image_math.py = mintpy.image_math:main',
            'image_stitch.py = mintpy.image_stitch:main',
            'info.py = mintpy.info:main',
            'iono_tec.py = mintpy.iono_tec:main',
            'load_data.py = mintpy.load_data:main',
            'load_gbis.py = mintpy.load_gbis:main',
            'local_oscilator_drift.py = mintpy.local_oscilator_drift:main',
            'lookup_geo2radar.py = mintpy.lookup_geo2radar:main',
            'mask.py = mintpy.mask:main',
            'modify_network.py = mintpy.modify_network:main',
            'multilook.py = mintpy.multilook:main',
            'multi_transect.py = mintpy.multi_transect:main',
            'plot_coherence_matrix.py = mintpy.plot_coherence_matrix:main',
            'plot_network.py = mintpy.plot_network:main',
            'plot_transection.py = mintpy.plot_transection:main',
            'prep_aria.py = mintpy.prep_aria:main',
            'prep_cosicorr.py = mintpy.prep_cosicorr:main',
            'prep_fringe.py = mintpy.prep_fringe:main',
            'prep_gamma.py = mintpy.prep_gamma:main',
            'prep_gmtsar.py = mintpy.prep_gmtsar:main',
            'prep_hyp3.py = mintpy.prep_hyp3:main',
            'prep_isce.py = mintpy.prep_isce:main',
            'prep_roipac.py = mintpy.prep_roipac:main',
            'prep_snap.py = mintpy.prep_snap:main',
            'reference_date.py = mintpy.reference_date:main',
            'reference_point.py = mintpy.reference_point:main',
            'remove_hdf5_dataset.py = mintpy.remove_hdf5_dataset:main',
            'remove_ramp.py = mintpy.remove_ramp:main',
            's1ab_range_bias.py = mintpy.s1ab_range_bias:main',
            'save_gbis.py = mintpy.save_gbis:main',
            'save_gdal.py = mintpy.save_gdal:main',
            'save_gmt.py = mintpy.save_gmt:main',
            'save_hdfeos5.py = mintpy.save_hdfeos5:main',
            'save_kite.py = mintpy.save_kite:main',
            'save_kmz.py = mintpy.save_kmz:main',
            'save_kmz_timeseries.py = mintpy.save_kmz_timeseries:main',
            'save_qgis.py = mintpy.save_qgis:main',
            'save_roipac.py = mintpy.save_roipac:main',
            'smallbaselineApp.py = mintpy.smallbaselineApp:main',
            'solid_earth_tides.py = mintpy.solid_earth_tides:main',
            'spatial_average.py = mintpy.spatial_average:main',
            'spatial_filter.py = mintpy.spatial_filter:main',
            'subset.py = mintpy.subset:main',
            'temporal_average.py = mintpy.temporal_average:main',
            'temporal_derivative.py = mintpy.temporal_derivative:main',
            'temporal_filter.py = mintpy.temporal_filter:main',
            'timeseries2velocity.py = mintpy.timeseries2velocity:main',
            'timeseries_rms.py = mintpy.timeseries_rms:main',
            'tropo_gacos.py = mintpy.tropo_gacos:main',
            'tropo_phase_elevation.py = mintpy.tropo_phase_elevation:main',
            'tropo_pyaps3.py = mintpy.tropo_pyaps3:main',
            'tsview.py = mintpy.tsview:main',
            'unwrap_error_bridging.py = mintpy.unwrap_error_bridging:main',
            'unwrap_error_phase_closure.py = mintpy.unwrap_error_phase_closure:main',
            'view.py = mintpy.view:main',
        ]
    },

    # data files
    include_package_data=True,
    package_data={
        "mintpy": [
            "data/*.js",
            "data/*.png",
            "data/colormaps/*.cpt",
            "data/input_files/*.txt",
            "data/input_files/*.template",
            "data/input_files/*.md",
            "defaults/*.cfg",
            "defaults/*.yaml",
        ],
    },
    zip_safe=False,
)
