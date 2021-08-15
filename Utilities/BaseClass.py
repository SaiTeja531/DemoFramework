import pytest
import time


@pytest.mark.usefixtures("setup")
class BossClass:

    def how_much_time_u_want_to_stop_the_script(self, secs):
        return time.sleep(secs)
