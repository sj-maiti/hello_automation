import sys
import os

# Add project root to Python path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from main import get_ip

def test_get_ip():
    ip = get_ip()
    assert isinstance(ip, str)
    assert len(ip.split(".")) == 4  # simple IPv4 check
