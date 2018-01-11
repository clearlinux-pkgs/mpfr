#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x980C197698C3739D (vincent@vinc17.net)
#
Name     : mpfr
Version  : 4.0.0
Release  : 22
URL      : https://ftp.gnu.org/gnu/mpfr/mpfr-4.0.0.tar.xz
Source0  : https://ftp.gnu.org/gnu/mpfr/mpfr-4.0.0.tar.xz
Source99 : https://ftp.gnu.org/gnu/mpfr/mpfr-4.0.0.tar.xz.sig
Summary  : C library for multiple-precision floating-point computations
Group    : Development/Tools
License  : GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
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
%setup -q -n mpfr-4.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1515687449
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FCFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export FFLAGS="$CFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
export CXXFLAGS="$CXXFLAGS -O3 -falign-functions=32 -ffat-lto-objects -flto=4 -fno-math-errno -fno-semantic-interposition -fno-trapping-math "
%configure --disable-static
make  %{?_smp_mflags}

%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1515687449
rm -rf %{buildroot}
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/*.h
/usr/lib64/libmpfr.so
/usr/lib64/pkgconfig/mpfr.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/mpfr/*
%doc /usr/share/info/*

%files lib
%defattr(-,root,root,-)
/usr/lib64/libmpfr.so.6
/usr/lib64/libmpfr.so.6.0.0
