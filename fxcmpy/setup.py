from setuptools import setup

def readme():
    try:
        with open('README.md', 'r') as f:
            return f.read()
    except:
        return ''


setup(
    name = 'fxcmpy',
    packages = ['fxcmpy'], # this must be the same as the name above
    version = '1.1.36',
    description = 'A Python Wrapper Class for the RESTful API as provided by FXCM Forex Capital Markets Ltd.',
    long_description = readme(),
    author = 'FXCM API',
    author_email = 'api@fxcm.com',
    license='BSD',
    url = 'https://github.com/fxcm/RestAPI/tree/master/fxcmpy', 
    download_url = 'https://github.com/fxcm/RestAPI/tree/master/fxcmpy', 
    keywords = 'FXCM API Python Wrapper Finance Algo Trading',
    install_requires=['pandas', 'socketIO_client', 'configparser', 'requests[socks]'], 
    python_requires='>=3.4',
    include_package_data = True,
    package_data={
        '': ['*.txt']
    },
    classifiers = ['Programming Language :: Python :: 3.4',
                   'Programming Language :: Python :: 3.5',
                   'Programming Language :: Python :: 3.6'],

)
