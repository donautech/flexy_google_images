from pkg_resources import get_distribution, DistributionNotFound

try:
    __version__ = get_distribution('flexy_google_images').version
except DistributionNotFound:
    __version__ = '(local)'
