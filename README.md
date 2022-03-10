# ipynb-clear-test

implementing tutorial: https://zhauniarovich.com/post/2020/2020-10-clearing-jupyter-output-p2/


## Setup
Initialize pre-commit hook by running one of the two init scripts: 

- bash
> . ./init-hooks
- python
> python init-hooks.py

Then when you run `git commit` you will see something along the lines of: 
```
> git commit -am "a test commit"
Processing file: 'my-nb.ipynb'
[NbConvertApp] Converting notebook my-nb.ipynb to notebook
[NbConvertApp] Writing 1091 bytes to my-nb.ipynb
No ipynb files were modified!
[neilo e92e9ce] a test commit
 4 files changed, 68 insertions(+), 190 deletions(-)
 create mode 100644 init-hooks
 create mode 100644 init-hooks.py
 rewrite my-nb.ipynb (70%)
 delete mode 100644 pre-commit
```
