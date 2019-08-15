# Semi-continuous Integration and Testing

_Phil Marshall, August 5, 2018_

To help prevent our notebooks going stale, we run all our notebooks ~~automatically every few hours~~ from time to time using the LSST DESC's [`beavis-ci`]() script. These notes explain how this works. 

## Installing `beavis-ci`
Following the instructions on the [`beavis-ci` repo](https://github.com/LSSTDESC/beavis-ci), we downloaded the `beavis-ci` script into the `notebooks` folder.
```
cd notebooks
curl -o beavis-ci.sh https://raw.githubusercontent.com/LSSTDESC/beavis-ci/master/beavis-ci.sh
chmod a+x beavis-ci.sh
```

## Testing and Running `beavis-ci`
`beavis-ci` takes a repo name as its argument. It clones from master using ssh (so you need to give GitHub an ssh key for the machine you are working on). It also needs a GitHub username and associated API token in order to push (with the `--push` option) the deployed notebooks to the "rendered" orphan (history-less) branch. This information is stored in the environment variables `GITHUB_USERNAME` and `GITHUB_API_KEY`. We also need to specify the kernel
to run the notebooks with: "lsst" gets us the most recent supported release, as required. The `--png` option makes PNG format badges for display in the README tables. 
```
./beavis-ci.sh LSSTScienceCollaborations/StackClub --kernel lsst --push --png
```

## Aspiration: semi-CIT with `beavis-ci`
Continuous integration systems check for new commits or pushes; `beavis-ci` is not that clever. To achieve semi-continuous integration, we have attempted to run the `beavis-ci` script from a cron job. Here's what that job looks like:
```
crontab -l

45  11  *  *  * ( cd ~/notebooks && ./beavis-ci.sh LSSTScienceCollaborations/StackClub --kernel lsst --push --png )
```
Note that cron will need to set up your environment variables for the push to work. Right now this system doesn't work: the cron jobs don't survive the exit from the container (understandably). We're working with DM to try and get this (or something like it) working, but we're not there yet.

> Notes:
>
> It is a semi-abuse to run jobs that will make the LSP pod look busy, since the goal is to cull idle processes so that we use resources more efficiently. However, until notebook CIT is implemented properly, `beavis-ci` is the best we can do.
>
> Anything entered in the crontab will disappear every time the image is rebuilt. Only information in the user space will survive from one image to the next. This means that `beavis-ci` needs to be run from a regular NCSA account, not a JupyterLab terminal.
 
