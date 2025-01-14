from setuptools import setup

setup(
    name="nxbt-naibaoofficial",
    version='1.1.0',
    description='nxbt marco enhanced by naibaooffical',
    include_package_data=True,
    long_description_content_type="text/markdown",
    install_requires=[
        "dbus-python==1.2.16",
        "Flask==1.1.2",
        "Flask-SocketIO==5.0.1",
        "eventlet==0.31.0",
        "blessed==1.17.10",
        "pynput==1.7.1",
        "psutil==5.6.6",
        "cryptography==3.3.2",
        "jinja2==3.0.3",
        "Werkzeug==2.0.2"
    ],
    extra_require={
        "dev": [
            "pytest"
        ]
    }
)
