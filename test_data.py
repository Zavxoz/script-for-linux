SUB_DF_OUTPUT = """
Filesystem     1K-blocks     Used Available Use% Mounted on
dev              3446604        0   3446604   0% /dev
run              3455152     1320   3453832   1% /run
/dev/sda4      194354092 41257996 143153764  23% /
tmpfs            3455152   199556   3255596   6% /dev/shm
tmpfs            3455152        0   3455152   0% /sys/fs/cgroup
tmpfs            3455152    51320   3403832   2% /tmp
tmpfs             691028       44    690984   1% /run/user/1000
"""


EXPECTED_BaseExecutor_OK = {
    1: {
        "Filesystem": "dev",
        "1K-blocks": "3446604",
        "Used": "0",
        "Available": "3446604",
        "Use%": "0%",
        "Mounted on": "/dev"
    },
    2: {
        "Filesystem": "run",
        "1K-blocks": "3455152",
        "Used": "1320",
        "Available": "3453832",
        "Use%": "1%",
        "Mounted on": "/run"
    },
    3: {
        "Filesystem": "/dev/sda4",
        "1K-blocks": "194354092",
        "Used": "41257996",
        "Available": "143153764",
        "Use%": "23%",
        "Mounted on": "/"
    },
    4: {
        "Filesystem": "tmpfs",
        "1K-blocks": "3455152",
        "Used": "199556",
        "Available": "3255596",
        "Use%": "6%",
        "Mounted on": "/dev/shm"
    },
    5: {
        "Filesystem": "tmpfs",
        "1K-blocks": "3455152",
        "Used": "0",
        "Available": "3455152",
        "Use%": "0%",
        "Mounted on": "/sys/fs/cgroup"
    },
    6: {
        "Filesystem": "tmpfs",
        "1K-blocks": "3455152",
        "Used": "51320",
        "Available": "3403832",
        "Use%": "2%",
        "Mounted on": "/tmp"
    },
    7: {
        "Filesystem": "tmpfs",
        "1K-blocks": "691028",
        "Used": "44",
        "Available": "690984",
        "Use%": "1%",
        "Mounted on": "/run/user/1000"
    }
}


SUB_DF_I_OUTPUT = """
Filesystem     Inodes IUsed IFree IUse% Mounted on
dev              861651    528   861123    1% /dev
run              863788    797   862991    1% /run
/dev/sda4      12410880 402194 12008686    4% /
"""


EXPECTED_INODEPARSER = {
    1: {
        "Filesystem": "dev",
        "Inodes": "861651",
        "IUsed": "528",
        "IFree": "861123",
        "IUse%": "1%",
        "Mounted on": "/dev"
    },
    2: {
        "Filesystem": "run",
        "Inodes": "863788",
        "IUsed": "797",
        "IFree": "862991",
        "IUse%": "1%",
        "Mounted on": "/run"
    },
    3: {
        "Filesystem": "/dev/sda4",
        "Inodes": "12410880",
        "IUsed": "402194",
        "IFree": "12008686",
        "IUse%": "4%",
        "Mounted on": "/"
    }}


SUB_DF_H_OUTPUT = """
Filesystem      Size  Used Avail Use% Mounted on
dev             3.3G     0  3.3G   0% /dev
run             3.3G  1.3M  3.3G   1% /run
/dev/sda4       186G   40G  137G  23% /
"""


EXPECTED_HUMAN_OK = {
    1: {
        "Filesystem": "dev",
        "Size": "3.3G",
        "Used": "0",
        "Avail": "3.3G",
        "Use%": "0%",
        "Mounted on": "/dev"
    },
    2: {
        "Filesystem": "run",
        "Size": "3.3G",
        "Used": "1.3M",
        "Avail": "3.3G",
        "Use%": "1%",
        "Mounted on": "/run"
    },
    3: {
        "Filesystem": "/dev/sda4",
        "Size": "186G",
        "Used": "40G",
        "Avail": "137G",
        "Use%": "23%",
        "Mounted on": "/"
    }}


TEST_RESULT_OUTPUT = {"1":
                      {'Available': '832672', 'Use%': '20%',
                       'Used': '205664', '1K-blocks': '1038336',
                       'Filesystem': '/dev/sda1', 'Mounted on': '/boot'}}

TEST_RESULT_EXPECTED = """{
    "status": "success",
    "error": "",
    "result": {
        "1": {
            "Available": "832672",
            "Use%": "20%",
            "Used": "205664",
            "1K-blocks": "1038336",
            "Filesystem": "/dev/sda1",
            "Mounted on": "/boot"
        }
    }
}"""

TEST_RESULT_EXP_ERROR = """{
    "status": "failure",
    "error": "Error",
    "result": null
}"""

RETURN_CODE_ERROR = 1
RETURN_CODE_OK = 0
ERROR_MESSAGE_OK = ""
ERROR_MESSAGE_IF_ERROR = 'Error'
