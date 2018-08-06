# Semi-continuous Integration and Testing

_Phil Marshall, August 5, 2018_

To help prevent our notebooks going stale, we run our notebooks automatically very few hours using the LSST DESC's [`beavis-ci`]() script. These notes explain how this was set up. 

## Installing `beavis-ci`
Following the instructions on the [`beavis-ci` repo](https://github.com/LSSTDESC/beavis-ci), we downloaded the `beavis-ci` script into the `notebooks` folder.
```
cd notebooks
curl -o beavis-ci.sh https://raw.githubusercontent.com/LSSTDESC/beavis-ci/master/beavis-ci.sh
chmod a+x beavis-ci.sh
```

## Testing `beavis-ci`
`beavis-ci` takes a repo name as its argument. It also needs a GitHub username and associated API token, in order to push the deployed notebooks to the "rendered" orphan (history-less) branch. These are most conveniently exported as environment variables. We also need to specify the kernel
to run the notebooks with: "lsst" gets us the most recent release, as required.
```
./beavis-ci.sh LSSTScienceCollaborations/StackClub -u $GITHUB_USERNAME -k $GITHUB_API_KEY --kernel lsst
```

## Running `beavis-ci`
Continuous integration systems check for new commits or pushes; `beavis-ci` is not that clever. To achieve semi-continuous integration, we just run the `beavis-ci` script from a cron job. Here's what that job looks like:
```
crontab -l

45  11  *  *  * ( cd ~/notebooks && ./beavis-ci.sh  -u drphilmarshall -k <GITHUB_API_TOKEN> --kernel lsst )
```
Note that the GitHub arguments are passed in explicitly, in case cron does not set up your environment variables. 

> Notes:
>
> It is a semi-abuse to run jobs that will make the LSP pod look busy, since the goal is to cull idle processes so that we use resources more efficiently. However, until notebook CIT is implemented properly, `beavis-ci` is the best we can do.
>
> Anything entered in the crontab will disappear every time the image is rebuilt. Only information in the user space will survive from one image to the next. This means that `beavis-ci` needs to be run from a regular NCSA account, not a JupyterLab terminal.
 