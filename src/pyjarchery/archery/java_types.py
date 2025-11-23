# ruff: noqa: N802

import jpype
import jpype.imports
from com.github.romualdrousseau.archery.commons.dsf.json import JSON as JSON_
from java.nio.file import Paths as Paths_
from java.util import EnumSet as EnumSet_
from java.util import List as List_


@jpype._jcustomizer.JConversion("java.nio.file.Path", instanceof=str)
def _JPathConvert(jcls, obj):
    return Paths_.get(obj)


@jpype._jcustomizer.JConversion("java.util.List", instanceof=list)
def _JListConvert(jcls, obj):
    return List_.of(obj)


@jpype._jcustomizer.JConversion("com.github.romualdrousseau.archery.commons.dsf.DSFObject", instanceof=str)
def _JDSFObjectConvert(jcls, obj):
    return JSON_.objectOf(obj)


@jpype._jcustomizer.JConversion("java.util.EnumSet", instanceof=list)
def _JEnumSetConvert(jcls, obj):
    if len(obj) <= 2:
        return EnumSet_.of(*obj)
    else:
        return EnumSet_.of(obj[0], obj[1:])
