from setuptools import find_packages, setup
from statshog import __version__

setup(
    name='statshog',
    version=__version__,
    description='A simple statsd client.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='Karl-Aksel Puulmann',
    author_email='karl@technicalwealth.ee',
    url='https://github.com/macobo/statshog',
    license='MIT',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    package_data={'': ['README.md']},
    test_suite='nose.collector',
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
