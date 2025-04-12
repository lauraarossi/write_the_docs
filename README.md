# write_the_docs

Python documentation tool.

Given project details (name, author, version, release), a surce path and entry 
file irp erfors the following:
- Generates API style html Sphinx documentation.
- Runs black formatter.
- Runs flake8 checks.
- Generates html flowchart of the entry file.
- Writes lof to txt and html

Main tool usage:
write_the_docs [OPTIONS] SOURCE_CODE_PATH ENTRY_FILE PROJECT_NAME VERSION AUTHOR RELEASE

Initial version developed April 2025.

Laura Rossi laura.a.rossi.r@gmail.com
