import re

class Remote:

    def __init__(self, remote):
        self.remote = remote

    def repo_url(self):
        return self._add_path(self._remove_dot_git(self._parse_https(self.remote)))

    def _parse_https(self, remote):
        match = re.search('^git@(.*?):', remote)
        if match:
            to_replace = match.group(0)
            domain = 'https://{}/'.format(match.group(1))
            remote = remote.replace(to_replace, domain)

        return remote

    def _remove_dot_git(self, url):
        return '.git'.join(url.rsplit('.git')[:-1])

    def _add_path(self, url):
        return '{}/tree/master'.format(url)
