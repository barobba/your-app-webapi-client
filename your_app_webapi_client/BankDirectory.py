
import requests

from your_app_webapi_client.models.Account import Account
from your_app_webapi_client.BaseClient import BaseClient
from your_app_webapi_client import helper


class BankDirectory (BaseClient):

    def create(self, first, last, balance):

        response = requests.post(
            url=f'{self.base_url}/account',
            headers=helper.prepare_headers(),
            json={'first': first, 'last': last, 'balance': balance}
        )

        helper.validate_response(response)

        return Account(**response.json())

    def read_list(self):

        response = requests.get(
            url=f'{self.base_url}/account',
            headers=helper.prepare_headers()
        )

        helper.validate_response(response)

        return [Account(**kwargs) for kwargs in response.json()]

    def read(self, account_id):

        response = requests.get(
            url=f'{self.base_url}/account/{account_id}',
            headers=helper.prepare_headers()
        )

        helper.validate_response(response)

        return Account(**response.json())

    def update(self):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError
