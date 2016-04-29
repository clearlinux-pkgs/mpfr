#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mpfr
Version  : 3.1.4
Release  : 13
URL      : http://mirrors.kernel.org/gnu/mpfr/mpfr-3.1.4.tar.bz2
Source0  : http://mirrors.kernel.org/gnu/mpfr/mpfr-3.1.4.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: mpfr-lib
Requires: mpfr-doc
BuildRequires : gmp-dev
BuildRequires : sed

%description
Contributed by the AriC and Caramba projects, INRIA.
This file is part of the GNU MPFR Library.

%package dev
Summary: dev components for the mpfr package.
Group: Development
Requires: mpfr-lib
Provides: mpfr-devel

%description dev
dev components for the mpfr package.


%package doc
Summary: doc components for the mpfr package.
Group: Documentation

%description doc
doc components for the mpfr package.


%package lib
Summary: lib components for the mpfr package.
Group: Libraries

%description lib
lib components for the mpfr package.


%prep
%setup -q -n mpfr-3.1.4

%build
%configure --disable-static
make V=1  %{?_smp_mflags}

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/*.so

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/mpfr/*
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/*.so.*
