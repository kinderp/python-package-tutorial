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

* Add an `entry_point` in `setup.cfg`, a command called `say` will be avaible in `bin` after a new installation [commit](https://github.com/kinderp/python-package-tutorial/commit/14070f8ac7e437f1556a4c96071dc8fadac988a8). Remove `.venv` and re-create a new one as you did before, then activate it and run `say` in this way:
  ```
  .venv/bin/say DE
  Hallo Welt
  ```
  
  ## Add a test suite
  
  In order to biuld a test seuite you'll need a test runner. We'll use `pytest`(`python -m pytest`)
  
  * Add pytest's configuration in `setup.cfg` [commit](https://github.com/kinderp/python-package-tutorial/commit/23ce412602f08a82da78eb0ca8840ebd7cb4c385)
    * add `testpaths` under `[tool:pytest]`
    
    ```
    pytest is looking everywhere under the package’s root directory for tests
    To  encourage  placement of tests in the appropriate location, you should
    configure pytest to look only in the test/ directory.You can add configur
    ation for pytest into your package’s setup.cfg  file  using a new section
    called [tool:pytest] . The testpaths key maps to a list of paths in which
    to look for tests. You need just one: test .After you add this configurat
    ion,pytest should confirm in its output both that it’s using setup.cfg as
    the  configuration  file  and  that  it found the testpaths configuration
    ```

    ```
    [tool:pytest]
    testpaths = test
    ```
  * Add a simple `assert True` to mock a test suite [commit](https://github.com/kinderp/python-package-tutorial/commit/fad6f4e4b9dc43667acc2ed8660aacd1c1c00a68)
  * Run `python -m pytest`, you'll get an error like below, fix it just importing your packages as done in this [commit](https://github.com/kinderp/python-package-tutorial/commit/abbdda1320d12968ad2aba070ec6e791ae52a173)
    ```
    Module imppkg was never imported. (module-not-imported)
    ```
  * Now Run pytest agaiin, it should work having your test suite up and running

## Add test coverage measurement

* Install `pytest-cov`
* Try it just running `python -m pytest --cov`
* You can specify on which module (we have one module: `imppkg`) --cov should measure test coverage in this way: `python -m pytest --cov=imppkg`  
* Add branch coverage [commit](https://github.com/kinderp/python-package-tutorial/commit/02a00eab913504f51ccf18b2a71fb75abea662fa)

  ```
  It enables branch coverage, in other words how many
  alternative execution paths are possible, and which
  of those paths are untested.

  To configure branch coverage for your tests, add  a
  new section to setup.cfg called [coverage:run] . In
  this section, add a branch key with a value of  True
  This produces two new columns in the coverage output

  - Branch : how many branches exist through the code
  - BrPart : how many branches are only partially covered by tests

  python -m pytest --cov=imppkg

  test/test_translations.py .     [100%]

  ----------- coverage: platform linux, python 3.9.0-final-0 -----------
  Name                                                                    Stmts   Miss Branch BrPart  Cover
  ---------------------------------------------------------------------------------------------------------
  .venv/lib/python3.9/site-packages/imppkg/__init__.py                        0      0      0      0   100%
  .venv/lib/python3.9/site-packages/imppkg/hello.py                           4      1      0      0    75%
  .venv/lib/python3.9/site-packages/imppkg/say.py                            18     12      4      1    32%
  .venv/lib/python3.9/site-packages/imppkg/test_exclude_me_from_dist.py       0      0      0      0   100%
  ---------------------------------------------------------------------------------------------------------
  TOTAL                                                                      22     13      4      1    38%
  ```

  ```
  [coverage:run]
  branch = True
  ```

* Improve coverage output adding source key under `[coverage:run]` [commit](https://github.com/kinderp/python-package-tutorial/commit/f491e21a7d504bd75a4f03fe38418c1bd9dc0786)
  
  ```
  add a source key with a value of imppkg
  This  is a handy way to stop specifying
  imppkg  to  the --cov option for pytest
  each time, and ensures that anyone runn
  ing tests with coverage will see the sa
  me output.
  ```
  
  ```
  [coverage:run]
  source = imppkg
  ```
* Avoid to type `--cov` every time and add that to `addopts` key under `[tool:pytest]` [commit[(https://github.com/kinderp/python-package-tutorial/commit/c8ac84a9e5a8a7f76f4e6a4423a90004ac911abe)
  
  ```
  You can also avoid specifying --cov
  altogether by adding an addopts key
  to the [tool:pytest] section with a
  value of --cov . You  can  override
  this  at  the command line later as
  desired using the corresponding:
  --no-cov option.
  ```
  
  ```
  [tool:pytest]
  testpaths = test
  addopts = --cov
  ```
* Show missing tests in coverage [commit](https://github.com/kinderp/python-package-tutorial/commit/efcc7b089ebe0d6189b0ae0f5309b555589ae20d)
  
  ```
  Coverage.py can keep track of  exactly  which  lines and branches
  aren’t covered by tests, which is a big help as  you try to write
  tests  that increase the coverage of your code. You can turn this
  on by  adding a new section to setup.cfg called [coverage:report]
  with a new key called show_missing set to a value of True.   This
  will produce  one  new Missing column in the coverage output. The
  Missing column lists the following: Lines or ranges of lines that
  aren’t covered.  As an example,  9 means line 9 is uncovered, and
  10-12 means lines 10, 11, and 12 are uncovered.  Logic  flow from
  one line to another that represents a branch that isn’t  covered.
  As an example, 1319 means the execution path that starts at line
  13 that would next execute line 19 is uncovered

  test/test_translations.py .                                [100%]

  ----------- coverage: platform linux, python 3.9.0-final-0 -----------
  Name                                                                    Stmts   Miss Branch BrPart  Cover   Missing
  -------------------------------------------------------------------------------------------------------------------
  .venv/lib/python3.9/site-packages/imppkg/__init__.py                        0      0      0      0   100%
  .venv/lib/python3.9/site-packages/imppkg/hello.py                           4      1      0      0    75%   8
  .venv/lib/python3.9/site-packages/imppkg/say.py                            18     12      4      1    32%   9-20, 24
  .venv/lib/python3.9/site-packages/imppkg/test_exclude_me_from_dist.py       0      0      0      0   100%
  -------------------------------------------------------------------------------------------------------------------
  TOTAL                                                                      22     13      4      1    38%
  ```

* Simplify coverage report output [commit](https://github.com/kinderp/python-package-tutorial/commit/01887929375aef769fc14ea6877a4bd702c0a22d)
  
  ```
  In your project, the .venv directory of your
  installed  package is  roughly equivalent to
  the  src/imppkg/  directory of the package’s
  source code.  Tell Coverage.py  this  is the
  case  with a new section in setup.cfg called
  [coverage:paths] .  Add a source key to this
  section, with  a  list  value  of equivalent
  file paths. Coverage.py  will  use the first
  entry to replace  any  subsequent entries in
  the output

  test/test_translations.py .           [100%]

  ----------- coverage: platform linux, python 3.9.0-final-0 -----------
  Name                                      Stmts   Miss Branch BrPart  Cover   Missing
  -------------------------------------------------------------------------------------
  src/imppkg/__init__.py                        0      0      0      0   100%
  src/imppkg/hello.py                           4      1      0      0    75%   8
  src/imppkg/say.py                            18     12      4      1    32%   9-20, 24
  src/imppkg/test_exclude_me_from_dist.py       0      0      0      0   100%
  -------------------------------------------------------------------------------------
  TOTAL                                        22     13      4      1    38%
  ```

  ```
  [coverage:paths]
  source =
     src/imppkg/
    .venv/*/python3.9/site-packages/imppkg/
  ```
  
* Skip covered files [commit](https://github.com/kinderp/python-package-tutorial/commit/980b6318ad3e308e7ec73cb35b53b9da9bb8666f)

  ```
  As your project grows and you spend more time testing
  it might become harder to pick  out uncovered modules
  from the coverage report. If you’re reaching 100% cov
  erage for several files, it can  be helpful to ignore
  them in the report output. You can add a skip_covered
  key with avalue of True to the [coverage:report] sect
  ion  to filter those out. Files that are filtered out
  are only removed from the list their coverage's still
  considered in the total coverage calculation for your
  code

  test/test_translations.py .                    [100%]

  ----------- coverage: platform linux, python 3.9.0-final-0 -----------
  Name                  Stmts   Miss Branch BrPart  Cover   Missing
  -----------------------------------------------------------------
  src/imppkg/hello.py       4      1      0      0    75%   8
  src/imppkg/say.py        18     12      4      1    32%   9-20, 24
  -----------------------------------------------------------------
  TOTAL                    22     13      4      1    38%
  ```

## Multiple test envs with tox

* Add tox settings in `setup.cfg` [commit](https://github.com/kinderp/python-package-tutorial/commit/81e55e44453e0544e2984cdfbb2eac27a9000f44) and then run `tox`
  
  ```
  [tox:tox]
  isolated_build = True
  ```
* Set envs under test and then run `tox` again

  ```
  The envlist key in the tox configuration defines which environments
  tox should create and execute by default when running the tox comma
  nd. The environments in the envlist can also be run individually as
  desired by using the -e argument to  the tox command and specifying
  the environment name. To get started,  add  an  envlist  key to the
  tox:tox section in your setup.cfg file with a value of py39

  The next time you run tox, it will:
  1. Create an isolated build of your package
  2. Create a virtual environment with a copy of Python 3.9
  3. Install your package in the virtual environment
  ```
  
  ```
  [tox:tox]
  isolated_build = True
  envlist = py39
  ```

* Configure tox test environment with `posargs`

  ```
  So far you’ve configured tox in the [tox:tox] section to indicate how to build your package
  and which environments to create. To configure the test environments themselves,  add a new
  [testenv] section. This section is used by  default for any configured test environment. In
  this section, you tell tox what commands  to run using the commands key. This key accepts a
  list of commands to run, with some special syntax available to pass arguments to the comman
  ds within each command you can use the {posargs} placeholder, which will pass any arguments
  to specify to the tox command along to the test environment commands. As an example, if you
  specify python -c 'print("{posargs}")' as a command, running tox hello world will execute

  python -c 'print("hello world")' in the environment.

  You can also pass options to a test command by separating them from the tox command and any
  of its options with a -- . As an example, if you specify python as a command, running tox --
  -V will execute python -V in the environment

  After you add the pytest command to the commands list, run tox again. You’ll see that, after the
  steps you saw previously, tox tries to execute pytest and fails as shown in the following output

  WARNING: test command found but not installed in testenv
    cmd: /home/antonio/dev/python-package-tutorial/.venv/bin/pytest
    env: /home/antonio/dev/python-package-tutorial/.tox/py39
  Maybe you forgot to specify a dependency? See also the allowlist_externals envconfig setting.

  Even though you installed pytest into the virtual environment for your project earlier, recall
  that tox creates and uses an isolated virtual environment for each test environment.This means
  that tox won’t use the copy of pytest that you’ve been running. You haven’t told tox to install
  pytest in those environments, so it can’t find a copy there either.
  ```
  
  ```
  [testenv]
  commands =
    pytest {posargs}
  ```
