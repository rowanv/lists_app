from django.test import TestCase
from lists.forms import EMPTY_ITEM_ERROR, ItemForm


class ItemFormTest(TestCase):

	def test_form_renders_item_text_input(self):
		form = ItemForm()
		#self.fail(form.as_p()) #renders form as html
		self.assertIn('placeholder="Enter a to-do item"', form.as_p())
		self.assertIn('class="form-control input-lg"', form.as_p())

	def test_form_validation_for_blank_items(self):
		form = ItemForm(data={'text': ''})
		self.assertFalse(form.is_valid()) #check for validation before try to save any data
		self.assertEqual(form.errors['text'], [EMPTY_ITEM_ERROR])