# Stack Club

The LSST science community Stack Club is an LSSTC-supported project, to form a small community committed to learning how to use, and explain, the LSST data management (DM) software Stack. The idea is that _the best way to learn something is to try and teach it:_ if you can write a useful tutorial on some aspect of the DM Stack, and especially its science pipelines, then you have to understand that part first.

See below for how to get involved: we hope you find our notebooks useful!

## Community Tutorials

Our goal is to build on the existing LSST DM Stack demo notebooks and html tutorial pages to create a set of
_community-generated, community-oriented_ notebooks that reflect the science interests and expected analyses of
the LSST Science Collaborations.

| Topic   | Description  | Notebook Location  |
|---|---|---|
| Basics           | Guided tours of various key Stack classes and functions, data structures, etc. | [StackClub/Basics](Basics)  |
| Getting Started  | How to use JupyterLab, and contribute to the Stack Club repo.  | [StackClub/GettingStarted](GettingStarted)  |
| Visualization    | Displaying images and catalogs. | [StackClub/Visualization](Visualization)  |
| Image Processing | From raw images to `calexp`s and `coadd`s.  | [StackClub/ImageProcessing](ImageProcessing) |
| SourceDetection  | Detection of sources in images - including low surface brightness galaxies.  | [StackClub/SourceDetection](SourceDetection)  |
| Deblending       | Deblending the objects | [StackClub/Deblending](Deblending) |
| Measurement      | Measuring the objects | [StackClub/Measurement](Measurement) |
| Validation       | Tools for validating Stack outputs, example validation analyses | [StackClub/Validation](Validation) |

* [Stack Club projects](https://github.com/LSSTScienceCollaborations/StackClub/labels/project), as defined by Stack Club members - follow [this link](https://github.com/LSSTScienceCollaborations/StackClub/labels/project) to see what people are working on. [Unassigned projects](https://github.com/LSSTScienceCollaborations/StackClub/issues?utf8=%E2%9C%93&q=is%3Aopen+label%3Aproject+no%3Aassignee) are available for new members to take on!

* [Working list of target topics, with links to tutorial seeds](https://docs.google.com/document/d/1PSA1uWwTfs9CweatpxF8CEPGBYRY5ZaXB39JzXYE7_U/edit#), for help in defining a new Stack Club project. This list is a fairly comprehensive collection of existing project and community tutorial web pages and demo notebooks, from which seeds can be drawn.

## Joining the Stack Club
If you would like to join the Stack Club, please fill out this short **[application form](https://goo.gl/forms/588KlPTFfkEEFFUu2)**. (Basically you'll be asked to agree to abide by the [Stack Club Rules](Rules.md), and then give enough contact information to request an account on the LSST Science Platform.) If you are not ready to commit time to working on a Stack Club project, you can still follow along by [watching](https://github.com/LSSTScienceCollaborations/StackClub/subscription) this repo and joining the [#stack-club LSSTC Slack channel](https://lsstc.slack.com/messages/C9YRAS4HM/).  

## Contributing
New Stack Club members: please see the [notes on getting started](GettingStarted/GettingStarted.md) - they'll walk you onto you new LSST Science Platform account, and then show you how to work on your tutorial notebooks.

Everyone else: we welcome pull requests! Feel free to fork this repo and send us a pull request. And if you are interested in joining the  Stack Club, please drop one of us a line, or come and find us in the [#stack-club](https://lsstc.slack.com/messages/C9YRAS4HM) LSSTC Slack channel.

> When preparing a pull request, please note the [standards](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/GettingStarted/GettingStarted.md#standards) that we are trying to uphold.

## Contact
We welcome your input! Please post questions and suggestions in the
[issues](https://github.com/LSSTScienceCollaborations/StackClub/issues) of this repository. You can also contact the following points of contact directly via the links below:

* Greg Madejski (SLAC, [Madejski](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@kMadejski))
* Alex Drlica-Wagner (Fermilab, [@kadrlica](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@kadrlica))
* Phil Marshall (SLAC, [@drphilmarshall](https://github.com/LSSTScienceCollaborations/StackClub/issues/new?body=@drphilmarshall))

The Club meets periodically via Zoom, but you can find us on LSSTC Slack at [#stack-club](https://lsstc.slack.com/messages/C9YRAS4HM). You can also watch the tutorial walkthroughs in the Club sessions in the videos linked from our [Meetings page](Meetings.md). If you are just looking for the application form, it's [here](https://goo.gl/forms/588KlPTFfkEEFFUu2).

## License

The text in this repository is Copyright The Authors, and licensed under Creative Commons [CC-BY-ND 4.0](https://creativecommons.org/licenses/by-nd/4.0/), which means
you can copy and redistribute the material in any medium or format
for any purpose, as long as you give appropriate credit, provide a link to the license, and indicate if changes were made.
If you remix, transform, or build upon the material, you may not distribute the modified material - this is to prevent incorrect
information about the Stack getting out there, or at least, take responsibility ourselves if it does.
All the code in this repository is available for re-use under the [MIT License](https://github.com/LSSTScienceCollaborations/StackClub/blob/master/LICENSE), which means you can do anything you like with it
but you can't blame us if it doesn't do what you want.

## More About This Project

Following a successful LSSTC "Enabling Science" proposal, we put together a 3-phase plan, which you can read about in more detail [here](https://docs.google.com/document/d/103kzjOklSUWo5MJP9B-EsnAdO7V6bstTC_mzBvd0NIk/edit#). Phase 0 involved collecting existing tutorials and identifying potential club members from around the LSST Science Collaborations. Then, in Phase 1 (late May 2018 to mid August 2018) we worked together in a small group to turn a subset of those existing "seed" tutorials into community-maintained Jupyter notebooks, for display at the August LSST 2018 Project and Community Workshop (PCW) in Tucson. At that meeting, we opened up to a larger group of LSST science collaboration members, extending and spinning off the initial set of notebooks.
