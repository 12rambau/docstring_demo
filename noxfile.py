@nox.session(reuse_venv=True)
def docs(session):
    """Build the documentation."""
    session.install("sphinx")
    session.run("sphinx-apidoc","-o","modules","_src")
    session.run("sphinx-build","-b","html","./","build/html")