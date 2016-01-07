from django.test import TestCase, Client
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from django.core.urlresolvers import reverse
from selenium.webdriver.firefox.webdriver import WebDriver


class TestMixin:
    def reverse(self, pattern):
        return '%s%s' % (self.live_server_url, reverse(pattern))


class PageTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super(TestCase, cls).setUpClass()
        cls.client = Client()

    def test_index(self):
        url = reverse('page:index')
        response = self.client.get(url)

        self.assertTrue(response.status_code is 200)
        self.assertTrue('works' in response.context)

    @classmethod
    def tearDownClass(cls):
        super(TestCase, cls).tearDownClass()


class PageWithSeleniumTest(StaticLiveServerTestCase, TestMixin):
    @classmethod
    def setUpClass(cls):
        super(PageWithSeleniumTest, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(PageWithSeleniumTest, cls).tearDownClass()

    def test_hello(self):
        self.selenium.get(self.reverse('page:index'))
        link = self.selenium.find_element_by_id('work')
        link.click()
