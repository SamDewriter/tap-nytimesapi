"""Stream type classes for tap-nytimesapi."""

from pathlib import Path
import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from typing import Iterable
import requests

from singer_sdk.helpers.jsonpath import extract_jsonpath
from singer_sdk.streams import RESTStream


class nytimesAPIStream(RESTStream):
    """nytimesAPI stream class."""

    @property
    def url_base(self) -> str:
    #     """Return the API URL root, configurable via tap settings."""
        url_base = "https://api.nytimes.com/svc/search/v2"

        api_url = f"{url_base}/{self.config['section']}/.json?api-key={self.config['api-key']}"
        
        return api_url

    records_jsonpath = "$[*]"  # Or override `parse_response`.

    def parse_response(self, response: requests.Response) -> Iterable[dict]:
            """Parse the response and return an iterator of result rows."""
            
            query_url = self.url_base()
            r = requests.get(query_url)
            
            yield from extract_jsonpath(self.records_jsonpath, input=r.json())
