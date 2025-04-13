# write_the_docs

Python documentation tool.

Given project details (name, author, version, release), a surce path and entry 
file irp erfors the following:
- Generates API style html Sphinx documentation.
- Runs black formatter.
- Runs flake8 checks.
- Generates html flowchart of the entry file.
- Runs all unit tests and generates html report of results.
- Runs coverage analysis on unit tests and generates html report of results.
- Saves logs of process to html.

Main tool CLI usage:
write_the_docs [OPTIONS] SOURCE_CODE_PATH ENTRY_FILE PROJECT_NAME VERSION AUTHOR RELEASE

Python usage (full run):

from write_the_docs import run_all
run_all(
    <source path>,
    <entry file>,
    <project name>,
    <project version>,
    <project author(s)>,
    <project release>,
)

Alternatively, individual components (Sphinx, Flake8, Black, Flwochart, Tests)
can be run by instantiating the appropriate class and calling the run() method,
e.g.:

from write_the_docs import run_all, Sphinx
from write_the_docs.Utilities import configure_logging, logs_to_html

log_dir = <raw logs path>
configure_logging(log_dir)
Sphinx(
    <source path>,
    <entry file>,
    <project name>,
    <project version>,
    <project author(s)>,
    <project release>,
    <output path>,
).run()
logs_to_html(log_dir, <html logs path>)


Initial version developed April 2025.

Laura Rossi laura.a.rossi.r@gmail.com
