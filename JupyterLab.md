# Getting Started with JupyterLab

_[Greg Madejski](https://github.com/LSSTScienceCollaborations/DMStackClub/issues/new?body=@Madejski) and Phil Marshall_

We are developing tutorial notebooks on remote JupyterLab instances, to short-circuit the DM stack installation process and get used to working in the 
notebook aspect of the LSST science platform. In these notes we provide:
* Notes on how to get set up on JupyterLab at NCSA
* Some tips for using JupyterLab effectively.

> NB. In Phase 0, we made use of the [jupyterlabdemo.lsst.codes](https://jupyterlabdemo.lsst.codes/user/madejski/lab?redirects=1)
instance, set up by the DM team in the Google cloud. For Phase 1, we will be using the LSST JupyterLab instance at the LSST Data Facility, NCSA.

## Setting up at NCSA
The LSST technote ["SQR-025: Welcome to the Notebook Aspect of the LSST Science Platform"](https://sqr-025.lsst.io/) provides an introduction to the NCSA system, including how to gain access and then how to use JupyterLab once you are in. 
Getting in to NCSA takes involves getting an NCSA account, and then figuring out VPN access.

### Getting an NCSA Account
Contact Phil (DM @drphilmarshall on LSSTC Slack) or Simon (@ksk) to get an NCSA Stack Club account. You'll need to provide your full name (first and last) and your email address. You'll (eventually) get an email invitation to [create an account at NCSA](https://identity.ncsa.illinois.edu/) (including choosing a username of 8 characters or fewer).

### Accessing NCSA via its VPN
As explained on the [PDAC wiki](https://confluence.lsstcorp.org/display/DM/PDAC+networking+and+user+accounts+for+developers), the only way to get onto the LSST science platform at NCSA is via its virtual private network (VPN). The easiest way is by using Cisco's AnyConnect, which if you don't have you can get by pointing your browser at **https://vpn.ncsa.illinois.edu/** and selecting the `ncsa-vpn-default` option. If you already have the AnyConnect client installed, open it up and enter `vpn.ncsa.illinois.edu` in its connection window. 

### Starting up JupyterLab 
Once the VPN connection is established, you should be able to navigate to the the JupyterLab instance at **https://lsst-lspdev.ncsa.illinois.edu/nb**. Select `Release 15.0` and `medium` on the Spawner Options landing page, and then hit the "Spawn" button. You'll (eventually) end up on the JupyterLab launcher, where you can start a terminal, `cd` to the `notebooks` folder and clone the `DMStackClub` repo, and also start playing with the project notebooks in `notebook-demo`.


## JupyterLab Tips


