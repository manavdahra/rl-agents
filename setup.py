from setuptools import setup, find_packages

setup(
    name='rl-agents',
    version='1.0.0',
    description='A collection of Reinforcement Learning agents. Forked form',
    url='https://github.com/manavdahra/rl-agents',
    author='Manav Dahra',
    author_email='manav.dahra@gmail.com',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Researchers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.5',
    ],

    keywords='reinforcement learning agents',
    packages=find_packages(exclude=['docs', 'scripts', 'tests*']),
    install_requires=[
        'gymnasium', 
        'gymnasium[other]',
        'numpy', 
        'pandas', 
        'numba', 
        'pygame', 
        'matplotlib', 
        'seaborn', 
        'six', 
        'docopt',
        'torch>=1.2.0', 
        'tensorboard',
        'tensorboardX', 
        'scipy',
        'highway_env@git+https://github.com/manavdahra/highway-env',
    ],
    tests_require=['pytest'],
    extras_require={
        'dev': ['scipy'],
    },
    entry_points={
        'console_scripts': [],
    },
)

