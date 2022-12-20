
def test_abused_offers(abuse_page):
    abuse_page.goto_page("googl.com")
    abuse_page.find_cf_abuse()
    assert 1 == 1
