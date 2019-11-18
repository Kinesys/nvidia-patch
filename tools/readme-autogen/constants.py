from enum import IntEnum, Enum
import os.path

class OSKind(Enum):
    Linux = 'linux'
    Windows = 'win'

    def __str__(self):
        return self.name

class Product(IntEnum):
    GeForce = 10
    Quadro = 20

    def __str__(self):
        return self.name

class WinSeries(IntEnum):
    win10 = 10
    win7 = 20
    ws2012 = 30
    ws2016 = 40

    def __str__(self):
        return self.name

BASE_PATH = os.path.dirname(os.path.abspath(__file__))
TEMPLATE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             "templates")
DATAFILE_PATH = os.path.join(BASE_PATH,
                             "..", "..", "drivers.json")
LINUX_README_PATH = os.path.join(BASE_PATH,
                                 "..", "..", "README.md")
WINDOWS_README_PATH = os.path.join(BASE_PATH,
                                 "..", "..", "win", "README.md")

ENCODING='utf-8'

DRIVER_URL_TEMPLATE = {
    (OSKind.Linux, None, None, None):                                       "https://international.download.nvidia.com/XFree86/Linux-x86_64/$version/NVIDIA-Linux-x86_64-$version.run",
    (OSKind.Windows, Product.GeForce, WinSeries.win10, ''):                 "https://international.download.nvidia.com/Windows/$version/$version-desktop-win10-64bit-international-whql.exe",
    (OSKind.Windows, Product.GeForce, WinSeries.win10, 'Studio Driver'):    "https://international.download.nvidia.com/Windows/$version/$version-desktop-win10-64bit-international-nsd-whql.exe",
    (OSKind.Windows, Product.Quadro, WinSeries.win10, ''):                  "https://international.download.nvidia.com/Windows/Quadro_Certified/$version/$version-quadro-desktop-notebook-win10-64bit-international-whql.exe",
    (OSKind.Windows, Product.GeForce, WinSeries.win7, ''):                  "https://international.download.nvidia.com/Windows/$version/$version-desktop-win8-win7-64bit-international-whql.exe",
    (OSKind.Windows, Product.Quadro, WinSeries.win7, ''):                   "https://international.download.nvidia.com/Windows/Quadro_Certified/$version/$version-quadro-desktop-notebook-win8-win7-64bit-international-whql.exe",
    (OSKind.Windows, Product.Quadro, WinSeries.ws2012, ''):                 "https://international.download.nvidia.com/Windows/Quadro_Certified/$version/$version-quadro-winserv2008r2-2012-2012r2-64bit-international-whql.exe",
    (OSKind.Windows, Product.Quadro, WinSeries.ws2016, ''):                 "https://international.download.nvidia.com/Windows/Quadro_Certified/$version/$version-quadro-winserv-2016-2019-64bit-international-whql.exe",
}

DRIVER_DIR_PREFIX = {
    (Product.GeForce, ''): '',
    (Product.GeForce, 'Studio Driver'): 'nsd_',
    (Product.Quadro, ''): 'quadro_',
}

REPO_BASE = "https://raw.githubusercontent.com/keylase/nvidia-patch/master"
