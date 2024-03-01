# section-metadata-wg-onto

This repository is meant to organize the work of the [NFDI Section (Meta)Data](https://www.nfdi.de/section-metadata/) Working Group Ontology harmonization and Mapping.

## Important Links
* Working Group Charter [published version (Zenodo)](https://zenodo.org/doi/10.5281/zenodo.6726518) & [editor version (GDoc)](https://docs.google.com/document/d/1GUh7K0Sy8tyrKZ4-BEizb-9Qa0tt3uzE)
* Mailing list [Sign-up link](https://lists.nfdi.de/postorius/lists/section-metadata-wg-onto.lists.nfdi.de/)
  * If you are affiliated with a NFDI consortium and want to be part of the WG, you need to sign up to this mailing list 
  as it is our official communication channel.
* [our RocketChat channel](https://all-chat.nfdi.de/channel/section-metadata-wg-onto) in the NFDI general workspace
  * Only for quick chats, use the mailing list for sharing important information to reach all WG members.
  * The use of RocektChat in NFDI might be abandoned due to licensing issues in the future.
* We have bi-monthly meetings according to these schedules:
  * [section-metadata-onto_every_2nd_wednesday_call_series.ics](section-metadata-onto_every_2nd_wednesday_call_series.ics)
  * [section-metadata-onto_every_4th_tuesday_call_series.ics](section-metadata-onto_every_4th_tuesday_call_series.ics)

## Repository Structure

* [mapping](mapping) - is the workspace for charter epic #7 
  * contains a [README.md](mapping%2FREADME.md) to document the completed work
* [TLO_Infos](TLO_Infos) - is the workspace for charter epic #3
  * TODO: add README for this epic and possibly rename the folder to something more suitable
* TODO: add folders and README for the other epics
* [Meetings](Meetings) - contains the notes of our meetings in Markdown format

## Philip's Workflow Proposal
There are three kinds of issues:
* [epic issues](https://github.com/StroemPhi/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+label%3A%22charter+epic%22)
  * taken from our charter and labeled with "charter epic"
  * comment section should ony be used for "meta" discussions about this epic (e.g. requirements)
  * actual specific aspects associated with an epic should be discussed in "epic subtaks issues"
* [epic subtask issues](https://github.com/StroemPhi/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+sort%3Areactions-%2B1-desc+-label%3A%22charter+epic%22+-label%3A%22organizational%22+)
  * must be opened via respective issue template
    * each epic has a subtask issue template
      * mapping recommendation epic has more > a test > might be overkill or good for this special case
      * **TODO: MLO and TLO evaluation epics still need to get an issue template and be adjusted to the rest** 
  * each WG memeber can open a new discussion / propose a new subtask using such an issue
  * https://github.com/StroemPhi/section-metadata-wg-onto/issues/12 explains how such issues can be prioritized to 
    be discussed in upcomming calls
  * discussions around such an issue should be documented within its discussion thread
* [organizational issues](https://github.com/StroemPhi/section-metadata-wg-onto/issues?q=is%3Aissue+is%3Aopen+label%3Aorganizational)
  * for organizational "meta" discussions around how to structure our work that has nothing to do with 
    any of our epics
  * should always be tagged with the "organizational" label
  * TODO: think about making an issue template for this

READMEs:
I had the idea that each epic gets a working folder to store whatever needs to be stored in there and then there 
should be a README which contains the documentation (agreements) regarding this epic. This way we#d have an easy to 
read/grasp repo, the READMEs could serve as living drafts for official recommendation/charter publications from the 
WG, they are used to link to the open and closed issues around the epics in a way that allows a more fine-grained 
structuring that only with labels.
