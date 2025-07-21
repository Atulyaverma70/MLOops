 ## data versioning
 * what
    * Data versioning is the process of saving, tracking, and managing multiple versions of a dataset over time. It lets you know what changed, when it changed, and who changed it—just like version control for code.
* why
    * Reproducibility
        * Helps you reproduce past results by using the exact version of data used during experiments or training.
    * Debugging
        * When model results suddenly change, data versioning helps you compare old and new datasets to find out why.
    * Collaboration
        * Multiple team members can work on datasets without overwriting each other’s changes.
    * Auditing & Compliance
        * You can track and show how data has changed over time—critical in finance, healthcare, etc.
    * Experiment Tracking
        * Useful in machine learning to link models with the exact version of data they were trained on.

* why?
    * We can use tools like DVC (Data Version Control) to manage data versions. For example, I can add a dataset with dvc add, which generates a .dvc file, then track it with Git. This way, the dataset version is tied to my code commit. If the dataset changes, DVC helps me compare versions, revert, or share it across teams via remote storage like S3 or Google Drive.
