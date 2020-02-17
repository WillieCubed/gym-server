import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="gym-server",
    version="0.1.0",
    author="Willie Chalmers III",
    author_email="dev@williecubed.me",
    description="A remote gym training server for RL agents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/WillieCubed/gym-server",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'flask',
    ],
    python_requires='>=3.6',
)
