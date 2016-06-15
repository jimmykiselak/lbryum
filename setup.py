#!/usr/bin/env python2

# python setup.py sdist --format=zip,gztar

from setuptools import setup
import os
import sys
import platform
import imp
import argparse

version = imp.load_source('version', 'lib/version.py')

if sys.version_info[:3] < (2, 7, 0):
    sys.exit("Error: lbryum requires Python version >= 2.7.0...")

data_files = []

parser = argparse.ArgumentParser()
parser.add_argument("--root_path", default=None)
opts = parser.parse_args()


if False and platform.system() in ['Linux', 'FreeBSD', 'DragonFly']:
    usr_share = os.path.join(sys.prefix, "share")
    if not os.access(opts.root_path + usr_share, os.W_OK) and \
       not os.access(opts.root_path, os.W_OK):
        if 'XDG_DATA_HOME' in os.environ.keys():
            usr_share = os.environ['$XDG_DATA_HOME']
        else:
            usr_share = os.path.expanduser('~/.local/share')
    data_files += [
        (os.path.join(usr_share, 'applications/'), ['electrum.desktop']),
        (os.path.join(usr_share, 'pixmaps/'), ['icons/electrum.png'])
    ]

setup(
    name="lbryum",
    version=version.ELECTRUM_VERSION,
    install_requires=[
        'slowaes>=0.1a1',
        'ecdsa>=0.9',
        'pbkdf2',
        'requests',
        'qrcode',
        'protobuf<=3.0.0b2',
        'dnspython',
        'jsonrpclib',
    ],
    packages=[
        'lbryum',
        'lbryum_gui',
        'lbryum_gui.qt',
        'lbryum_plugins',
        'lbryum_plugins.audio_modem',
        'lbryum_plugins.cosigner_pool',
        'lbryum_plugins.email_requests',
        'lbryum_plugins.exchange_rate',
        'lbryum_plugins.greenaddress_instant',
        'lbryum_plugins.keepkey',
        'lbryum_plugins.labels',
        'lbryum_plugins.ledger',
        'lbryum_plugins.plot',
        'lbryum_plugins.trezor',
        'lbryum_plugins.trustedcoin',
        'lbryum_plugins.virtualkeyboard',
    ],
    package_dir={
        'lbryum': 'lib',
        'lbryum_gui': 'gui',
        'lbryum_plugins': 'plugins',
    },
    package_data={
        'lbryum': [
            'www/index.html',
            'wordlist/*.txt',
            'locale/*/LC_MESSAGES/electrum.mo',
        ]
    },
    #scripts=['electrum'],
    data_files=data_files,
    description="Lightweight LBRYcrd Wallet",
    author="LBRY",
    author_email="jimmy@lbry.io",
    license="GNU GPLv3",
    url="https://lbry.io",
    long_description="""Lightweight LBRYcrd Wallet"""
)
