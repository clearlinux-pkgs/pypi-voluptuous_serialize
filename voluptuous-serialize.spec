#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : voluptuous-serialize
Version  : 2.1.0
Release  : 4
URL      : https://files.pythonhosted.org/packages/62/fb/ee79dabf3b425ac6b8efcef455f64ba29acd981bb286452feda46f3b87b5/voluptuous-serialize-2.1.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/62/fb/ee79dabf3b425ac6b8efcef455f64ba29acd981bb286452feda46f3b87b5/voluptuous-serialize-2.1.0.tar.gz
Summary  : Convert voluptuous schemas to dictionaries
Group    : Development/Tools
License  : Apache-2.0
Requires: voluptuous-serialize-python = %{version}-%{release}
Requires: voluptuous-serialize-python3 = %{version}-%{release}
Requires: voluptuous
BuildRequires : buildreq-distutils3
BuildRequires : voluptuous

%description
# Voluptuous Serialize
Convert Voluptuous schemas to dictionaries so they can be serialized.

%package python
Summary: python components for the voluptuous-serialize package.
Group: Default
Requires: voluptuous-serialize-python3 = %{version}-%{release}

%description python
python components for the voluptuous-serialize package.


%package python3
Summary: python3 components for the voluptuous-serialize package.
Group: Default
Requires: python3-core

%description python3
python3 components for the voluptuous-serialize package.


%prep
%setup -q -n voluptuous-serialize-2.1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1547654645
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
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
