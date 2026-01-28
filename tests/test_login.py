
from pathlib import Path
from pytest_bdd import scenarios

HERE = Path(__file__).resolve().parent
FEATURE = HERE / "features" / "login.feature"

scenarios(str(FEATURE))

