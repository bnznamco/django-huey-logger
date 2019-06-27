from setuptools import setup, find_packages

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name='django-huey-logger',
    version='0.0.1',
    url='https://github.com/bnznamco/django-huey-logger',
    install_requires=[
        'django>=1.11.6',
    ],
    long_description=long_description,
    description="A simple Django app to let you know if huey cron are working without errors.",
    license="MIT",
    author="Gabriele Baldi",
    author_email="gabriele.baldi.01@gmail.com",
    packages=find_packages(),
    include_package_data=True,
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Framework :: Django :: 1.11',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)
