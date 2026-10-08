from enum import Enum

class Plan(str, Enum):
    CUT = "cut"
    MAINTAIN = "maintain"
    BULK = "bulk"
