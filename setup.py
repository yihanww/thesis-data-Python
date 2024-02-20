import setuptools

setuptools.setup(
    name="data_pipeline",
    version="0.0.1",
    author="Yihan Wang", 
    author_email="yihanwang@uchicago.edu",
    description="data pipeline test",
    packages=setuptools.find_packages(),
    install_requires=[
        'pandas',
        'scipy',
    ],
)
