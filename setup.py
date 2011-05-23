from distutils.core import setup

setup(
    name = 'django-queryset-decorator',
    packages = ['queryset_decorator'],
    version='0.0.2',
    description='Experimental .decorate(fn) method for Django QuerySets, for '
                'clever lazily evaluated optimisations.',
    long_description=open('README.txt').read(),
    author='Diederik van der Boor',
    author_email='vdboor@edoburu.nl',
    url='https://github.com/vdboor/django-queryset-decorator',
    license='BSD',
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
