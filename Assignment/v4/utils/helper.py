from utils import message
import numpy as np

class Helper:
    @staticmethod
    def check_if_customer_exist(customer_id, customers):
        """
        :param customer_id:
        :param customers:
        :return:
        """
        customer_found = next(
            (customer for customer in customers if customer.get('customer_id') == customer_id), None
        )

        if customer_found is not None:
            return customer_found

        print(f"{message.status_404}\n- Customer with ID {customer_id} not found.\n")

    @staticmethod
    def check_if_customer_exist_np(customer_id, customers):
        # Convert the list of dictionaries to a NumPy structured array
        dtype = [('customer_id', int)]
        customer_id_array = np.array([(customer['customer_id']) for customer in customers], dtype=dtype)

        # Use NumPy to find the customer
        customer_found = np.where(customer_id_array['customer_id'] == customer_id)

        if customer_found[0].size > 0:
            return customer_id_array[customer_found][0]

        print(f"{message.status_404}\n- Customer with ID {customer_id} not found.\n")

