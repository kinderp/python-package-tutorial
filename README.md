# python-package-tutorial

* Install `pyproject-build`
  ```
  pip install build
  ```
* Check your installation
  ```
  pyproject-build --version
  ```
* Run build process
  ```  
  pyproject-build
  ```
  ```
  ERROR Source /home/antonio/dev/python-package-tutorial does not appear to be a Python project: no pyproject.toml or setup.py
  ```
* Create a `pyproject.toml`
  ```
  touch pyproject.toml
  ```
* Run build process
  ```
  pyproject-build
  ```
  ```
  * Creating venv isolated environment...
  * Installing packages in isolated environment... (setuptools >= 40.8.0, wheel)
  * Getting dependencies for sdist...
  running egg_info
  creating UNKNOWN.egg-info
  writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
  writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
  * Building sdist...
  running sdist
  running egg_info
  writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
  running check
  warning: check: missing required meta-data: name, url

  warning: check: missing meta-data: either (author and author_email) or (maintainer and maintainer_email) should be supplied

  creating UNKNOWN-0.0.0
  creating UNKNOWN-0.0.0/UNKNOWN.egg-info
  copying README.md -> UNKNOWN-0.0.0
  copying pyproject.toml -> UNKNOWN-0.0.0
  copying UNKNOWN.egg-info/PKG-INFO -> UNKNOWN-0.0.0/UNKNOWN.egg-info
  copying UNKNOWN.egg-info/SOURCES.txt -> UNKNOWN-0.0.0/UNKNOWN.egg-info
  copying UNKNOWN.egg-info/dependency_links.txt -> UNKNOWN-0.0.0/UNKNOWN.egg-info
  copying UNKNOWN.egg-info/top_level.txt -> UNKNOWN-0.0.0/UNKNOWN.egg-info
  Creating tar archive
  removing 'UNKNOWN-0.0.0' (and everything under it)
  * Building wheel from sdist
  * Creating venv isolated environment...
  * Installing packages in isolated environment... (setuptools >= 40.8.0, wheel)
  * Getting dependencies for wheel...
  running egg_info
  writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
  * Installing packages in isolated environment... (wheel)
  * Building wheel...
  running bdist_wheel
  running build
  running install
  running install_egg_info
  running egg_info
  writing manifest file 'UNKNOWN.egg-info/SOURCES.txt'
  Copying UNKNOWN.egg-info to build/bdist.linux-x86_64/wheel/UNKNOWN-0.0.0-py3.7.egg-info
  running install_scripts
  Successfully built UNKNOWN-0.0.0.tar.gz and UNKNOWN-0.0.0-py3-none-any.whl
  ```
* List root directory a new `dist` dir has been created for you, it cointains your package
  ```
  ls -al .
  total 4
  drwxrwxr-x 1 antonio antonio  106 Dec 23 14:52 .
  drwxrwxr-x 1 antonio antonio 1852 Dec 23 14:45 ..
  drwxrwxr-x 1 antonio antonio  100 Dec 23 14:51 dist
  drwxrwxr-x 1 antonio antonio  138 Dec 23 14:45 .git
  drwxrwxr-x 1 antonio antonio   56 Dec 23 14:46 .myenv
  -rw-rw-r-- 1 antonio antonio    0 Dec 23 14:50 pyproject.toml
  -rw-rw-r-- 1 antonio antonio 2037 Dec 23 14:52 README.md
  drwxrwxr-x 1 antonio antonio  104 Dec 23 14:51 UNKNOWN.egg-info
  ```
* `dist` contains:
   * `UNKNOWN-0.0.0.tar.gz` source distrubtion
   * `UNKNOWN-0.0.0-py3-none-any.whl` binary destribution (wheel)
  ```
  ls -al dist
  total 8
  drwxrwxr-x 1 antonio antonio 100 Dec 23 14:51 .
  drwxrwxr-x 1 antonio antonio 106 Dec 23 14:54 ..
  -rw-rw-r-- 1 antonio antonio 961 Dec 23 14:51 UNKNOWN-0.0.0-py3-none-any.whl
  -rw-rw-r-- 1 antonio antonio 686 Dec 23 14:51 UNKNOWN-0.0.0.tar.gz
  ```

* Create `setup.cfg`
  ```
  touch setup.cfg
  ```
* Add `[metadata]` section in `setup.cfg` [commit](https://github.com/kinderp/python-package-tutorial/commit/2d81fe55b08e87aba15ecd94f8a8f7d6ab548dd8)
  * name
  * version

* Run build process again
  ```
  rm -rf dist
  pyproject-build
  ```
* Now our package has its own `name` and `version`
  ```
  ls -al dist
  total 8
  drwxrwxr-x 1 antonio antonio  152 Dec 23 15:09 .
  drwxrwxr-x 1 antonio antonio  182 Dec 23 15:09 ..
  -rw-rw-r-- 1 antonio antonio 1101 Dec 23 15:09 first_python_package-0.0.1-py3-none-any.whl
  -rw-rw-r-- 1 antonio antonio 1481 Dec 23 15:09 first-python-package-0.0.1.tar.gz
  ```

* Check its content, you'have an empty package, let's add some code
  ```
  tar -ztvf dist/first-python-package-0.0.1.tar.gz
  drwxrwxr-x antonio/antonio   0 2021-12-23 15:09 first-python-package-0.0.1/
  -rw-rw-r-- antonio/antonio 145 2021-12-23 15:09 first-python-package-0.0.1/PKG-INFO
  -rw-rw-r-- antonio/antonio 2862 2021-12-23 15:09 first-python-package-0.0.1/README.md
  drwxrwxr-x antonio/antonio    0 2021-12-23 15:09 first-python-package-0.0.1/first_python_package.egg-info/
  -rw-rw-r-- antonio/antonio  145 2021-12-23 15:09 first-python-package-0.0.1/first_python_package.egg-info/PKG-INFO
  -rw-rw-r-- antonio/antonio  210 2021-12-23 15:09 first-python-package-0.0.1/first_python_package.egg-info/SOURCES.txt
  -rw-rw-r-- antonio/antonio    1 2021-12-23 15:09 first-python-package-0.0.1/first_python_package.egg-info/dependency_links.txt
  -rw-rw-r-- antonio/antonio    1 2021-12-23 15:09 first-python-package-0.0.1/first_python_package.egg-info/top_level.txt
  -rw-rw-r-- antonio/antonio   90 2021-12-23 15:06 first-python-package-0.0.1/pyproject.toml
  -rw-rw-r-- antonio/antonio   94 2021-12-23 15:09 first-python-package-0.0.1/setup.cfg
  ```


* Add a package layout like this
  ```
  ├── LICENSE
  ├── pyproject.toml
  ├── README.md
  ├── setup.cfg
  ├── src
  │   └── imppkg
  │       ├── hello.py
  │       └── __init__.py
  └── test
  ```
