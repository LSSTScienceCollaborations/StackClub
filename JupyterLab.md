# Getting Started on the LSST Science Platform

_Greg Madejski and [Phil Marshall](https://github.com/LSSTScienceCollaborations/DMStackClub/issues/new?body=@drphilmarshall)_

We are developing tutorial notebooks on remote JupyterLab instances, to short-circuit the DM stack installation process and get used to working in the 
notebook aspect of the LSST science platform. In these notes we provide:
* Notes on how to get set up on the LSST Science Platform (LSP) JupyterLab Notebook Aspect at NCSA
* Help with getting set up to the DM Stack Club tutorial notebooks

> NB. In Phase 0, we made use of the [jupyterlabdemo.lsst.codes](https://jupyterlabdemo.lsst.codes/user/madejski/lab?redirects=1)
instance, set up by the DM team in the Google cloud. For Phase 1, we will be using the LSP JupyterLab instance at the LSST Data Facility, NCSA.

**The go-to resource is the [LSST Science Platform (LSP) Notebook Aspect Documentation](https://nb.lsst.io/v/DM-14406/index.html)** - below we give a very brief summary, and some DM Stack Club-specific tips.

## Accessing the LSST Science Platform
The [LSP docs](https://nb.lsst.io/v/DM-14406/index.html) provides an introduction to the NCSA system, including how to gain access and then how to use JupyterLab once you are in. 
Getting in to NCSA takes involves getting an NCSA account, and then figuring out VPN access.

### Getting an NCSA Account
Contact Phil (DM @drphilmarshall on LSSTC Slack) or Simon (@ksk) to get an NCSA Stack Club account. You'll need to provide your full name (first and last) and your email address. You'll (eventually) get an email invitation to [create an account at NCSA](https://identity.ncsa.illinois.edu/) (including choosing a username of 8 characters or fewer).

### Accessing NCSA via its VPN
As explained on the [PDAC wiki](https://confluence.lsstcorp.org/display/DM/PDAC+networking+and+user+accounts+for+developers), the only way to get onto the LSST science platform at NCSA is via its virtual private network (VPN). The easiest way is by using Cisco's AnyConnect, which if you don't have you can get by pointing your browser at **https://vpn.ncsa.illinois.edu/** and selecting the `ncsa-vpn-default` option. If you already have the AnyConnect client installed, open it up and enter `vpn.ncsa.illinois.edu` in its connection window. 

### Starting up the LSST Science Platform JupyterLab Notebook Aspect 
Once the VPN connection is established, you should be able to navigate to the the JupyterLab instance at **https://lsst-lspdev.ncsa.illinois.edu/nb**. Select `Release 15.0` and `medium` on the Spawner Options landing page, and then hit the "Spawn" button. You'll (eventually) end up on the JupyterLab launcher, where you can use the file manager in the left hand side bar to open your Jupyter notebooks, or start terminal or notebook editor tabs from the buttons provided.  You should see the pre-installed `notebook-demo`  notebooks in the file manager, for example.


## Contributing to the DM Stack Club Repo
From the Launcher, start a terminal, `cd` to the `notebooks` folder and `git clone` the `DMStackClub` repo, using https access:
```
git clone https://github.com/LSSTScienceCollaborations/DMStackClub.git
```

### Workflow
The Stack Club workflow is to edit the club notebooks (or start new ones) in a suitable development branch, push it to the base repo, and submit a pull request (to enable club code review). Club members have Write access and so can do this; everyone else can push to their fork of the DMStackClub repo, and submit a PR from there. To exercise this workflow, try modifying  [`Hello_World.ipynb`](https://github.com/LSSTScienceCollaborations/DMStackClub/blob/master/notebooks/Hello_World.ipynb), pushing your commit(s) and submitting a PR. 





