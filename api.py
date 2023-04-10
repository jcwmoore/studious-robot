from datetime import datetime
from typing import Optional, Any, Dict
import time

class PolygonFreeApi:
    last_call = datetime(datetime.today().year, datetime.today().month, datetime.today().day) 
    
    def __init__(self, api_key: Optional[str] = ..., connect_timeout: float = 10, read_timeout: float = 10, num_pools: int = 10, retries: int = 3, base: str = ..., verbose: bool = False, custom_json: Optional[Any] = None):
        super().__init__(api_key, connect_timeout, read_timeout, num_pools, retries, base, verbose, custom_json)
        self.BASE = 'https://api.polygon.io'
    
    def _get(self, path: str, params: Optional[dict] = None, result_key: Optional[str] = None, deserializer=None, raw: bool = False, options: Optional[RequestOptionBuilder] = None) -> Any:
        now = datetime.now()
        time_diff = now - PolygonFreeApi.last_call
        if time_diff.seconds < 13:
            time.sleep(13 - time_diff.seconds)

        response = super()._get(path, params, result_key, deserializer, raw, options)
        PolygonFreeApi.last_call = datetime.now()
        return response
    

if __name__ == '__main__':
    symbols = ['FB']

    client = PolygonFreeApi('')
    for s in symbols:
        res = client.get_daily_open_close_agg(ticker=s, date=datetime(2023,4,6).strftime('%Y-%m-%d'))
        client.list_dividends
        print(res)