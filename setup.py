"""
  tpkit.setup
  ~~~~~~~~~~~
"""

from setuptools import setup

PACKAGE_NAME = 'tpkit'

with open('requirements.txt') as f:
  requirements = f.read().splitlines()

print(requirements)

setup(
  name=PACKAGE_NAME,
  package_dir={PACKAGE_NAME: 'src'}, # source files are in the repos's root directory
  install_requires=requirements, # requirements outlined in `requirements.txt`
  scripts=['./commands/text']
)
