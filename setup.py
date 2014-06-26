from setuptools import setup, find_packages
from setuptools.command.install import install as InstallCommand

# class InstallWithDefaultConfig(InstallCommand):
#     description = 'Installs the module with a specified YAML config file.'
#     user_options = [
#         ('config=', None, 'The YAML config file to include with the installation')
#     ] + InstallCommand.user_options

#     def initialize_optione(self):
#         InstallCommand.initialize_options(self)
#         self.config_file = None

#     def run(self):
#         print "testtestsetstste"
#         install.run(self)

setup(
    name='NbUrnClient',
    version='0.8.0',
    author='Rune Lain Knudsen',
    author_email='rune.knudsen@uib.no',
    packages=find_packages(),
    url='https://github.com/runelk/NB_URN_Client_Python',
    license='LICENSE.txt',
    description='Python Client for the URN PID service at the National Library of Norway',
    long_description=open('README.md').read(),
    install_requires=[
        'PyYAML',
        'suds==0.4'
    ]
)
