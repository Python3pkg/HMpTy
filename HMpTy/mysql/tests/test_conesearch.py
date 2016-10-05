import os
import nose
import shutil
import yaml
from HMpTy.utKit import utKit

from fundamentals import tools

su = tools(
    arguments={"settingsFile": None},
    docString=__doc__,
    logLevel="DEBUG",
    options_first=False,
    projectName="HMpTy",
    tunnel=False
)
arguments, settings, log, dbConn = su.setup()

# # load settings
# stream = file(
#     "/Users/Dave/.config/HMpTy/HMpTy.yaml", 'r')
# settings = yaml.load(stream)
# stream.close()

# SETUP AND TEARDOWN FIXTURE FUNCTIONS FOR THE ENTIRE MODULE
moduleDirectory = os.path.dirname(__file__)
utKit = utKit(moduleDirectory)
log, dbConn, pathToInputDir, pathToOutputDir = utKit.setupModule()
utKit.tearDownModule()

# load settings
stream = file(
    pathToInputDir + "/example_settings.yaml", 'r')
settings = yaml.load(stream)
stream.close()

import shutil
try:
    shutil.rmtree(pathToOutputDir)
except:
    pass

# Recursively create missing directories
if not os.path.exists(pathToOutputDir):
    os.makedirs(pathToOutputDir)

# xt-setup-unit-testing-files-and-folders


class test_conesearch():

    def test_conesearch_function(self):

        from HMpTy.mysql import conesearch
        this = conesearch(
            log=log,
            dbConn=dbConn,
            ra="23:25:53.56",
            dec="+26:54:23.9",
            radiusArcsec=100,
            settings=settings
        )
        this.get()

    def test_conesearch_function2(self):

        from HMpTy.mysql import conesearch
        this = conesearch(
            log=log,
            dbConn=dbConn,
            ra=351.47321,
            dec=26.90664,
            radiusArcsec=100,
            settings=settings
        )
        this.get()

    def test_conesearch_function_exception(self):

        from HMpTy.mysql import conesearch
        try:
            this = conesearch(
                log=log,
                settings=settings,
                fakeKey="break the code"
            )
            this.get()
            assert False
        except Exception, e:
            assert True
            print str(e)

        # x-print-testpage-for-pessto-marshall-web-object

    # x-class-to-test-named-worker-function
