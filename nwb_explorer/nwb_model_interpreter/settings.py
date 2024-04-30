from pynwb import TimeSeries
from pynwb.image import ImageSeries
from pynwb.ophys import RoiResponseSeries

SUPPORTED_TIME_SERIES_TYPES = (
    RoiResponseSeries, ImageSeries, TimeSeries)
# Assuming numerical or image time series only for now

path_separator = '.'