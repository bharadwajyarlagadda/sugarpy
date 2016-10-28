# -*- coding: utf-8 -*-
"""sugar.py module.
"""

from .__pkg__ import (
    __description__,
    __url__,
    __version__,
    __author__,
    __email__,
    __license__
)

from .arrays import (
    add,
    append,
    average,
    clone,
    compact,
    construct,
    count,
    create,
    every,
    exclude,
    filter,
    first,
    from_,
    includes,
    is_empty,
    is_equal,
    last,
    subtract
)

from .number import (
    random_
)

from .predicates import (
    is_array,
    is_boolean,
    is_none,
    is_number,
    is_string
)
