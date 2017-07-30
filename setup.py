from setuptools import setup, find_packages

setup(name="prewikka-apps-twitter",
      version="4.0.0",
      author="Prelude Team",
      author_email="support.prelude@c-s.fr",
      url="https://www.prelude-siem.org",
      packages=find_packages(),
      install_requires=["prewikka >= 4.0.0"],
      entry_points={
          "prewikka.plugins": [
              "Twitter = twitter:Twitter",
          ],
      },
      package_data={
          "twitter": ["htdocs/css/*.css",
                      "htdocs/js/*.js",
                      "templates/*.mak"],
      },
)
