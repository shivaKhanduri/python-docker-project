import unittest
import pandas as pd
from analysis import compute_monthly_revenue, compute_product_revenue, compute_customer_revenue, compute_top_10_customers
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class TestAnalysis(unittest.TestCase):

    def setUp(self):
        
        self.data = pd.DataFrame({
            'order_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20],
            'customer_id': [1001, 1002, 1001, 1003, 1002, 1004, 1005, 1006, 1001, 1002, 1007, 1008, 1003, 1009, 1010, 1004, 1005, 1006, 1007, 1008],
            'order_date': pd.to_datetime(['2021-01-10', '2021-01-12', '2021-02-05', '2021-02-18', '2021-03-22', '2021-03-25', '2021-04-02', '2021-04-15', '2021-05-10', '2021-05-12', '2021-06-01', '2021-06-15', '2021-07-22', '2021-08-10', '2021-08-15', '2021-09-05', '2021-09-12', '2021-10-01', '2021-10-15', '2021-11-01']),
            'product_id': [1, 2, 3, 1, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19],
            'product_name': ['iPhone 12', 'Galaxy S21', 'MacBook Pro', 'iPhone 12', 'Surface Laptop', 'AirPods Pro', 'PlayStation 5', 'Nintendo Switch', 'iPad Pro', 'Galaxy Tab S7', 'Dell XPS 13', 'Apple Watch', 'Bose Headphones', 'GoPro Hero 9', 'Fitbit Charge 4', 'Kindle Paperwhite', 'Amazon Echo', 'Ring Doorbell', 'Google Nest Hub', 'Sony WH-1000XM4'],
            'product_price': [799.00, 699.99, 1299.00, 799.00, 999.00, 249.99, 499.99, 299.99, 799.00, 649.99, 999.99, 399.00, 299.99, 399.99, 149.95, 129.99, 99.99, 199.99, 89.99, 349.99],
            'quantity': [1, 1, 1, 2, 1, 1, 1, 2, 1, 1, 1, 1, 2, 1, 2, 1, 1, 1, 1, 1]
        })
        self.data['revenue'] = self.data['product_price'] * self.data['quantity']

    def test_monthly_revenue(self):
        expected = pd.Series([1498.99, 2897.00, 1248.99, 1099.97, 1448.99, 1398.99, 599.98, 699.89, 229.98, 289.98, 349.99], index=['2021-01', '2021-02', '2021-03', '2021-04', '2021-05', '2021-06', '2021-07', '2021-08', '2021-09', '2021-10', '2021-11'], name='revenue')
        result = compute_monthly_revenue(self.data)
        logger.info(f"Expected Monthly Revenue:\n{expected}")
        logger.info(f"Actual Monthly Revenue:\n{result}")
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_product_revenue(self):
        expected = pd.Series([2397.00, 699.99, 1299.00, 999.00, 249.99, 499.99, 599.98, 799.00, 649.99, 999.99, 399.00, 599.98, 399.99, 299.90, 129.99, 99.99, 199.99, 89.99, 349.99], index=['iPhone 12', 'Galaxy S21', 'MacBook Pro', 'Surface Laptop', 'AirPods Pro', 'PlayStation 5', 'Nintendo Switch', 'iPad Pro', 'Galaxy Tab S7', 'Dell XPS 13', 'Apple Watch', 'Bose Headphones', 'GoPro Hero 9', 'Fitbit Charge 4', 'Kindle Paperwhite', 'Amazon Echo', 'Ring Doorbell', 'Google Nest Hub', 'Sony WH-1000XM4'], name='revenue')
        result = compute_product_revenue(self.data)
        logger.info(f"Expected Product Revenue:\n{expected}")
        logger.info(f"Actual Product Revenue:\n{result}")
        pd.testing.assert_series_equal(result.sort_index(), expected.sort_index(), check_names=False)

    def test_customer_revenue(self):
        expected = pd.Series([2897.00, 2348.98, 2197.98, 379.98, 599.98, 799.97, 1089.98, 748.99, 399.99, 299.90], index=[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010], name='revenue')
        result = compute_customer_revenue(self.data)
        logger.info(f"Expected Customer Revenue:\n{expected}")
        logger.info(f"Actual Customer Revenue:\n{result}")
        pd.testing.assert_series_equal(result, expected, check_names=False)

    def test_top_10_customers(self):
        expected = pd.Series([2897.00, 2348.98, 2197.98, 379.98, 599.98, 799.97, 1089.98, 748.99, 399.99, 299.90], index=[1001, 1002, 1003, 1004, 1005, 1006, 1007, 1008, 1009, 1010], name='revenue')
        result = compute_top_10_customers(self.data)
        logger.info(f"Expected Top 10 Customers:\n{expected}")
        logger.info(f"Actual Top 10 Customers:\n{result}")
        pd.testing.assert_series_equal(result.sort_index(), expected.sort_index(), check_names=False)

if __name__ == '__main__':
    unittest.main()
