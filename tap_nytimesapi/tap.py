"""nytimesAPI tap class."""

import os, sys
sys.path.append(os.path.abspath(os.path.join('..')))
from typing import List

from singer_sdk import Tap, Stream
from singer_sdk.typing import (
    PropertiesList,
    Property,
    StringType,
    DateTimeType)


from tap_nytimesapi.streams import (
    nytimesAPIStream,
)

STREAM_TYPES = [
    nytimesAPIStream,
]

class TapNyTimesAPI(Tap):
    """nytimesAPI tap class."""
    name = "tap-nytimesapi"

    config_jsonschema = PropertiesList(
        Property("api_key", StringType, required=True,
            description="The token to authenticate against the API service"
        ),
        Property("section", StringType, required=True,
            description="The section of the API to query"
        ),
        Property(
            "start_date", DateTimeType,
            description="The earliest record date to sync"
        ),
    ).to_dict()
    
    def discover_streams(self) -> List[Stream]:
        """Return a list of discovered streams."""
        return [stream_class(tap=self) for stream_class in STREAM_TYPES]

cli = TapNyTimesAPI.cli