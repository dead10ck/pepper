# -*- coding: utf-8 -*-
# Import Python Libraries
from __future__ import print_function, unicode_literals, absolute_import
import sys

from mock import patch, MagicMock

PAYLOAD = {
    "return": [
        {
            "saltstack.ezh.msk.ru": {
                "jid": "20180414193904158892",
                "ret": "pass",
                "retcode": 0
            },
            "ezh.msk.ru": {
                "jid": "20180414193904158892",
                "ret": "Hello from SaltStack",
            }
        }
    ]
}


@patch('pepper.cli.PepperCli.low', MagicMock(side_effect=lambda api, load: PAYLOAD))
def test_default(session_pepper_no_login):
    sys.argv = ['pepper', 'minion_id', 'request']
    ret_code = session_pepper_no_login.script.Pepper()()
    assert ret_code == 0


@patch('pepper.cli.PepperCli.low', MagicMock(side_effect=lambda api, load: PAYLOAD))
def test_fail_any(session_pepper_no_login):
    sys.argv = ['pepper', '--fail-any', 'minion_id', 'request']
    ret_code = session_pepper_no_login.script.Pepper()()
    assert ret_code == 0


@patch('pepper.cli.PepperCli.low', MagicMock(side_effect=lambda api, load: PAYLOAD))
def test_fail_any_none(session_pepper_no_login):
    sys.argv = ['pepper', '--fail-any-none', 'minion_id', 'request']
    ret_code = session_pepper_no_login.script.Pepper()()
    assert ret_code == 0


@patch('pepper.cli.PepperCli.low', MagicMock(side_effect=lambda api, load: PAYLOAD))
def test_fail_all(session_pepper_no_login):
    sys.argv = ['pepper', '--fail-all', 'minion_id', 'request']
    ret_code = session_pepper_no_login.script.Pepper()()
    assert ret_code == 0


@patch('pepper.cli.PepperCli.low', MagicMock(side_effect=lambda api, load: PAYLOAD))
def test_fail_all_none(session_pepper_no_login):
    sys.argv = ['pepper', '--fail-all-none', 'minion_id', 'request']
    ret_code = session_pepper_no_login.script.Pepper()()
    assert ret_code == 0
