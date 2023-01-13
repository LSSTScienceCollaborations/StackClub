# Stack Club

The science community Stack Club is an LSSTC-supported project, to form a small community committed to learning how to use, and explain, the [Rubin Observatory LSST Science Pipelines](https://pipelines.lsst.io/) (colloquially called "the Stack"). The idea is that _the best way to learn something is to try and teach it:_ if you can write a useful tutorial on some aspect of the DM Stack, and especially its science pipelines, then you have to understand that part first. 

We develop tutorial notebooks on the Rubin Science Platform (RSP) at NCSA, which provides a standard computing environment, including the most recent version of the Stack and a number of useful precursor datasets. We meet up for biweekly video hack sessions, at which we also review each other's notebooks, and all of our tutorials are available in this repo. New members with zero experience are very welcome: we aim to produce tutorials for beginners as well as more advanced Stack users, and the organizers are happy to spend time walking new members through the available resources, and explaining how to get started. 

We also offer short, self-contained courses on using the Stack. Material from first course from Spring 2020 can be found [here](https://github.com/LSSTScienceCollaborations/StackClubCourse).

See below for how to get involved: we hope you find our notebooks useful!

## Community Tutorials

Our goal is to build on the existing demo notebooks and html tutorial pages to create a set of _community-generated, community-oriented_ notebooks that reflect the science interests and expected analyses of the Rubin Observatory/LSST Science Collaborations. The notebooks in the repo were developed on the Rubin Science Platform (RSP) at NCSA, and use the standard datasets provided there.

| Topic   | Description  |
|---|---|
| [GettingStarted](GettingStarted)   | How to use JupyterLab, and contribute to the Stack Club repo.  |
| [Basics](Basics)                   | Guided tours of various key Stack classes and functions, data structures, etc. |
| [Visualization](Visualization)     | Displaying images and catalogs. |
| [ImageProcessing](ImageProcessing) | From raw images to calibrated exposures and coadded images.  |
| [SourceDetection](SourceDetection) | Detection of sources in images - including low surface brightness galaxies.  |
| [Deblending](Deblending)           | Deblending astronomical sources |
| [Measurement](Measurement)         | Measuring object properties |
| [Validation](Validation)           | Tools for validating Stack outputs, example validation analyses |

* [Stack Club projects](https://github.com/LSSTScienceCollaborations/StackClub/labels/project), as defined by Stack Club members - follow [this link](https://github.com/LSSTScienceCollaborations/StackClub/labels/project) to see what people are working on. [Unassigned projects](https://github.com/LSSTScienceCollaborations/StackClub/issues?utf8=%E2%9C%93&q=is%3Aopen+label%3Aproject+no%3Aassignee) are available for new members to take on!

* [Working list of target topics, with links to tutorial seeds](https://docs.google.com/document/d/1PSA1uWwTfs9CweatpxF8CEPGBYRY5ZaXB39JzXYE7_U/edit#), for help in defining a new Stack Club project. This list is a fairly comprehensive collection of existing project and community tutorial web pages and demo notebooks, from which seeds can be drawn.

## Joining the Stack Club
Active participation in the Stack Club requires Rubin Observatory data rights as described in [ls.st/rdo-013](https://ls.st/rdo-013). We welcome new members with any level of experience. We have found that some familiarity with Python is helpful, and that experience with Jupyter notebooks and git/GitHub can help you get started faster. No experience with the Stack is required.

If you would like to join the Stack Club, please fill out this short **[application form](https://forms.gle/rehWtaoHgiBx6VfZ6)**. 
You'll be asked to agree to abide by the [Stack Club Rules](Rules.md) and provide enough contact information to request an account on the Rubin Science Platform.
You'll receive an email when your account is created; at that point, you can start [contributing](#contributing).

If you are not ready to commit time to working on a Stack Club project, you can still follow along by [watching](https://github.com/LSSTScienceCollaborations/StackClub/subscription) this repo, joining the [#stack-club](https://lsstc.slack.com/messages/C9YRAS4HM/) on the LSSTC Slack workspace, or viewing material from the [Stack Club Course](https://github.com/LSSTScienceCollaborations/StackClubCourse).  

## Contributing
**New members: [START HERE!](GettingStarted/GettingStarted.md)** These notes will walk you through getting access to the Rubin Science Platform and show you how to work on tutorial notebooks.

**Everyone else:** we welcome pull requests! Feel free to fork this repo and send us a pull request. If you are interested in joining the Stack Club, please drop us a line in [#stack-club](https://lsstc.slack.com/messages/C9YRAS4HM). When preparing a pull request, please note the Stack Club [standards](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/GettingStarted/GettingStarted.md#standards).

## Contact
We welcome your input! Please post questions and suggestions in the
[issues](https://github.com/LSSTScienceCollaborations/StackClub/issues) of this repository. 
You can also contact the organizers directly via the links below:

* Greg Madejski (SLAC, [@Madejski](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@Madejski))
* Alex Drlica-Wagner (Fermilab, [@kadrlica](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@kadrlica))
* Melissa Graham (UW, [@MelissaGraham](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@MelissaGraham))

The Stack Club meets fortnightly via Zoom, and you can find us on LSSTC Slack at [#stack-club](https://lsstc.slack.com/messages/C9YRAS4HM).

## License
The text in this repository is Copyright The Authors, and licensed under Creative Commons [CC-BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/), which means
you can copy and redistribute the material in any medium or format
for any purpose, as long as you give appropriate credit, provide a link to the license, and indicate if changes were made.
If you remix, transform, or build upon the material, you may not distribute the modified material - this is to prevent incorrect
information about the Stack getting out there, or at least, take responsibility ourselves if it does.
All the code in this repository is available for re-use under the [MIT License](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/LICENSE), which means you can do anything you like with it
but you can't blame us if it doesn't do what you want.

## More About This Project
The Stack Club has been supported by awards from the LSSTC Enabling Science program. You can read about our original 3-phase plan [here](https://docs.google.com/document/d/103kzjOklSUWo5MJP9B-EsnAdO7V6bstTC_mzBvd0NIk/edit#). Phase 0 involved collecting existing tutorials and identifying potential club members from around the LSST Science Collaborations. Then, in Phase 1 (late May 2018 to mid August 2018) we worked together in a small group to turn a subset of those existing "seed" tutorials into community-maintained Jupyter notebooks, for display at the August LSST 2018 Project and Community Workshop (PCW) in Tucson. At that meeting, we opened up to a larger group of LSST science collaboration members, extending and spinning off the initial set of notebooks. We met once a week through Fall 2018, defining about 20 projects, and producing 11 tutorial notebooks for community use. In fall 2018 the Stack Club had about 20 active participants.
