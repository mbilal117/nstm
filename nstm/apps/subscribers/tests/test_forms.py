from nstm.apps.lists.tests.factories import MailingListFactory
from nstm.apps.subscribers.forms import SubscribeForm
from nstm.test.testcases import TestCase


class TestSubscribeForm(TestCase):
    def test_cleaned_data(self):
        form = SubscribeForm(data={'email': 'JOHN@DOE.COM'}, mailing_list=MailingListFactory())
        form.is_valid()
        self.assertEqual('JOHN@doe.com', form.cleaned_data['email'])
