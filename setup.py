from setuptools import setup, find_packages

setup(
    name                = 'url_request_scheduler',
    version             = '0.3',
    description         = 'scheduler for url request',
    author              = 'beomwoo.moon',
    author_email        = 'doorbw@outlook.com',
    url                 = 'https://github.com/doorBW/url_request_scheduler',
    download_url        = 'https://github.com/doorBW/url_request_scheduler/archive/master.zip',
    install_requires    =  ['schedule','requests'],
    packages            = find_packages(exclude = []),
    keywords            = ['url_request_scheduler','url request scheduler','url scheduler','scheduler','url request'],
    python_requires     = '>=3',
    package_data        = {},
    zip_safe            = False,
    classifiers         = [
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
    ],
)