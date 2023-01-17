# Getting Started on the Rubin Science Platform

_[Greg Madejski](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@Madejski)
 and [Phil Marshall](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@drphilmarshall)_

First, a preamble:  The instructions below are for setting up the Rubin account, and connecting to the Rubin Data Facility at NCSA, 
used for the Rubin Stack Club members.  This is 
distinct from the Rubin Data Facility used for the work of Data Preview 0 (DP0) delegates 
(using the Rubin DC2 dataset), which is at the Interim Data Facility (IDF).  The 
instructions for connecting to the Rubin Science Platform as a DP0 delegate, go to 
https://dp0-1.lsst.io/dp0-delegate-resources/index.html .  We note that it is possible to 
access the DC2 data from the Jupyter notebook instance running at NCSA, but this requires one additional step (see below).  

The goal of the Stak Club (which predates the DP0) has been to develop tutorial notebooks on remote JupyterLab instances, 
to short-circuit the DM stack installation process and get used to working in the notebook aspect of the Rubin Science Platform (RSP). 

## Accessing the Rubin Science Platform
The notes here provide an introduction to the system, including how to gain access and then how to use JupyterLab once you are in. 
You will also need to get an NCSA account and connect through the NCSA VPN.

#### Getting a Rubin Science Platform Account
To join the Stack Club and request one of these accounts, please fill out the [Stack Club Membership Application Form](https://forms.gle/rehWtaoHgiBx6VfZ6). You'll need to agree to abide by the [Rules](../Rules.md), provide your full name (first and last), and your email address. 
If your application is successful, you'll get an email with instructions on how to set up your RSP account. 

#### Accessing the LSP via its VPN
At present, unless you are on an approved network, you must use the [NCSA virtual private network (VPN)](https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service).
The recommended method is to use Cisco's AnyConnect with DUO two-factor authentication (verified on Mac and Linux). Detailed instructions are available on the [NCSA VPN site](https://wiki.ncsa.illinois.edu/display/cybersec/Virtual+Private+Network+%28VPN%29+Service#VirtualPrivateNetwork(VPN)Service-UsingtheCiscoAnyConnectVPNClient(Required)).

> You can get AnyConnect by pointing your browser at https://sslvpn.ncsa.illinois.edu/ and selecting the `ncsa-vpn-default` option (this will only work if you have a java-compatible browser, like firefox esr version<=52). If you already have the AnyConnect client installed, open it up and enter `sslvpn.ncsa.illinois.edu/` in its connection window.  (**NB:** Make sure to use the `ncsa-vpn-default` group; this may not be the default group selected)

> You will need to setup two-factor authentication with DUO. To setup DUO, follow the instructions here https://duo.security.ncsa.illinois.edu/portal. DUO can be configured for smartphone or table access (currently dumb phones are not supported). When AnyConnect asks for your "second password", it wants the 6-digit number in your Duo app. (This may need refreshing, each one can only be used once.)  (**NB:** Use "NCSA as the identity provider", not your institution).  


#### Starting the Rubin Science Platform JupyterLab Notebook Aspect
Once the VPN connection is established, you should be able to navigate to the the JupyterLab instance at **https://lsst-lsp-stable.ncsa.illinois.edu**. Select the `Release` and `medium` options on the Spawner Options landing page, and then hit the "Spawn" button. You'll (eventually) end up on the JupyterLab launcher, where you can use the file manager in the left hand side bar to open your Jupyter notebooks, or start terminal or notebook editor tabs from the buttons provided.  You should see the pre-installed `notebook-demo`  notebooks in the file manager, for example.

> It might take a long time to start the JupyterLab instance (a few minutes or so).  We recommend using the most recent major release (e.g. v18.0.0) so that our [semi-continuous integration script](../CIT.md) is able to run your notebook, and using "medium" size (to support image processing tasks).

> At the end of your JupyterLab session, please make sure you save all and log out (from the launcher menu), to free up the cluster for others.

## Accessing the DC2 data set using the Jupyter notebook instance running at NCSA 
For Stack Club members using the DC2 data sets at the NCSA, there is an additional step they must do to authorize their account to access the DC2 data. The step is explained in the file /repo/README.md in the NSCA RSP (you can see this README.md in your linux terminal by typing ```cat /repo/README.md``` ).  Specifically, the user must create a small file named ```~/.pgpass``` .  That file must contain one line: 

```
lsst-pg-prod1.ncsa.illinois.edu:5432:lsstdb1:myusername:mysecretpasswd
```
where the ```myusername``` is your NCSA username, and ```mysecretpassword``` is your NCSA password.  

It is important to note that the location of the data repository accessible from IDF (``` s3://butler-us-central1-dp01 ```) is not the same as that accessible from NCSA (``` /repo/dc2 ```).  Your notebook needs to account for this.  

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
Broadly useful, small datasets are available in `/project/shared/data`  - this directory is world readable, but is only writeable by members of the `lsst-users` group (i.e., Rubin Project members). The stack club has its own read/writeable directory under `/project/stack-club` - feel free to contribute public data there. You can also use your personal `/project/<username>` folder for datasets that you want to share, but may not be as generally applicable. As a rule, Stack Club notebooks should use data in `/project/shared/data` or `/project/stack-club`. If you add a shared dataset, please document it in the `README` of the associated directory.

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
