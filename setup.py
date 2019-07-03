from setuptools import setup
from codecs import open
from os import path

here = path.abspath(path.dirname(__file__))

# Get the long description from the README file
with open(path.join(here, 'sanic_swagger_ui/README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='sanic-swagger-ui',
    version='0.0.1',
    description='Swagger UI blueprint for Sanic',
    long_description=long_description,
    zip_safe=False,

    url='https://github.com/swingingsimian/sanic-swagger-ui',

    author='Nathan Johnson',
    author_email='sveint@gmail.com',
    license='MIT',

    classifiers=[
        'Development Status :: 4 - Beta',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7',
    ],

    keywords='sanic swagger',
    packages=['sanic_swagger_ui'],
    install_requires=['sanic',
                      'jinja2'],
    package_data={
        'sanic_swagger_ui': [
            'LICENSE',
            'README.md',
            'templates/*.html',
            'dist/VERSION',
            'dist/LICENSE',
            'dist/README.md',
            'dist/*.html',
            'dist/*.js',
            'dist/*.css',
            'dist/*.png'
        ],
    }
)
