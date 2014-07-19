#!/usr/bin/env python3
import tempfile
import shutil
import os
from os import path


APP_NAME = 'files'

with tempfile.TemporaryDirectory() as tempdir:
    os.system('git clone .. %s/%s' % (tempdir, APP_NAME))
    shutil.rmtree(path.join(tempdir, APP_NAME, '.git'))
    shutil.make_archive(path.join(os.getcwd(), '..', APP_NAME), 'zip', root_dir=tempdir)
