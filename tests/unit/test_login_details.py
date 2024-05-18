# -*- coding: utf-8 -*-
from __future__ import absolute_import

import sys

# Import Testing libraries
from mock import MagicMock, patch

# Import Pepper Libs
import pepper.cli


def test_interactive_logins():
    sys.argv = ["pepper", "-c", "tests/.pepperrc", "-p", "noopts"]

    with patch("pepper.cli.input", MagicMock(return_value="pepper")), patch(
        "pepper.cli.getpass.getpass", MagicMock(return_value="pepper")
    ):
        result = pepper.cli.PepperCli().get_login_details()

    assert result["username"] == "pepper"
    assert result["password"] == "pepper"
