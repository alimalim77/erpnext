# Copyright (c) 2023, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

# import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase


class TestProcessSubscription(FrappeTestCase):
=======
from frappe.tests import IntegrationTestCase, UnitTestCase


class UnitTestProcessSubscription(UnitTestCase):
	"""
	Unit tests for ProcessSubscription.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestProcessSubscription(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	pass
