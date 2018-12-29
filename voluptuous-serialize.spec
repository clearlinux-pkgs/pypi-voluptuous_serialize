#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : voluptuous-serialize
Version  : 2.0.0
Release  : 2
URL      : https://files.pythonhosted.org/packages/66/fd/c3e522ce5645686b9712d230e3599fca12bdf5f76b8176da26d19c3852db/voluptuous-serialize-2.0.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/fd/c3e522ce5645686b9712d230e3599fca12bdf5f76b8176da26d19c3852db/voluptuous-serialize-2.0.0.tar.gz
Summary  : Convert voluptuous schemas to dictionaries
Group    : Development/Tools
License  : Apache-2.0
Requires: voluptuous-serialize-python3
Requires: voluptuous-serialize-python
Requires: voluptuous
BuildRequires : buildreq-distutils3
BuildRequires : voluptuous

%description
# Voluptuous Serialize
Convert Voluptuous schemas to dictionaries so they can be serialized.

%package python
Summary: python components for the voluptuous-serialize package.
Group: Default
Requires: voluptuous-serialize-python3

%description python
python components for the voluptuous-serialize package.


%package python3
Summary: python3 components for the voluptuous-serialize package.
Group: Default
Requires: python3-core

%description python3
python3 components for the voluptuous-serialize package.


%prep
%setup -q -n voluptuous-serialize-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1534860291
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
