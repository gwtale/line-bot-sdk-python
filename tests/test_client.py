# -*- coding: utf-8 -*-

import responses

from linebot.client import LineBotClient


class TestLineBotClient():
    def test_client_instance_creation(self, fx_channel_id, fx_channel_secret, fx_channel_mid):
        credentials = {
            'channel_id': fx_channel_id,
            'channel_secret': fx_channel_secret,
            'channel_mid': fx_channel_mid,
        }
        LineBotClient(**credentials)

    @responses.activate
    def test_send_text(self, fx_client, mocking):
        response = fx_client.send_text(to_mid=[mocking['mid']], text='')
        assert response.status_code == 200
