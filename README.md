# python-package-tutorial

### Introduction

In order to release your python code you need to package it building a python package.

Do exist two different type of python packages:

1. **Source distribution**: (called `sdist`) is a compressed archive file of the source code with an extension `tgz`, `tar.gz`
2. **Binary distribution**: (called `wheel`) is a binary file with an extension `.whl`

Main difference between those two artifcats is that a source distribution allows most anyone to build your code on their platform, a binary
distribution is prebuilt for a given platform and saves users the work of building it themselves.

Now python packages building process involves two main actors:

1. A **build frontend:** it's just an interface between you and a build backend. [build](https://github.com/pypa/build) package is a build frontend and you'll need to install to follow this tutorial
2. A **build backend**: it makes real dirty work of building artifacts (sdist or wheel). [setuptools](https://github.com/pypa/setuptools) is a build backend and we'll use it during this tutorial

A build frontend and a build backend talk with each other throug an interface defined in [PEP 517](https://www.python.org/dev/peps/pep-0517/#build-backend-interface).


```
   +------------+
   |    build   |
   |    (BE)    |
   +------------+
         ||
         \/
   +------------+
   |   PEP 517  |
   | (interface)|
   +------------+
         ||
         \/
   +------------+
   | setuptools |
   |    (BE)    |
   +------------+
   
```

In order to create a binary distribution (wheel) `setuptools` uses [wheel](https://github.com/pypa/wheel) package.

`build-->setuptools-->wheel-->.whl`

Altenatives build backends are for example: [poetry](https://python-poetry.org/) and [flit](https://flit.readthedocs.io/)

In this way you can change build backend used by build frontend, but how/where to specify which build backend you wanna use?

According to [PEP 518](https://www.python.org/dev/peps/pep-0518/#specification) `pyproject.toml` is default configuartion file where you can define which build backend will be used and its dependecies (for example we said that setuptools uses wheel to build binary distrubution so wheel must be defined as setuptools's dependecy in `pyproject.toml` to make building process working)

Two other files as important as `pyproject.toml` in building process are:
* `setup.py` (dynamic): setup.py is the **build script** for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include
* `setup.cfg` (static): is the **configuration file** for setuptools. It tells setuptools about your package (such as the name and version) as well as which code files to include. Eventually much of this configuration may be able to move to pyproject.toml.

They are basically used to define **metadata of your package** that will be consumed by build backend (setuptools)

So at this point we could say: there are **two types of metadata**: static and dynamic.
* **Static metadata** (`setup.cfg`): guaranteed to be the same every time. This is simpler, easier to read, and avoids many common errors, like encoding errors.
* **Dynamic metadata** (`setup.py`): possibly non-deterministic. Any items that are dynamic or determined at install-time, as well as extension modules or extensions to setuptools, need to go into setup.py.

Static metadata (`setup.cfg`) should be preferred. Dynamic metadata (`setup.py`) should be used only as an escape hatch when absolutely necessary. setup.py used to be required, but can be omitted with newer versions of setuptools and pip

As mentioned in [official python documentation](https://packaging.python.org/en/latest/tutorials/packaging-projects/#configuring-metadata) `pyproject.toml` + `setup.cfg` should be always preferred rather than `setup.py`

### Tutorial

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
* Add in `setup.cfg` under `[metadata]` section  [commit](https://github.com/kinderp/python-package-tutorial/commit/2d81fe55b08e87aba15ecd94f8a8f7d6ab548dd8)
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

* Add in `setup.cfg` under `[metadata]` section [commit](https://github.com/kinderp/python-package-tutorial/commit/83722af669350204c27e66efe2ed6060ff616b51)
  * url
  * author
  * author_email

* Add in `setup.cfg` under `[metadata]` section [commit](https://github.com/kinderp/python-package-tutorial/commit/e190b1e20f1a08a4c558de1e189b665272554dab)
  * description

* Add in `setup.cfg` under `[metadata]` section [commit](https://github.com/kinderp/python-package-tutorial/commit/a0cd6c453a69e008dea94b5c123a240b0976cbd1)
  * long_description
  * long_description_content_type
  
* Add a LICENCE file in root dir [commit](https://github.com/kinderp/python-package-tutorial/commit/817109cfb5cbd46a271036b21cc2dc650e16ec5b)

* Add in `setup.cfg` under `[metadata]` section [commit](https://github.com/kinderp/python-package-tutorial/commit/973086d556af285caf9d96b96288e003d940d5a7)
  * license
  * license_files
  * classifiers

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


* Add a package layout like this [commit](https://github.com/kinderp/python-package-tutorial/commit/0c443bbdad22e335ddb0507f03824736d16009e2)
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

* Add options in `setup.cfg` to inform setuptools how/where to find your packages [commit](https://github.com/kinderp/python-package-tutorial/commit/eeb5be3bd0b5807f1c6b5175afc3857cdca067c1)

* Add a new file `data.json` to show how to add non python code [commit](https://github.com/kinderp/python-package-tutorial/commit/a7ae1b721cc957d31318dfedaf8bb0436413311f)

* Add `MANIFEST.in` [commit](https://github.com/kinderp/python-package-tutorial/commit/f50cc86d97d0f61e1a6fe988c4f342fa2e37afb3)

* Run again building process and check dist content, you can see your new package and `data.json` there
  ```
  rm -rf dist && pyproject-build
  ```
  
  ```
  tar -ztvf dist/first-python-package-0.0.1.tar.gz
  drwxrwxr-x antonio/antonio   0 2022-01-04 11:39 first-python-package-0.0.1/
  -rw-rw-r-- antonio/antonio 1092 2021-12-23 15:25 first-python-package-0.0.1/LICENSE
  -rw-rw-r-- antonio/antonio   50 2021-12-23 16:21 first-python-package-0.0.1/MANIFEST.in
  -rw-rw-r-- antonio/antonio 4835 2022-01-04 11:39 first-python-package-0.0.1/PKG-INFO
  -rw-rw-r-- antonio/antonio 4447 2021-12-23 15:35 first-python-package-0.0.1/README.md
  -rw-rw-r-- antonio/antonio   90 2021-12-23 15:06 first-python-package-0.0.1/pyproject.toml
  -rw-rw-r-- antonio/antonio  575 2022-01-04 11:39 first-python-package-0.0.1/setup.cfg
  drwxrwxr-x antonio/antonio    0 2022-01-04 11:39 first-python-package-0.0.1/src/
  drwxrwxr-x antonio/antonio    0 2022-01-04 11:39 first-python-package-0.0.1/src/first_python_package.egg-info/
  -rw-rw-r-- antonio/antonio 4835 2022-01-04 11:39 first-python-package-0.0.1/src/first_python_package.egg-info/PKG-INFO
  -rw-rw-r-- antonio/antonio  350 2022-01-04 11:39 first-python-package-0.0.1/src/first_python_package.egg-info/SOURCES.txt
  -rw-rw-r-- antonio/antonio    1 2022-01-04 11:39 first-python-package-0.0.1/src/first_python_package.egg-info/dependency_links.txt
  -rw-rw-r-- antonio/antonio    7 2022-01-04 11:39 first-python-package-0.0.1/src/first_python_package.egg-info/top_level.txt
  drwxrwxr-x antonio/antonio    0 2022-01-04 11:39 first-python-package-0.0.1/src/imppkg/
  -rw-rw-r-- antonio/antonio    0 2021-12-23 15:34 first-python-package-0.0.1/src/imppkg/__init__.py
  -rw-rw-r-- antonio/antonio    0 2021-12-23 16:23 first-python-package-0.0.1/src/imppkg/data.json
  -rw-rw-r-- antonio/antonio    0 2021-12-23 15:34 first-python-package-0.0.1/src/imppkg/hello.py
  -rw-rw-r-- antonio/antonio    0 2021-12-23 16:05 first-python-package-0.0.1/src/imppkg/test_exclude_me_from_dist.py
  ```

* Even if `data.json` has been included into source distribution, it's still missing in .whl
  ```
  unzip -l dist/first_python_package-0.0.1-py3-none-any.whl
  Archive:  dist/first_python_package-0.0.1-py3-none-any.whl
    Length      Date    Time    Name
  ---------  ---------- -----   ----
          0  2021-12-23 14:34   imppkg/__init__.py
          0  2021-12-23 15:23   imppkg/data.json
          0  2021-12-23 14:34   imppkg/hello.py
          0  2021-12-23 15:05   imppkg/test_exclude_me_from_dist.py
       1092  2022-01-04 10:39   first_python_package-0.0.1.dist-info/LICENSE
       4835  2022-01-04 10:39   first_python_package-0.0.1.dist-info/METADATA
         92  2022-01-04 10:39   first_python_package-0.0.1.dist-info/WHEEL
          7  2022-01-04 10:39   first_python_package-0.0.1.dist-info/top_level.txt
        750  2022-01-04 10:39   first_python_package-0.0.1.dist-info/RECORD
  ---------                     -------
       6776                     9 files

  ```

* Set `include_package_data = True` in setup.cfg to include non python files in source distrubution into binary one [commit](https://github.com/kinderp/python-package-tutorial/commit/6ae8937b1c11170826d454048d34f41f33e2e837)


## Handling package dependencies and entrypoint

* Add a main module: `src/imppkg/say.py` [commit](https://github.com/kinderp/python-package-tutorial/commit/282c1ce258a00ab053e01fd96c5c485478762ec0)

  Now we have an entrypoint for our project `src.imppkg.say.main()`, some new code has been added in `src/imppkg/hello.py` in order to be able our project to do something: it just receives in input a language (a language code following [iso639-1](https://it.wikipedia.org/wiki/ISO_639?uselang=it)) and print `Hello World` translated in that language.
  In order to test you need to create a vevn and install say hello in your venv. Run donw below command in say hello root dir in order to respectively:
  
  * create a venv
  * activate a venv
  * install say hello in a venv 
  
  ```
  python3 -m venv .venv
  ```
  
  ```
  source .venv/bin/activate
  ```
  
  ```
  pip install .
  ```
  
  At this point you have say hello installed in your env (and venv is activated under your fingers) and you can test it in this way:
  
  ```
  python -m imppkg.say DE
  Traceback (most recent call last):
  File "/home/antonio/.pyenv/versions/3.9.0/lib/python3.9/runpy.py", line 197, in _run_module_as_main
    return _run_code(code, main_globals, None,
  File "/home/antonio/.pyenv/versions/3.9.0/lib/python3.9/runpy.py", line 87, in _run_code
    exec(code, run_globals)
  File "/home/antonio/dev/python-package-tutorial/.venv/lib/python3.9/site-packages/imppkg/say.py", line 3, in <module>
    from imppkg.hello import say_hello
  File "/home/antonio/dev/python-package-tutorial/.venv/lib/python3.9/site-packages/imppkg/hello.py", line 1, in <module>
    from googletrans import Translator
  ModuleNotFoundError: No module named 'googletrans'

  ```
  
  As you can see we didn't include googletrans as depencencies of your project, we use it to translate `Hello World`.
  Let's add googletrans as dep in our project
  
* Add `install_requires` key of the `[options]` section in the `setup.cfg` [commit](https://github.com/kinderp/python-package-tutorial/commit/2846e9453e699af973af62b88076e43c59c7ff3c)
  
* Now let's remove our venv 
  ```
  rm -rf .venv
  ```
* Create a new venv and install our project again
    ```
  python3 -m venv .venv
  ```
  
  ```
  source .venv/bin/activate
  ```
  
  ```
  pip install .
  ```
  
* Run it again 
  ```
  python -m imppkg.say DE
  Hallo Welt
  ```
As you can see above you're running our project as module but we'd like to have a command called `say` installed in `bin` in order to execute our project just typing `say DE`. In order to do that we need to add an entrypoint in `setup.cfg`

