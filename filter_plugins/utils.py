class FilterModule(object):
    def filters(self):
        return {
            "php_pkg_list": self.php_pkg_list,
        }

    @staticmethod
    def php_pkg_list(mods: list, version: str) -> list:
        # much faster than looping inside ansible
        return [f"php{version}-{mod}" for mod in mods]
