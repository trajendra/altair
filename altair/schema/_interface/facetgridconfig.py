# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject


class FacetGridConfig(BaseObject):
    """Wrapper for Vega-Lite FacetGridConfig definition.
    
    Attributes
    ----------
    color: Unicode
        
    offset: CFloat
        
    opacity: CFloat
        
    """
    color = T.Unicode(allow_none=True, default_value=None)
    offset = T.CFloat(allow_none=True, default_value=None)
    opacity = T.CFloat(allow_none=True, default_value=None)
    
    def __init__(self, color=None, offset=None, opacity=None, **kwargs):
        kwds = dict(color=color, offset=offset, opacity=opacity)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(FacetGridConfig, self).__init__(**kwargs)