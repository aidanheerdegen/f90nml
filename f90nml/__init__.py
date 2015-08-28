"""f90nml
   ======

   A Fortran 90 namelist parser and generator.

   :copyright: Copyright 2014 Marshall Ward, see AUTHORS for details.
   :license: Apache License, Version 2.0, see LICENSE for details.
"""
from f90nml.parser import Parser

__version__ = '0.12'


def read(nml_path, row_major=False):
    """Parse a Fortran 90 namelist file with file path ``nml_path``  return its
    contents as a ``NmlDict``.

    >>> nml = f90nml.read('data.nml')

    This function is equivalent to the ``read`` function of the ``Parser``
    object.

    >>> parser = f90nml.Parser()
    >>> nml = parser.read('data.nml')

    Multidimensional array data contiguity is preserved by default, so that
    column-major Fortran data is represented as row-major Python list of
    lists.

    The ``row_major`` flag will reorder the data to preserve the index rules
    between Fortran to Python, but the data will be converted to row-major form
    (with respect to Fortran)."""

    return Parser().read(nml_path, row_major=row_major)


def write(nml, nml_path, force=False):
    """Output namelist ``nml`` to a Fortran 90 namelist file with file path
    ``nml_path``.

    >>> f90nml.write(nml, 'data.nml')

    This function is equivalent to the ``write`` function of the ``Namelist``
    object ``nml``.

    >>> nml.write('data.nml')

    By default, ``write`` will not overwrite an existing file.  To override
    this, use the ``force`` flag.

    >>> nml.write('data.nml', force=True)"""

    nml.write(nml_path, force=force)


def patch(nml_path, nml_patch, out_path=None, row_major=False):
    """Create a new namelist based on an input namelist and reference dict.

    >>> f90nml.patch('data.nml', nml_patch, 'patched_data.nml')

    This function is equivalent to the ``read`` function of the ``Parser``
    object with the patch output arguments.

    >>> parser = f90nml.Parser()
    >>> nml = parser.read('data.nml', nml_path, 'patched_data.nml')

    A patched namelist file will retain any formatting or comments from the
    original namelist file.  Any modified values will be formatted based on the
    settings of the ``Namelist`` object."""

    return Parser().read(nml_path, nml_patch, out_path, row_major=row_major)
