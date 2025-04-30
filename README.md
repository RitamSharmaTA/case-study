# Emerging Business Opportunities

# Background
Our client (Manufacturer A) is a leading Food & Beverage manufacturer. Client wants to understand the growth patterns of consumer preferences (themes) and evaluate positioning of their brand across different themes. Client also wants to know the sales drivers of their products.

# Data
Client will provide the following data for the project:

● Sales Data – At UPC level for both Client and Competitors

● Social Media Data – Mentions of theme across all Social media Platforms

● Google Search Data – Search volume of the Theme

● Theme_Product_List – Product to theme Mapping

● Product_Manufacturer_List – Product to Manufacturer Mapping

● Theme List – Theme Names 

# Pre-requisites

* Ensure [invoke](http://www.pyinvoke.org/index.html) tool and pyyaml are installed in your `base` `conda` environment. If not, run

```
(base):~$ pip install invoke
(base):~$ pip install pyyaml
```

# Getting started

* Switch to the root folder (i.e. folder containing this file)
* A collection of workflow automation tasks can be seen as follows
    **NOTE**

     * Please make sure there are no spaces in the folder path. Environment setup fails if spaces are present.

```
(base):~/<proj-folder>$ inv -l
```

* To verify pre-requisites, run

```
(base)~/<proj-folder>$ inv debug.check-reqs
```

and check no error messages (`Error: ...`) are printed.


## Environment setup:

### Introduction

* Tip: Default name of the env is `ta-lib-dev`. You can change it for your project.
    * For example: to make it as `env-myproject-prod`.
    * Open `tasks.py`
    * Set `ENV_PREFIX = 'env-customer-x'`

### Setup a development environment:

Run below to install core libraries
```
(base):~/<proj-folder>$ inv dev.setup-env 
```

The above command should create a conda python environment named `ta-lib-dev` and install the code in the current repository along with all required dependencies.

Activate the environment first to install other addons. Keep the environment active for all the remaining commands in the manual.
```
(base):~/<proj-folder>$ conda activate ta-lib-dev
```

Install `invoke` and `pyyaml` in this env to be able to install the addons in this environment.
```
(ta-lib-dev):~/<proj-folder>$ pip install invoke
```

Now run all following command to install all the addons. Feel free to customize addons as suggested in the introduction.

```
(ta-lib-dev):~/<proj-folder>$ inv dev.setup-addon --formatting --jupyter --documentation --testing --extras --ts
```

You now should have a standalone conda python environment and installed code in the current repository along with all required dependencies.

* Get the installation info by running
```
(ta-lib-dev):~/<proj-folder>$ inv dev.info
```

* Test your installation by running
```
(ta-lib-dev):~/<proj-folder>$ inv test.val-env --usecase=<specific usecase>
```

# Launching Jupyter Notebooks

- In order to launch a jupyter notebook locally in the web server, run

    ```
    (ta-lib-dev):~/<proj-folder>$ inv launch.jupyterlab
    ```
     After running the command, type [localhost:8080](localhost:8080) to see the launched JupyterLab.

- The `inv` command has a built-in help facility available for each of the invoke builtins. To use it, type `--help` followed by the command:
    ```
    (ta-lib-dev):~/<proj-folder>$ --help
    ```
- On running the ``help`` command, you get to see the different options supported by it.

    ```
    Usage: inv[oke] [--core-opts] launch.jupyterlab [--options] [other tasks here ...]

    Options:
    -a STRING, --password=STRING
    -e STRING, --env=STRING
    -i STRING, --ip=STRING
    -o INT, --port=INT
    -p STRING, --platform=STRING
    -t STRING, --token=STRING
    ```
# Frequently Asked Questions

The FAQ for code templates during setting up, testing, development and adoption phases are available
[here](https://tigeranalytics-code-templates.readthedocs-hosted.com/en/latest/faq.html)