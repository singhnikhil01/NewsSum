import setuptools

with open("README.md", 'r', encoding='utf-8') as f:
    long_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summerization-"
AUTHOR_USER_NAME = "singhsansar"
SRC_REPO = "TextSummerizer"
AUTHOR_EMAIL = "aiengineer@nikhilsingh.com.np"  # Corrected email address

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small NLP project",
    long_description=long_description,  # Corrected 'Long_description' to 'long_description'
    long_description_content_type="text/markdown",  # Corrected 'Long_description_content' to 'long_description_content_type'
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",  # Corrected 'BUG Tracer' to 'Bug Tracker'
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
