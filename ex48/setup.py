try:
    from setuptools import setup
    except ImportError:
        from disutils.core import setup
    
config = {
    'description': 'ex48',
    'author': 'ghaash',
    'url': 'URL to get it at.',
    'download_url': 'Where to download it.',
    'author_email': 'My email.',
    'version': '0.1',
    'install_requires': ['nose'],
    'packages': ['ex48'],
    'scripts': [],
    'name': 'projectname'
}

setup(**config)