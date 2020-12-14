#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : voluptuous-serialize
Version  : 2.4.0
Release  : 16
URL      : https://files.pythonhosted.org/packages/c5/70/e9248a3dfe1bb8fbc8ee2befb45bfe724989f2db943a4d2033623b0518c8/voluptuous-serialize-2.4.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c5/70/e9248a3dfe1bb8fbc8ee2befb45bfe724989f2db943a4d2033623b0518c8/voluptuous-serialize-2.4.0.tar.gz
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
Provides: pypi(voluptuous_serialize)
Requires: pypi(voluptuous)

%description python3
python3 components for the voluptuous-serialize package.


%prep
%setup -q -n voluptuous-serialize-2.4.0
cd %{_builddir}/voluptuous-serialize-2.4.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1593192085
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
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
