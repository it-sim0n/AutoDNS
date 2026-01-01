import tempfile

RESOLVERS = """\
8.8.8.8
8.8.4.4
1.1.1.1
1.0.0.1
9.9.9.9
149.112.112.112
208.67.222.222
208.67.220.220
94.140.14.14
94.140.15.15
64.6.64.6
64.6.65.6
84.200.69.80
84.200.70.40
8.26.56.26
8.20.247.20
"""

def create_resolvers_file():
    f = tempfile.NamedTemporaryFile(mode="w+", delete=False)
    f.write(RESOLVERS)
    f.close()
    return f.name

