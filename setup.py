from setuptools import setup

setup(# package information
      name="stackclub",
      version="0.1",
      author="Phil Marshall",
      author_email="dr.phil.marshall@gmail.com",
      description="Utilities for use in e.g the Stack Club LSST tutorial notebooks",
      long_description=open("README.md").read(),
      url="https://github.com/LSSTScienceCollaborations/StackClub",
      packages=['stackclub'],
      package_dir={'stackclub':'stackclub'},
      include_package_data=True,
      package_data={},
      classifiers=[
          "Development Status :: 4 - Beta",
          "License :: OSI Approved :: MIT License",
          "Intended Audience :: Developers",
          "Intended Audience :: Science/Research",
          "Operating System :: OS Independent",
          "Programming Language :: Python",
      ],
      install_requires=["numpy", "matplotlib"],
)