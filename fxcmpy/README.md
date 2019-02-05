# Project description

## Introduction
FXCM provides a RESTful API to interact with its trading platform. Among others, it allows the retrieval of historical data as well as of streaming data. In addition, it allows to place different types of orders and to read out account information. The overall goal is to allow the implementation automated, algortithmic trading programs.

fxcmpy.py is a Python wrapper package for that API.

## Demo Account
To get started with the the API and the package, a demo account with FXCM is sufficient. You can open such an account under https://www.fxcm.com/uk/forex-trading-demo/.

## Package Installation
Installation happens via pip install on the command line.

		pip install fxcmpy

## API Token
To connect to the API, you need an API token that you can create or revoke from within your (demo) account in the Trading Station https://tradingstation.fxcm.com/.

In an interactive context, you can use e.g. a variable called TOKEN to reference your unique API token.

		TOKEN = YOUR_FXCM_API_TOKEN
Connecting to the server, then boils down to the following line of code.

		con = fxcmpy.fxcmpy(access_token=TOKEN, log_level='error', server='demo')
However, it is recommended to store the API token in a configuration file which allows for re-usability and hides the token on the GUI level. The file should contain the following lines.

		[FXCM]
		log_level = error
		log_file = PATH_TO_AND_NAME_OF_LOG_FILE
		access_token = YOUR_FXCM_API_TOKEN
It is assumed onwards that this file is in the current working directory and that its name is fxcm.cfg.

With such a configuration file in the current working directory, only the filename need to be passed as a parameter to connect to the API.

		con = fxcmpy.fxcmpy(config_file='fxcm.cfg', server='demo')
## Documentation
The detailed documentation of this wrapper is found under:

https://www.fxcm.com/fxcmpy/
The detailed documentation of the API is found under:

https://github.com/fxcm/RestAPI
