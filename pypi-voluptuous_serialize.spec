#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-voluptuous_serialize
Version  : 2.6.0
Release  : 42
URL      : https://files.pythonhosted.org/packages/42/09/c26b38ab35d9f61e9bf5c3e805215db1316dd73c77569b47ab36a40d19b1/voluptuous-serialize-2.6.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/42/09/c26b38ab35d9f61e9bf5c3e805215db1316dd73c77569b47ab36a40d19b1/voluptuous-serialize-2.6.0.tar.gz
Summary  : Convert voluptuous schemas to dictionaries
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-voluptuous_serialize-license = %{version}-%{release}
Requires: pypi-voluptuous_serialize-python = %{version}-%{release}
Requires: pypi-voluptuous_serialize-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pypi(voluptuous)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# Voluptuous Serialize
Convert Voluptuous schemas to dictionaries so they can be serialized.

%package license
Summary: license components for the pypi-voluptuous_serialize package.
Group: Default

%description license
license components for the pypi-voluptuous_serialize package.


%package python
Summary: python components for the pypi-voluptuous_serialize package.
Group: Default
Requires: pypi-voluptuous_serialize-python3 = %{version}-%{release}

%description python
python components for the pypi-voluptuous_serialize package.


%package python3
Summary: python3 components for the pypi-voluptuous_serialize package.
Group: Default
Requires: python3-core
Provides: pypi(voluptuous_serialize)
Requires: pypi(voluptuous)

%description python3
python3 components for the pypi-voluptuous_serialize package.


%prep
%setup -q -n voluptuous-serialize-2.6.0
cd %{_builddir}/voluptuous-serialize-2.6.0
pushd ..
cp -a voluptuous-serialize-2.6.0 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1676517395
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FCFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export FFLAGS="$FFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export CXXFLAGS="$CXXFLAGS -fdebug-types-section -femit-struct-debug-baseonly -fno-lto -g1 -gno-column-info -gno-variable-location-views -gz "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-voluptuous_serialize
cp %{_builddir}/voluptuous-serialize-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/pypi-voluptuous_serialize/894a04ac1d0e0ff0bd046a3809f98ddd80459496 || :
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-voluptuous_serialize/894a04ac1d0e0ff0bd046a3809f98ddd80459496

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
