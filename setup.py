from setuptools import setup, find_packages

setup(
    name='pym',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'colorama',
        'setuptools'
    ],
    entry_points={
        'console_scripts': [
            'pym=pym.__main__:main',
        ],
    },
    description='Template engine that renders Python code into tags.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    author='David León',
    author_email='davidalfonsoleoncarmona@gmail.com',
    python_requires='>=3.10',
    package_data={
        'pym.core': [
            'config/config.json',
        ],
    },
)