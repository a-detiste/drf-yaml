# How to create a new release

- Create a new branch.
- Update version on `drf_yaml/__init__.py`.
- Update version on `pyproject.toml`.
- Update CHANGELOG.md
    - Add new version below unreleased
    - Move unreleased to new version
    - Add compare link on the bottom
- Commit
- Push
- Fix any CI issues
- Run `poetry run mike deploy --update-aliases <version> latest --push`
- Merge
- Create github release
- Profit
