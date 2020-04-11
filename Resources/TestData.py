import os, sys, inspect
class TestData():
    # fetch path to the directory in which current file is, from root directory or C:\ (or whatever driver number it is)
    currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
    # extract the path to parent directory
    parentdir = os.path.dirname(currentdir)
    ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
    CHROME_EXECUTABLE_PATH = "C:/D/PyWorkspace/amazon/drivers/chromedriver.exe"
    FIREFOX_EXECUTABLE_PATH = parentdir+"\Drivers\geckodriver.exe"   #"D:/PycharmProjects/PythonUnitTest_POM_Project/Drivers/geckodriver.exe"
    BASE_URL = "https://www.amazon.in"
    SEARCH_TERM = "WD My Passport 4TB"
    HOME_PAGE_TITLE = "Amazon.in"
    NO_RESULTS_TEXT = "No results found."
    SIGN_IN_PAGE_TITLE = "Amazon Sign In"