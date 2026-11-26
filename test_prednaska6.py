import random
from prednaska6 import vrat_symboly

def test_vrat_symboly():
    random.seed(0)
    assert vrat_symboly() == ['7️⃣', '🍇', '7️⃣']