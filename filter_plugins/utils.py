class FilterModule(object):
    def filters(self):
        return {
            "ensure_list": self.ensure_list,
            "php_pkg_list": self.php_pkg_list,
        }

    @staticmethod
    def php_pkg_list(mods: list, version: str) -> list:
        # much faster than looping inside ansible
        return [f"php{version}-{mod}" for mod in mods]

    @staticmethod
    def ensure_list(data: (str, list)) -> list:
        # if user supplied a string instead of a list => convert it to match our expectations
        if isinstance(data, list):
            return data

        return [data]

