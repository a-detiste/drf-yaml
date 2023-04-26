from pathlib import Path

import toml
from django.test import TestCase

import drf_yaml


class _VersionTests(TestCase):
    """Tests specific to the package version."""

    def test_versions_are_in_sync(self) -> None:
        """Ensure that the version on pyproject.toml and package.__init__.py match."""
        path = Path(__file__).parent.parent / "pyproject.toml"
        pyproject = toml.loads(path.read_text())
        pyproject_version = pyproject["tool"]["poetry"]["version"]

        package_init_version = drf_yaml.__version__

        self.assertEqual(package_init_version, pyproject_version)
