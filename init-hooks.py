import shutil, os
files = ['hooks/pre-commit']
for f in files:
    print('copying: ', f)
    shutil.copy(f, '.git/hooks')
