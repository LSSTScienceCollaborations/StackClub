# Getting Started on the Rubin Science Platform

_Greg Madejski and [Phil Marshall](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@drphilmarshall)_

We are developing tutorial notebooks on remote JupyterLab instances, to short-circuit the DM stack installation process and get used to working in the
notebook aspect of the Rubin Science Platform (RSP). In these notes we provide:
* [Notes on how to get set up on the Rubin Science Platform (RSP) JupyterLab Notebook Aspect at the LSST Data Facility at NCSA](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/GettingStarted/GettingStarted.md#accessing-the-lsst-science-platform)
* [Help with getting set up to run and edit the Stack Club tutorial notebooks](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/GettingStarted/GettingStarted.md#running-and-contributing-to-the-stack-club-notebooks)

## Accessing the Rubin Science Platform
The [Rubin Science Platform (RSP) Notebook Aspect Documentation](https://nb.lsst.io/) provides an introduction to the system, including how to gain access and then how to use JupyterLab once you are in. 
Accessing the RSP involves getting an NCSA account and figuring out VPN access.

#### Getting a Rubin Science Platform Account
To join the Stack Club and request one of these accounts, please fill out the [Stack Club Membership Application Form](https://forms.gle/rehWtaoHgiBx6VfZ6). You'll need to agree to abide by the [Rules](../Rules.md), provide your full name (first and last), and your email address. 
If your application is successful, you'll get an email with instructions on how to set up your RSP account. 

#### Accessing the LSP via its VPN
At present, unless you are on an approved network, you must use the [NCSA virtual private network (VPN)](https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service).
The recommended method is to use Cisco's AnyConnect with DUO two-factor authentication (verified on Mac and Linux). Detailed instructions are available on the [NCSA VPN site](https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service#VirtualPrivateNetwork(VPN)Service-UsingtheCiscoAnyConnectVPNClient(Required)).
The best documentation for getting setup with your account is on [nb.lsst.io](https://nb.lsst.io/index.html#getting-started).

1. [Install and configure the NCSA VPN](https://nb.lsst.io/getting-started/logging-in.html#vpn-setup)
2. [Log into the NCSA VPN](https://nb.lsst.io/getting-started/logging-in.html#vpn-login) (**NB:** Use the `ncsa-vpn-default` group; this may not be the default group selected)
3. [Log into the Notebook Aspect](https://nb.lsst.io/getting-started/logging-in.html#step-2-log-in) (**NB:** Use "NCSA as the identity provider", not your institution)

If you forget your password it can be reset following the instructions [here](https://developer.lsst.io/services/lsst-dev.html?highlight=reset#lsst-dev-password). If you have problems connecting to the NCSA services you can check their status and submit a help ticket [here](https://confluence.lsstcorp.org/display/DM/LSST+Service+Status+page).

For a Linux install, you may need to pre-install [`openconnect`](http://www.infradead.org/openconnect/) from your favorite package manager.

#### Starting the Rubin Science Platform JupyterLab Notebook Aspect
Once the VPN connection is established, you should be able to navigate to the the JupyterLab instance at **https://lsst-lsp-stable.ncsa.illinois.edu**. Select the `Release` and `medium` options on the Spawner Options landing page, and then hit the "Spawn" button. You'll (eventually) end up on the JupyterLab launcher, where you can use the file manager in the left hand side bar to open your Jupyter notebooks, or start terminal or notebook editor tabs from the buttons provided.  You should see the pre-installed `notebook-demo`  notebooks in the file manager, for example.

> It might take a long time to start the JupyterLab instance (a few minutes or so).  We recommend using the most recent major release (e.g. v18.0.0) so that our [semi-continuous integration script](../CIT.md) is able to run your notebook, and using "medium" size (to support image processing tasks).

> At the end of your JupyterLab session, please make sure you save all and log out (from the launcher menu), to free up the cluster for others.


## Running and Contributing to the Stack Club Notebooks
From the Launcher, start a terminal, `cd` to the `notebooks` folder and `git clone` the `StackClub` repo, using either HTTP or SSH access:
```
git clone https://github.com/LSSTScienceCollaborations/StackClub.git
```
(You'll need to [set up your SSH keys](https://github.com/drphilmarshall/GettingStarted/#contributing) to use the SSH option, but this will enable you to avoid typing your GitHub password a lot.)
You can then `git checkout` a development branch (so that you can keep your `master` branch clean and up to date with the latest updates from the Club), and execute and modify the club notebooks. You can open them from the file manager, and use the resulting notebook editor. 

> New to `git` and GitHub? Have a play in [this sandbox](https://github.com/drphilmarshall/GettingStarted) - from there you can watch Phil on YouTube doing a GitHub live demo, too.

#### Workflow
The Stack Club workflow is to edit the club notebooks (or start new ones) in a suitable development branch, push it to the base repo, and submit a pull request (to enable club code review). Club members have Write access and so can do this; everyone else can push to their fork of the StackClub repo, and submit a PR from there. To exercise this workflow, try modifying  [`Hello_World.ipynb`](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/notebooks/Hello_World.ipynb), pushing your commit(s) and submitting a PR. Don't forget to clear outputs and save before committing your changes!
 
#### Standards
We aspire to produce high-quality tutorials that can be followed by any member of the LSST Science Collaborations who wants to learn about the DM Stack, and in particular its science pipelines. 
* We [regularly test](../CIT.md) all the notebooks in the `master` branch of this repo using the most recent major release 
of the Stack, and flag those that do not run all the way through. The `master` branch should only contain working notebooks, so that (ideally) Stack Club notebooks only fail to run if the Stack changes.
* Maintenance of the Stack Club notebooks is the responsibility of the notebooks' "owner(s)", who are listed in the first cell of each notebook. This cell also lists the date and Stack release on which the notebook was last verified to run.
* The introduction cell of each notebook contains a list of "learning objectives", so that the user can judge whether or not this tutorial is right for them.
* We include markdown cells to explain each step in the tutorial, and provide links to the source code and reference documents as needed.

> A [template notebook](templates/template_Notebook.ipynb) that will help you maintain the above standards is available in the [templates folder](templates).

#### Available Datasets
Broadly useful, small datasets are available in `/project/shared/data`  - this director is world readable, but is only writeable by members of the `lsst-users` group (i.e., Rubin Project members). The stack club has its own read/writeable directory under `/project/stack-club` - feel free to contribute public data there. You can also use your personal `/project/<username>` folder for datasets that you want to share, but may not be as generally applicable. As a rule, Stack Club notebooks should use data in `/project/shared/data` or `/project/stack-club`. If you add a shared dataset, please document it in the `README` of the associated directory.

Larger datasets are available in `/datasets`. This is a read-only folder.

#### The Stack Club Library
The [`stackclub` folder in this repo](../stackclub) is a python package containing a number of utility functions and classes for use in tutorial notebooks. You can browse its documentation at https://stackclub.readthedocs.io/.  
If you are contributing notebooks, you may want or need to develop the  `stackclub` package as well 
(e.g., by adding modules to it), and so its best to setup the package installation to be local and editable. 
Start by opening a terminal in the RSP and sourcing the LSST setup:
```
source /opt/lsst/software/stack/loadLSST.bash
```
In the top level folder of your local clone of the StackClub repo, do:
```
python setup.py -q develop --user
```
This will put the repo's `stackclub` folder on your path. When developing the package, you may find it useful to add the following lines to your notebook:
```python
%load_ext autoreload
%autoreload 2
```
This enables you to repeatedly `import stackclub` as you update the library code. The above lines are in the [template notebook](templates/template_Notebook.ipynb), for your convenience.

If you are not developing this package, and you have permission to write to your base python site-packages, you can install it using pip, like this:
```
pip install git+git://github.com/LSSTScienceCollaborations/StackClub.git#egg=stackclub
```
