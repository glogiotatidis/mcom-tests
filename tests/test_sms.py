#!/usr/bin/env python

# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.

import pytest
import requests

from pages.desktop.sms import SMS

link_check = pytest.mark.link_check
nondestructive = pytest.mark.nondestructive


class TestSMSPage():

    @nondestructive
    def test_info_link_destinations_are_correct(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_links = []
        for link in sms_page.info_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links

    @link_check
    @nondestructive
    def test_info_link_urls_are_valid(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_urls = []
        for link in sms_page.info_links_list:
            url = sms_page.link_destination(link.get('locator'))
            response_code = sms_page.get_response_code(url)
            if response_code != requests.codes.ok:
                bad_urls.append('%s is not a valid url - status code: %s.' % (url, response_code))
        assert [] == bad_urls

    @nondestructive
    def test_footer_section(self, mozwebqa):
        sms_page = SMS(mozwebqa)
        sms_page.go_to_page()
        bad_links = []
        for link in sms_page.Footer.footer_links_list:
            url = sms_page.link_destination(link.get('locator'))
            if not url.endswith(link.get('url_suffix')):
                bad_links.append('%s does not end with %s' % (url, link.get('url_suffix')))
        assert [] == bad_links
