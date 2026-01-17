Name:          todo.txt-cli
Version:       2.13.0
Release:       1%{?dist}

Summary:       A simple and extensible shell script for managing your todo.txt file
License:       GPL-3.0-only
URL:           https://github.com/todotxt/todo.txt-cli
Source:        %{url}/archive/refs/tags/v%{version}.tar.gz

BuildArch:     noarch
BuildRequires: make

Requires:      bash
Recommends:    bash-completion

%description
A simple but powerful shell script called todo.sh that lets you interact with
todo.txt at the command line for quick and easy, Unix-y access. It supports
archiving completed tasks to done.txt and priority/context tab autocompletion.

%prep
%setup -q
sed -i "s/^DEF_VER=v[0-9.]*\$/DEF_VER=v%{version}/" GEN-VERSION-FILE
sed -i '1s,/usr/bin/env bash,%{_bindir}/bash,' todo.sh
sed -i "s/@DEV_VERSION@/%{version}/" todo.sh

%build
make

%install
make install CONFIG_DIR=%{buildroot}%{_sysconfdir} \
             INSTALL_DIR=%{buildroot}%{_bindir} \
             BASH_COMPLETION=%{buildroot}%{_datadir}/bash-completion/completions

%check
make test

%files
%dir %{_sysconfdir}/todo
%config(noreplace) %{_sysconfdir}/todo/config
%{_bindir}/todo.sh
%{_datadir}/bash-completion/completions/todo.sh
%doc CHANGELOG.md README.md USAGE.md
%license LICENSE

%changelog
* Thu Jan 15 2026 Eugene Zamriy <eugene@zamriy.ru> - 2.13.0-1
- Initial package
