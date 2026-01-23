from enum import Enum

class ResultStates(str, Enum):
    ENABLED = "Enabled"
    DISABLED = "Disabled"
    SUBMITTED = "Submitted"
    CLICK = "Click"