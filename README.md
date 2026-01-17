# todo.txt-cli RPM package

This repository contains the RPM package files for
[todo.txt-cli](https://github.com/todotxt/todo.txt-cli) - a simple and
extensible shell script for managing your `todo.txt` file.

## Installation

RPM packages are built in [OBS](https://build.opensuse.org/) and available for
installation:

* AlmaLinux OS 9 and other EL 9 derivatives:
  ```shell
  $ sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/home:/R3XDW:/desktop:/EL:/9/AlmaLinux_9/home:R3XDW:desktop:EL:9.repo

  $ sudo rpm --import https://download.opensuse.org/repositories/home:/R3XDW:/desktop:/EL:/9/AlmaLinux_9/repodata/repomd.xml.key

  $ sudo dnf install todo.txt-cli
  ```

* AlmaLinux OS 10 and other EL 10 derivatives:
  ```shell
  $ sudo dnf config-manager --add-repo https://download.opensuse.org/repositories/home:/R3XDW:/desktop:/EL:/10/AlmaLinux_10/home:R3XDW:desktop:EL:10.repo

  $ sudo rpm --import https://download.opensuse.org/repositories/home:/R3XDW:/desktop:/EL:/10/AlmaLinux_10/repodata/repomd.xml.key

  $ sudo dnf install todo.txt-cli
  ```

* openSUSE Leap 16.0:
  ```shell
  $ sudo zypper addrepo https://download.opensuse.org/repositories/home:/R3XDW:/desktop:/Leap:/16/openSUSE_Leap_16.0/home:R3XDW:desktop:Leap:16.repo

  $ sudo zypper install todo.txt-cli
  ```

## Licensing

* The `todo.txt-cli` upstream project is licensed under
  [GPLv3](https://github.com/todotxt/todo.txt-cli/blob/master/LICENSE).
* The RPM package files in this repository are licensed under
  [MIT](LICENSE).
