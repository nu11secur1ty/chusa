#!/usr/bin/env python

"""
Copyright (c) 2024-2025 chusa developers (https://www.nu11secur1ty.com)
See the file 'LICENSE' for copying permission
"""

import glob
import os
import re
import shutil
import subprocess
import time
import zipfile

from lib.core.common import dataToStdout
from lib.core.common import extractRegexResult
from lib.core.common import getLatestRevision
from lib.core.common import getSafeExString
from lib.core.common import openFile
from lib.core.common import pollProcess
from lib.core.common import readInput
from lib.core.convert import getText
from lib.core.data import conf
from lib.core.data import logger
from lib.core.data import paths
from lib.core.revision import getRevisionNumber
from lib.core.settings import GIT_REPOSITORY
from lib.core.settings import IS_WIN
from lib.core.settings import VERSION
from lib.core.settings import TYPE
from lib.core.settings import ZIPBALL_PAGE
from thirdparty.six.moves import urllib as _urllib

# =============================================================================
# UPDATE FUNCTIONALITY
# =============================================================================

def update():
    """
    Update chusa to the latest version from the repository
    Supports pip, git, and zipball update methods
    """
    if not conf.updateAll:
        return

    success = False

    # =========================================================================
    # PIP UPDATE METHOD
    # =========================================================================
    if TYPE == "pip":
        infoMsg = "updating chusa to the latest stable version from the "
        infoMsg += "PyPI repository"
        logger.info(infoMsg)

        debugMsg = "chusa will try to update itself using 'pip' command"
        logger.debug(debugMsg)

        dataToStdout("\r[%s] [INFO] update in progress" % time.strftime("%X"))

        output = ""
        try:
            process = subprocess.Popen("pip install -U chusa", shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=paths.SQLMAP_ROOT_PATH)
            pollProcess(process, True)
            output, _ = process.communicate()
            success = not process.returncode
        except Exception as ex:
            success = False
            output = getSafeExString(ex)
        finally:
            output = getText(output)

        if success:
            logger.info("%s the latest revision '%s'" % ("already at" if "already up-to-date" in output else "updated to", extractRegexResult(r"\binstalled chusa-(?P<result>\d+\.\d+\.\d+)", output) or extractRegexResult(r"\((?P<result>\d+\.\d+\.\d+)\)", output)))
        else:
            logger.error("update could not be completed ('%s')" % re.sub(r"[^a-z0-9:/\\]+", " ", output).strip())

    # =========================================================================
    # GIT REPOSITORY UPDATE METHOD
    # =========================================================================
    elif not os.path.exists(os.path.join(paths.SQLMAP_ROOT_PATH, ".git")):
        warnMsg = "not a git repository. It is recommended to clone the 'nu11secur1ty/chusa' repository "
        warnMsg += "from GitHub (e.g. 'git clone --depth 1 %s chusa')" % GIT_REPOSITORY
        logger.warning(warnMsg)

        if VERSION == getLatestRevision():
            logger.info("already at the latest revision '%s'" % (getRevisionNumber() or VERSION))
            return

        message = "do you want to try to fetch the latest 'zipball' from repository and extract it (experimental) ? [y/N]"
        if readInput(message, default='N', boolean=True):
            directory = os.path.abspath(paths.SQLMAP_ROOT_PATH)

            # Verify write permissions
            try:
                # Try both possible main file names
                main_file = "chusa.py" if os.path.exists(os.path.join(directory, "chusa.py")) else "sqlmap.py"
                open(os.path.join(directory, main_file), "w+b")
            except Exception as ex:
                errMsg = "unable to update content of directory '%s' ('%s')" % (directory, getSafeExString(ex))
                logger.error(errMsg)
            else:
                # Backup file attributes
                main_file = "chusa.py" if os.path.exists(os.path.join(directory, "chusa.py")) else "sqlmap.py"
                attrs = os.stat(os.path.join(directory, main_file)).st_mode
                
                # Clear directory contents (preserve .git if exists)
                for wildcard in ('*', ".*"):
                    for filepath in glob.glob(os.path.join(directory, wildcard)):
                        try:
                            # Skip .git directory to preserve repository
                            if os.path.basename(filepath) == '.git':
                                continue
                            if os.path.isdir(filepath):
                                shutil.rmtree(filepath)
                            else:
                                os.remove(filepath)
                        except Exception:
                            pass  # Ignore cleanup errors

                # Verify directory is ready for update
                remaining_files = [f for f in glob.glob(os.path.join(directory, '*')) if os.path.basename(f) != '.git']
                if remaining_files:
                    errMsg = "unable to clear the content of directory '%s'" % directory
                    logger.error(errMsg)
                else:
                    try:
                        # Download and extract latest zipball from nu11secur1ty/chusa
                        logger.info("downloading latest version from %s" % ZIPBALL_PAGE)
                        archive = _urllib.request.urlretrieve(ZIPBALL_PAGE)[0]

                        with zipfile.ZipFile(archive) as zip_file:
                            # Get the root directory name in the zip
                            root_dir = None
                            for name in zip_file.namelist():
                                if '/' in name and not name.startswith('.'):
                                    root_dir = name.split('/')[0]
                                    break
                            
                            # Extract all files, adjusting paths
                            for info in zip_file.infolist():
                                if root_dir and info.filename.startswith(root_dir + '/'):
                                    # Remove the root directory from the path
                                    info.filename = info.filename[len(root_dir) + 1:]
                                
                                if info.filename and not info.filename.startswith('.'):
                                    try:
                                        zip_file.extract(info, directory)
                                    except Exception as e:
                                        logger.warning("could not extract %s: %s" % (info.filename, getSafeExString(e)))

                        # Verify update success by checking settings file
                        filepath = os.path.join(paths.SQLMAP_ROOT_PATH, "lib", "core", "settings.py")
                        if os.path.isfile(filepath):
                            with openFile(filepath, "r") as f:
                                content = f.read()
                                version_match = re.search(r"(?m)^VERSION\s*=\s*['\"]([^'\"]+)", content)
                                if version_match:
                                    version = version_match.group(1)
                                    logger.info("updated to the latest version '%s#dev'" % version)
                                    success = True
                                else:
                                    logger.error("could not determine version from settings file")
                        else:
                            logger.error("settings file not found after update")
                            
                    except Exception as ex:
                        logger.error("update could not be completed ('%s')" % getSafeExString(ex))
                    else:
                        if not success:
                            logger.error("update could not be completed")
                        else:
                            # Restore file attributes
                            try:
                                main_file = "chusa.py" if os.path.exists(os.path.join(directory, "chusa.py")) else "sqlmap.py"
                                os.chmod(os.path.join(directory, main_file), attrs)
                            except OSError:
                                logger.warning("could not set the file attributes of main file")

    # =========================================================================
    # GIT COMMAND UPDATE METHOD
    # =========================================================================
    else:
        infoMsg = "updating chusa to the latest development revision from the "
        infoMsg += "GitHub repository"
        logger.info(infoMsg)

        debugMsg = "chusa will try to update itself using 'git' command"
        logger.debug(debugMsg)

        dataToStdout("\r[%s] [INFO] update in progress" % time.strftime("%X"))

        output = ""
        try:
            # Reset any local changes and pull latest updates from nu11secur1ty/chusa
            process = subprocess.Popen("git checkout . && git pull %s HEAD" % GIT_REPOSITORY, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, cwd=paths.SQLMAP_ROOT_PATH)
            pollProcess(process, True)
            output, _ = process.communicate()
            success = not process.returncode
        except Exception as ex:
            success = False
            output = getSafeExString(ex)
        finally:
            output = getText(output)

        if success:
            logger.info("%s the latest revision '%s'" % ("already at" if "Already" in output else "updated to", getRevisionNumber()))
        else:
            if "Not a git repository" in output:
                errMsg = "not a valid git repository. Please checkout the 'nu11secur1ty/chusa' repository "
                errMsg += "from GitHub (e.g. 'git clone --depth 1 %s chusa')" % GIT_REPOSITORY
                logger.error(errMsg)
            else:
                logger.error("update could not be completed ('%s')" % re.sub(r"\W+", " ", output).strip())

    # =========================================================================
    # FALLBACK UPDATE RECOMMENDATIONS
    # =========================================================================
    if not success:
        if IS_WIN:
            infoMsg = "for Windows platform it's recommended "
            infoMsg += "to use a GitHub for Windows client for updating "
            infoMsg += "purposes (https://desktop.github.com/) or just "
            infoMsg += "download the latest snapshot from "
            infoMsg += "https://github.com/nu11secur1ty/chusa/downloads"
        else:
            infoMsg = "for Linux platform it's recommended "
            infoMsg += "to install a standard 'git' package (e.g.: 'apt install git')"

        logger.info(infoMsg)
