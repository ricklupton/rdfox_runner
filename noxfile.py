"""
Configure environments to test rdfox runner across multiple RDFox versions.
"""

import nox


RDFOX_VERSIONS = ["5.6", "6.2", "6.3.1"]

RDFOX_VERSIONS_IDS = [f"rdfox{version.replace('.', '')}" for version in RDFOX_VERSIONS]


@nox.session
@nox.parametrize("rdfox", RDFOX_VERSIONS, ids=RDFOX_VERSIONS_IDS)
def tests(session, rdfox):
    session.install("pytest~=5.2")
    session.install(f"rdfox=={rdfox}")
    session.install("-e", ".")
    session.run("pytest", "tests", "--log-level=DEBUG", *session.posargs)
