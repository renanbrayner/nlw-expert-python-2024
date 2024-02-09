from pathvalidate import sanitize_filename


class PathHandler:
    def sanatize_name(self, path: str) -> str:
        return sanitize_filename(path)
