import unittest
import make_requests
from unittest.mock import patch, mock_open
import json
from io import StringIO
# sample_json = StringIO( ' your_existing_dict ') 


class TestRequest(unittest.TestCase):

    def test_url(self):
        result = make_requests.test_url()
        self.assertRaisesRegex(ValueError, r'[a-zA-Z0-9.-]+\.(com|edu|net|gov)')
    

    def test_load_json(self):
        sample_json = StringIO ('{"name": "John", "shares": "100", "price": 1230.23}')

        with patch('urllib.request.urlopen') as url_patch:
            with patch('json.load') as j_patch:
                url_patch.return_value.__enter__.return_value = sample_json
                res = make_requests.load_json('test', file_counter=0)
                j_patch.assert_called_with({})
            # print(res)
            # self.assertDictEqual(res, {'name': 'John', 'shares': '100', 'price': 1230.23})


        # def test_read_file_data(self):
        #     import json
        #     sample_json = {
        #         'name': 'John',
        #         'shares': 100,
        #         'price': 1230.23
        #     }
        #     sample_json = json.dump(sample_json)
        #     path = / path / to / file
        #     filename = testcase.json
        #     self.assertEqual(read_file_data(filename, path), sample_json)




if __name__ == '__main__':
    unittest.main()