from setuptools import setup, find_packages

setup(
    name='simple_package',  # The name of your package
    version='0.1',
    packages=find_packages(),  # Automatically include all packages
    include_package_data=True,
    install_requires=[],  # Any external dependencies (add if required)
    author='Your Name',
    author_email='yourname@example.com',
    description='A simple utility package for Django projects',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/simple_package',  # Your GitHub URL
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3 :: Only',
    ],
)
