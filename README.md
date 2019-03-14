# pick1

It's pick1pack1, but this time there's a Spring Boot application instead of wordpress. The database will remain some SQL variant, but its design will need to be redone from the ground up. 

## State of the Project:

The idea is a repo that includes devops features driven by a system-agnostic virtual machine configured by code that is stored in the repo. Python scripts are available to allow anyone with the repo to build their own website, as the repo will not contain fetched resources such as images. The database will eventually be managed by these scripts, but may be built by hand first. Honestly not too sure how to go with the database on this one. In-memory for the portable version with a separate thread for the live site could be in the cards. 

It makes sense to kick things off with generating starter projects for the various components, at the very least to work on mapping out the project's directory structure.

### Starters:
- [x] Spring
- [x] Python
- [x] Devops
- [ ] Database