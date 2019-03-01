import setuptools

setuptools.setup(
    name="pb_bss",

    author="Lukas Drude",
    author_email="mail@lukas-drude.de",

    description="EM algorithms for integrated spatial and spectral models.",
    long_description=open('README.md', encoding='utf-8').read(),

    packages=setuptools.find_packages(),

    install_requires=[
        'numpy',
        'dataclasses',
        'matplotlib',
        'scikit-learn',
        'cached_property',
    ],

    classifiers=[
        'Programming Language :: Python :: 3.6',
    ]
)
