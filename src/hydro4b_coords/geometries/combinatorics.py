"""
This module contains the dictionary that maps geometry tags to the number of times
that geometry appears, from the POV of a molecule in an HCP lattice surrounded by
its 56 nearest and next-nearest neighbours.
"""


# fmt: off
MAP_GEOMETRY_TAG_TO_COMBINATORIAL_COUNT = {
    '1'                                     : 8,
    'sqrt2'                                 : 48,
    'sqrt83'                                : 12,
    'sqrt3'                                 : 36,
    'sqrt2_sqrt2'                           : 12,
    'sqrt2_sqrt113'                         : 48,
    'sqrt2_sqrt3'                           : 144,
    'sqrt83_sqrt113'                        : 48,
    'sqrt3_sqrt3'                           : 72,
    'sqrt3_sqrt113'                         : 48,
    'sqrt3_2'                               : 96,
    'sqrt113_sqrt113'                       : 24,
    'sqrt2_sqrt2_sqrt83'                    : 24,
    'sqrt2_sqrt2_sqrt113'                   : 24,
    'sqrt2_sqrt2_2'                         : 24,
    'sqrt2_sqrt83_sqrt113'                  : 48,
    'sqrt2_sqrt3_sqrt3_a'                   : 144,
    'sqrt2_sqrt3_sqrt3_b'                   : 48,
    'sqrt2_sqrt3_sqrt113_a'                 : 48,
    'sqrt2_sqrt3_sqrt113_b'                 : 48,
    'sqrt2_sqrt113_sqrt113_a'               : 24,
    'sqrt2_sqrt113_sqrt113_b'               : 48,
    'sqrt83_sqrt3_sqrt3'                    : 24,
    'sqrt83_sqrt3_sqrt113'                  : 48,
    'sqrt83_sqrt113_sqrt113'                : 48,
    'sqrt3_sqrt3_sqrt3_a'                   : 24,
    'sqrt3_sqrt3_sqrt3_b'                   : 8,
    'sqrt3_sqrt3_2_a'                       : 48,
    'sqrt3_sqrt3_2_b'                       : 48,
    'sqrt2_sqrt2_sqrt83_sqrt3'              : 12,
    'sqrt2_sqrt2_sqrt83_sqrt113'            : 48,
    'sqrt2_sqrt2_sqrt3_sqrt3_a'             : 48,
    'sqrt2_sqrt2_sqrt3_sqrt3_b'             : 12,
    'sqrt2_sqrt2_sqrt3_2'                   : 96,
    'sqrt2_sqrt3_sqrt3_sqrt3'               : 96,
    'sqrt2_sqrt3_sqrt3_sqrt113_a'           : 48,
    'sqrt2_sqrt3_sqrt3_sqrt113_b'           : 48,
    'sqrt2_sqrt3_sqrt3_sqrt113_c'           : 48,
    'sqrt2_sqrt3_sqrt3_2_a'                 : 48,
    'sqrt2_sqrt3_sqrt3_2_b'                 : 24,
    'sqrt2_sqrt3_sqrt3_2_c'                 : 48,
    'sqrt2_sqrt3_sqrt113_sqrt113_a'         : 48,
    'sqrt2_sqrt3_sqrt113_sqrt113_b'         : 48,
    'sqrt2_sqrt3_sqrt113_sqrt113_c'         : 48,
    'sqrt2_sqrt3_sqrt113_sqrt113_d'         : 48,
    'sqrt83_sqrt83_sqrt113_sqrt113'         : 12,
    'sqrt83_sqrt3_sqrt3_sqrt3'              : 24,
    'sqrt83_sqrt3_sqrt3_sqrt113'            : 48,
    'sqrt83_sqrt3_sqrt3_2'                  : 24,
    'sqrt83_sqrt3_sqrt113_sqrt113'          : 48,
    'sqrt83_sqrt113_sqrt113_sqrt113'        : 48,
    'sqrt83_sqrt113_sqrt113_2'              : 24,
    'sqrt3_sqrt3_sqrt3_sqrt113'             : 24,
    'sqrt3_sqrt3_sqrt3_2_a'                 : 24,
    'sqrt3_sqrt3_sqrt3_2_b'                 : 96,
    'sqrt3_sqrt3_sqrt3_2_c'                 : 48,
    'sqrt3_sqrt3_sqrt113_sqrt113_a'         : 48,
    'sqrt3_sqrt3_sqrt113_sqrt113_b'         : 24,
    'sqrt3_sqrt3_sqrt113_sqrt113_c'         : 48,
    'sqrt3_sqrt3_sqrt113_2'                 : 24,
    'sqrt3_sqrt3_2_2'                       : 12,
    'sqrt3_sqrt113_sqrt113_sqrt113'         : 48,
    'sqrt3_sqrt113_sqrt113_2'               : 48,
    'sqrt3_2_2_2'                           : 24,
    'sqrt2_sqrt2_sqrt83_sqrt3_sqrt3'        : 24,
    'sqrt2_sqrt2_sqrt83_sqrt3_sqrt113'      : 48,
    'sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_a'     : 24,
    'sqrt2_sqrt2_sqrt3_sqrt3_sqrt113_b'     : 48,
    'sqrt2_sqrt2_sqrt3_sqrt3_2'             : 48,
    'sqrt2_sqrt2_sqrt3_sqrt113_2'           : 48,
    'sqrt2_sqrt2_sqrt113_sqrt113_2'         : 24,
    'sqrt2_sqrt83_sqrt3_sqrt3_sqrt113'      : 48,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_a'       : 48,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt3_b'       : 24,
    'sqrt2_sqrt3_sqrt3_sqrt3_sqrt113'       : 48,
    'sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_a'   : 48,
    'sqrt2_sqrt3_sqrt3_sqrt113_sqrt113_b'   : 48,
    'sqrt83_sqrt3_sqrt3_sqrt3_sqrt3'        : 12,
    'sqrt83_sqrt3_sqrt3_sqrt3_sqrt113'      : 48,
    'sqrt3_sqrt3_sqrt3_sqrt113_2'           : 48,
    'sqrt3_sqrt3_2_2_2'                     : 24,
    'sqrt3_sqrt113_sqrt113_sqrt113_sqrt113' : 24,
    'sqrt3_sqrt113_sqrt113_sqrt113_2'       : 96,
}
# fmt: on
