from .lebedev3 import Lebedev3
from .lebedev3 import LEBEDEV3_SCHEME_INFO
from .lebedev5 import Lebedev5
from .lebedev5 import LEBEDEV5_SCHEME_INFO

LebedevScheme = Lebedev3 | Lebedev5

LEBEDEV_SCHEME_MAP = {
    Lebedev3: LEBEDEV3_SCHEME_INFO,
    Lebedev5: LEBEDEV5_SCHEME_INFO,
}
