from zipfile import ZipFile
file_name = 'IntroTpPython.zip'

with ZipFile(file_name, 'r') as zip:
  zip.extractall()
  print('Done')
