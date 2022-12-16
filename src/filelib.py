"""
  tpkit.functional
  ~~~~~~~~~~~~~~~~

This module is useful when working with files.
"""

from typing import Iterator, List
from pathlib import PosixPath

def iterate_paths(directory) -> Iterator[PosixPath]:
  """
  generates a posix path for each file in the given directory
  """
  for file_name in os.listdir(directory):
    absolute_path = os.path.join(directory, file_name)
    yield pathlib.Path(absolute_path).resolve()

def get_paths(directory) -> List[PosixPath]:
  """
  returns a list containing the posix path of every file in the given directory
  """
  return list(iterate_paths)

def crawl(directory) -> Iterator[PosixPath]:
  """
  generates a posix path for every (non-directory) file contained 
  inside the nested directory structure of the given directory
  """
  for path in iterate_paths(directory):
    if os.path.isdir(path):
      yield from crawl(path)
    else:
      yield path
