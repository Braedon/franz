from setuptools import setup, find_packages

setup(
    name='franz',
    version='0.1.0.dev1',
    description='(Franz) Kafka CLI tool',
    url='https://github.com/Braedon/franz',
    author='Braedon Vickers',
    author_email='braedon.vickers@gmal.com',
    license='MIT',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Topic :: Utilities',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='kafka cli',
    packages=find_packages(),
    install_requires=[
        'click',
        'kafka-python>=1.3',
        'python-snappy',
    ],
    entry_points={
        'console_scripts': [
            'franz=franz:main',
        ],
    },
)
