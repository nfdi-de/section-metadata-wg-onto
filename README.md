# section-metadata-wg-onto

This repository is meant to organize the work of the [NFDI Section (Meta)Data](https://www.nfdi.de/section-metadata/) Working Group Ontology harmonization 
and Mapping.

This repository is two things. First, it is the cloud storage space where we upload and share files with our WG
members and the rest of the world in a version controlled manner. Second, it is the space in which we can discuss 
asynchronously and transparently the tasks we need to accomplish via GitHub Issues and Pull Requests.

## Deliverables
* Working Group Charter [published version (Zenodo)](https://zenodo.org/doi/10.5281/zenodo.6726518) & [editor version (GDoc)](https://docs.google.com/document/d/1GUh7K0Sy8tyrKZ4-BEizb-9Qa0tt3uzE)
* Mapping Recommendations on creation, tools, validating an publishing.
  *Work in progress in directory [mapping-recommendations](mapping-recommendations)*

## Contributing
The main channel of communication of the working group is the mailing list, for which you can sign up [here](https://lists.nfdi.de/postorius/lists/section-metadata-wg-onto.lists.nfdi.de/), 
if you are affiliated with an NFDI consortium.

We have bi-monthly meetings according to these schedules:
* [section-metadata-onto_every_2nd_wednesday_call_series.ics](section-metadata-onto_every_2nd_wednesday_call_series.ics)
* [section-metadata-onto_every_4th_tuesday_call_series.ics](section-metadata-onto_every_4th_tuesday_call_series.ics)

To contribute via this repository, members of the working group need to have a GitHub account and some basic knowledge 
about how to work with Git and GitHub to be able to participate. You need to know what an issue, pull request and a branch is.
To open or comment on issues, a browser suffices as the main interface to interact with this repository. 
To upload new or edited existing files and to create branches and pull request, we recommend using the 
[GitHub Desktop](https://desktop.github.com/) app, if you are not familiar with Git already. 
Please consult the web for one of the many tutorials on how to use Git, GitHub, GitHub Desktop, like the official 
GitHub documentation on [Issues](https://docs.github.com/en/issues/tracking-your-work-with-issues), [Pull Request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request) and [Branches](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches). 

We expect the WG members to follow the activity of this repository by starring or watching it. Members who want to
contribute directly must either be made part of the repository team (contact [@StroemPhi](https://github.com/StroemPhi)),
or fork the repository.

A prototypical interaction of a WG member with this repository would entail:
* checking [here](https://github.com/nfdi-de/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+-label%3A%22charter+epic%22+-label%3A%22organizational%22+) regularly, to see if any new open epic subtask issues have been created to be voted on,
* creating epic subtask issues,
* commenting on issues (participate in discussions),
* creating an issue branch when working on a specific subtask that requires the creation or editing of files,
* submitting changes made on an issue branch via a pull request.

### Issues in this Repository
The [issues of this repository](https://github.com/nfdi-de/section-metadata-wg-onto/issues/) represent tasks.
We use them to discuss, coordinate and work on the tasks of our working group. 
An issue is open as long as it needs to be worked on or discussed and is being closed when the task it represents is completed.
An issue can be tagged with labels and assigned to one or more WG members, which allows them to be categorized, 
filtered and sorted. Each issue should always have a concise and self-explanatory title and description. Each issue 
is open to be commented on or referenced by any GitHub user, which allows us to work in an open source fashion also 
with people outside our working group. 

There are three kinds of issues: 

#### [Epic Issues](https://github.com/nfdi-de/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+label%3A%22charter+epic%22)
Epic issues represent the main tasks we have identified in our WG charter. Hence, we will only create new epics, 
once we have agreed to amend our WG charter accordingly. These issues are called epics because they need 
to be broken down into smaller and more concrete subtasks to be completed, and thus will probably remain open 
throughout the existence of our working group. They are currently not assigned to any particular WG member, 
as all WG members are expected to contribute to an epic in some form via the associated subtasks.
All epics are tagged with the label "charter epic" and a label that represents the topic they address, e.g. "mapping 
development". The topic label of an epic comes from a controlled list and is being used to tag its subtasks. 
Each epic issue has a description (taken from our charter) that should explain sufficiently the topic it addresses and 
contain a link to an issue template with which new associated subtasks can be created.
The comment section of an epic issue should **only** be used for discussions about the required outcomes of an epic.

Additionally, each epic should have a folder in this repository to store any files associated with it, 
e.g. [mapping](mapping) is the workspace for epic #7 and [TLO_Infos](TLO_Infos) for epic #3.

#### [Epic Subtask Issues](https://github.com/nfdi-de/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+-label%3A%22charter+epic%22+-label%3A%22organizational%22+)
As the name implies, an epic subtask issue represents a subtask associated with an epic. A subtask could either be a 
concrete action item assigned to one or more WG members (e.g. writing a recommendation), or, it could represent a 
discussion about a certain aspect of an expected epic outcome that the WG needs to find an agreement on before being 
able to formulate concrete action items. For example, we might want to first discuss in one epic subtask issue 
which types of terminologies qualify for evaluation by our WG, before we create an epic subtask issue that is about 
the evaluation of a specific terminology. The comment section of an epic subtask issue should **only** be used to 
discuss the particular epic subtask. Creating epic subtasks in such a granular way allows us to focus on specific
aspects separately. By linking related epic subtask issues to each other, we should thus get a better overview of what
needs to be done and what needs to be discussed.

Each epic subtask issue is based on a template through which it gets automatically associated to its respective epic 
via hyperlink and topic label. For now, most epics have only one associate epic subtask issue template. 

To file an epic subtask issue you need to:
* either click on the link provided in the description of an epic, or select the appropriate template when clicking
  the "new issue" button,
* change the default title to a meaningful and concise one,
* provide the details required by the respective template.

#### [Organizational Issues](https://github.com/nfdi-de/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+label%3Aorganizational)
Organizational issues are those that are concerned **only** with "meta" discussions about how to structure our work.
Hence, they should not be associated with any epic or epic subtask issue. 
For example, when you have questions around or problems with the use of this repository, you should be filing an 
organizational issue. 
To file a new organizational issue, please use [this template](https://github.com/nfdi-de/section-metadata-wg-onto/issues/new?assignees=&labels=organizational&projects=&template=organizational-issue.md&title=organizational%3A+%5BADD+YOUR+CONCISE+ISSUE+TITLE+HERE%5D), change its default title and add a meaningful 
description about what needs to be discussed.

There exists one permanently open, organizational issue that is pinned to the top of the issue list. [This issue](https://github.com/nfdi-de/section-metadata-wg-onto/issues/12)
explains how all open epic subtask issues can be prioritized by up-voting. This is intended to to be discussed in 
upcoming calls.

### Using GitHub Project to manage issues
TODO: explain how to interact with our [project](https://github.com/orgs/nfdi-de/projects/1).


