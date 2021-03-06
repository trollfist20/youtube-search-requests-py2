# youtube-search-requests_py2
# async_search.py

from youtube_search_requests_py2.utils.errors import UnsupportedPython

class AsyncYoutubeSearch:
    """

    **Same as YoutubeSearch, but with async method**

    AsyncYoutubeSearch arguments

    search_query: :class:`str`
        a string terms want to search
    max_results: :class:`int` (optional, default: 10)
        maximum search results
    timeout: :class:`int` or :class:`NoneType` (optional, default: None)
        give number of times to execute search, if times runs out, search stopped & returning results
    json_results: :class:`bool` (optional, default: False)
        if True, Return results in json format. If False return results in dict format
    include_related_videos: :class:`bool` (optional, default: False)
        include all related videos each url's
    async_youtube_session: :class:`AsyncYoutubeSession` (optional, default: None)
        a async session for youtube.
        NOTE: AsyncYoutubeSearch require AsyncYoutubeSession in order to work !
    safe_search: :class:`bool` (optional, default: False)
        This helps hide potentially mature videos.
        No filter is 100% accurate.
    """
    def __init__(self):
        raise UnsupportedPython('python 2 is not support to use async method. Please Upgrade your python.')

    def _wrap_json(self):
        pass

    def request_search(self):
        pass

    def main(self):
        pass

    def _search(self, timeout=None):
        pass

    def search(self):
        pass