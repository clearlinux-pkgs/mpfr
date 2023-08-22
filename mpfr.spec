#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
#
# Source0 file verified with key 0x5831D11A0D4DB02A (vincent@vinc17.net)
#
Name     : mpfr
Version  : 4.2.1
Release  : 46
URL      : https://mirrors.kernel.org/gnu/mpfr/mpfr-4.2.1.tar.xz
Source0  : https://mirrors.kernel.org/gnu/mpfr/mpfr-4.2.1.tar.xz
Source1  : https://mirrors.kernel.org/gnu/mpfr/mpfr-4.2.1.tar.xz.sig
Summary  : C library for multiple-precision floating-point computations
Group    : Development/Tools
License  : GFDL-1.2 GPL-3.0 GPL-3.0+ LGPL-3.0 LGPL-3.0+
Requires: mpfr-info = %{version}-%{release}
Requires: mpfr-lib = %{version}-%{release}
Requires: mpfr-license = %{version}-%{release}
BuildRequires : buildreq-configure
BuildRequires : gmp-dev
BuildRequires : sed
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
Contributed by the AriC and Caramba projects, INRIA.
This file is part of the GNU MPFR Library.

%package dev
Summary: dev components for the mpfr package.
Group: Development
Requires: mpfr-lib = %{version}-%{release}
Provides: mpfr-devel = %{version}-%{release}
Requires: mpfr = %{version}-%{release}

%description dev
dev components for the mpfr package.


%package doc
Summary: doc components for the mpfr package.
Group: Documentation
Requires: mpfr-info = %{version}-%{release}

%description doc
doc components for the mpfr package.


%package info
Summary: info components for the mpfr package.
Group: Default

%description info
info components for the mpfr package.


%package lib
Summary: lib components for the mpfr package.
Group: Libraries
Requires: mpfr-license = %{version}-%{release}

%description lib
lib components for the mpfr package.


%package license
Summary: license components for the mpfr package.
Group: Default

%description license
license components for the mpfr package.


%prep
%setup -q -n mpfr-4.2.1
cd %{_builddir}/mpfr-4.2.1
pushd ..
cp -a mpfr-4.2.1 buildavx2
popd
pushd ..
cp -a mpfr-4.2.1 buildavx512
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1692720108
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FCFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export FFLAGS="$FFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
export CXXFLAGS="$CXXFLAGS -O3 -Ofast -falign-functions=32 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fno-semantic-interposition -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
%configure --disable-static
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3"
%configure --disable-static
make  %{?_smp_mflags}
popd
unset PKG_CONFIG_PATH
pushd ../buildavx512/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512 -Wl,-z,x86-64-v4 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v4 -mprefer-vector-width=512"
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v4"
%configure --disable-static
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check || :
cd ../buildavx2;
make %{?_smp_mflags} check || : || :
cd ../buildavx512;
make %{?_smp_mflags} check || : || :

%install
export SOURCE_DATE_EPOCH=1692720108
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/mpfr
cp %{_builddir}/mpfr-%{version}/COPYING %{buildroot}/usr/share/package-licenses/mpfr/31a3d460bb3c7d98845187c716a30db81c44b615 || :
cp %{_builddir}/mpfr-%{version}/COPYING.LESSER %{buildroot}/usr/share/package-licenses/mpfr/a8a12e6867d7ee39c21d9b11a984066099b6fb6b || :
pushd ../buildavx2/
%make_install_v3
popd
pushd ../buildavx512/
%make_install_v4
popd
%make_install
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}
/usr/bin/elf-move.py avx512 %{buildroot}-v4 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/mpf2mpfr.h
/usr/include/mpfr.h
/usr/lib64/libmpfr.so
/usr/lib64/pkgconfig/mpfr.pc

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/mpfr/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/mpfr.info

%files lib
%defattr(-,root,root,-)
/V3/usr/lib64/libmpfr.so.6.2.1
/V4/usr/lib64/libmpfr.so.6.2.1
/usr/lib64/libmpfr.so.6
/usr/lib64/libmpfr.so.6.2.1

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/mpfr/31a3d460bb3c7d98845187c716a30db81c44b615
/usr/share/package-licenses/mpfr/a8a12e6867d7ee39c21d9b11a984066099b6fb6b
