import pytest
from links.linksList import test_links


@pytest.mark.parametrize('link', test_links)
def test_abused_offers(abuse_page, link):
    abuse_page.get_link(link)
    abuse_page.find_cf_abuse()
    assert 1 == 1
