# Copyright (c) 2015, Frappe Technologies Pvt. Ltd. and Contributors
# See license.txt

import frappe
<<<<<<< HEAD
from frappe.tests.utils import FrappeTestCase
=======
from frappe.tests import IntegrationTestCase, UnitTestCase
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)

from erpnext.stock.doctype.item.test_item import make_item
from erpnext.stock.utils import _create_bin


<<<<<<< HEAD
class TestBin(FrappeTestCase):
=======
class UnitTestBin(UnitTestCase):
	"""
	Unit tests for Bin.
	Use this class for testing individual functions and methods.
	"""

	pass


class TestBin(IntegrationTestCase):
>>>>>>> 94d7e5964b (fix: add doc.status to translation from POS)
	def test_concurrent_inserts(self):
		"""Ensure no duplicates are possible in case of concurrent inserts"""
		item_code = "_TestConcurrentBin"
		make_item(item_code)
		warehouse = "_Test Warehouse - _TC"

		bin1 = frappe.get_doc(doctype="Bin", item_code=item_code, warehouse=warehouse)
		bin1.insert()

		bin2 = frappe.get_doc(doctype="Bin", item_code=item_code, warehouse=warehouse)
		with self.assertRaises(frappe.UniqueValidationError):
			bin2.insert()

		# util method should handle it
		bin = _create_bin(item_code, warehouse)
		self.assertEqual(bin.item_code, item_code)

		frappe.db.rollback()

	def test_index_exists(self):
		indexes = frappe.db.sql("show index from tabBin where Non_unique = 0", as_dict=1)
		if not any(index.get("Key_name") == "unique_item_warehouse" for index in indexes):
			self.fail("Expected unique index on item-warehouse")
