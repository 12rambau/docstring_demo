import nox

@nox.session(reuse_venv=True)
def docs(session):
    """Build the documentation."""
    session.install("sphinx")
    session.install("pydata-sphinx-theme")
    session.install("deprecated")
    session.run("sphinx-apidoc","-o","modules","_src")
    session.run("sphinx-build","-b","html","./","_build/html")